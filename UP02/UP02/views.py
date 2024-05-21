"""
Routes and views for the flask application.
"""

from datetime import datetime
import io
import json
import os
import time
from flask import Response, request, jsonify, send_file
from flask import abort, make_response, render_template, render_template_string
from UP02 import app
from .code import *
import numpy as np
import pandas as pd


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Контакты',
        year=datetime.now().year,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/theory')
def theory():
    """Renders the theory page."""
    return render_template(
        'theory.html',
        title="Theory",
                year=datetime.now().year
    )

def get_resume(r_square_linear, r_square_quadratic):
    try:
        if r_square_linear < r_square_quadratic:
            if r_square_linear == r_square_quadratic:
                return "На допустимой точности ни одна из функций не имеет преимущества"
            if r_square_linear == 999 or r_square_quadratic == 999:
                return "Невозможно сравнить функции"
            return "Квадратичная функция аппроксимурует данные лучше"
        return "Линейная функция аппроксимурует данные лучше"
    except:
        return "Невозможно сравнить функции"


@app.route('/load-html/<file>/<tag>', methods=['POST'])
def process_data(file, tag):
    data = input_validate(request.get_json())
    if not isinstance(data, list):
        with open(f'UP02\\UP02\\templates\\uncorrect_input.html', 'r', encoding="utf-8") as f:
            html = f.read()
            response = make_response(render_template_string(html, tag=tag, error_message=data))
            response.headers['Content-Type'] = 'text/html; charset=UTF-8'
            return response 
    
    # <линеная регрессия>
    a0, a1 = linear_approximation(np.array(data[0]), np.array(data[1]))
    # </линеная регрессия>

    # <квадратичная регрессия>
    quadratic = Quadratic(np.array(data[0]), np.array(data[1]))
    a, b, c = quadratic.getCoefs()
    # </квадратичная регрессия>
        
    # <сравнение>
    regression_metrics = RegressionMetrics(a0, a1, a, b, c, np.array(data[0]), np.array(data[1]))
    r_square_linear, correlation_linear = regression_metrics.linear_regression_metrics()
    r_square_quadratic, correlation_quadratic = regression_metrics.quadratic_regression_metrics()
    chart = regression_metrics.get_chart()
    # </сравнение>

    # <прирост>
    # вызываем функцию dynamic_series_calculations
    df, y, delta_y, T = dynamic_series_calculations(np.array(data[0]), np.array(data[1]))
    # конвертируем все столбцы в числовые типы данных, если это возможно
    df = df.apply(pd.to_numeric, errors='ignore')
    # преобразуем данные в HTML-код таблицы
    html_table = df.to_html(index=False, header=False)
    html_table = html_table.replace('&lt;', '<').replace('&gt;', '>')
    # </прирост>

    data_dump = OutputData(a0, a1, a, b, c, r_square_linear, correlation_linear, r_square_quadratic, correlation_quadratic, "no chart", get_resume(r_square_linear, r_square_quadratic))

    with open(f'UP02\\UP02\\templates\\{file}', 'r', encoding="utf-8") as f:
        html = f.read()
        response: Response = None
        if file == "comparison.html":
            response = make_response(render_template_string(html,
                                                             tag=tag,
                                                             r_square_linear=r_square_linear,
                                                             correlation_linear=correlation_linear,
                                                             r_square_quadratic=r_square_quadratic,
                                                             correlation_quadratic=correlation_quadratic,
                                                             chart=chart,
                                                             resume=get_resume(r_square_linear, r_square_quadratic)))
        elif file == "approximation.html":
            response = make_response(render_template_string(html, 
                                                            tag=tag, 
                                                            a0=a0, a1=a1, 
                                                            r_square_linear=r_square_linear,
                                                            a=a, b=b, c=c, 
                                                            r_square_quadratic=r_square_quadratic))
        elif file == "analyzing.html":
            # используем метод render_template_string, чтобы сгенерировать HTML-код страницы
            html = render_template_string(html, tag=tag, table=html_table, y=y, delta_y=delta_y, T=T)

            response = make_response(html)
        else:
            response = make_response(render_template_string(html, tag=tag))

        json_data = json.dumps(data_dump.to_json(), indent=4)
        client_ip = request.remote_addr
        with open(f"UP02\\UP02\\tmp\\{client_ip}.json", "w+") as f:
            f.write(json_data)

        response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        return response
    

def input_validate(data: list) -> list | str:
    """
    Валидация и преобразование входных данных
    """
    try:
        for idx, row in enumerate(data):
            if len(row) < 3:
                return "Нужно 3 и более точек для аппроксимации!"
            for idy, col in enumerate(row):
                try:
                    tmp_for_err = row[idy]
                    row[idy] = float(col)
                    if ((idx == 0) and (idy > 0) and (row[idy] <= row[idy - 1])):
                        return f"Значение '{tmp_for_err}' [позиция {idx}; {idy}] нарушает прямую последовательность аргумента функции!"
                        
                except ValueError as ve:
                    t = ve.args[0].split('\'')[1]
                    return f"Значение '{t}' [позиция {idx}; {idy}] не может быть преобразовано во float!"
        return data
    except Exception as e:
        return "Ошибка ввода!"


@app.route('/download_json')
def download_json():
    json_data = ""
    client_ip = request.remote_addr
    try:
        with open(f"UP02\\UP02\\tmp\\{client_ip}.json", "r") as f:
            json_data = f.read()
        os.remove(f"UP02\\UP02\\tmp\\{client_ip}.json")
    except:
        return "No data to download!"

    if json_data is None or json_data == "":
        return "No data to download."

    # Создаем файл-объект в памяти для записи JSON данных избегая записи на диск
    memory_file = io.BytesIO()
    memory_file.write(json_data.encode('utf-8'))
    memory_file.seek(0)
    
    # Отправляем файл 
    return send_file(memory_file, as_attachment=True, download_name='data.json', mimetype='application/json')

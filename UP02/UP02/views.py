"""
Routes and views for the flask application.
"""

from datetime import datetime
import os
import time
from flask import Response, request, jsonify
from flask import abort, make_response, render_template, render_template_string
from UP02 import app
from .code import RegressionMetrics


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


@app.route('/load-html/<file>/<tag>', methods=['POST'])
def process_data(file, tag):
    data = input_validate(request.get_json())
    if data is None:
        return "<h1>Не корректные входные данные!</h1>"
    with open(f'UP02/UP02/templates/{file}', 'r', encoding="utf-8") as f:
        html = f.read()
        response: Response = None
        if file == "comparison.html":
            import numpy as np
            regression_metrics = RegressionMetrics(1.4285714285714282, 0.7619047619047606, 0.1249999999980923, 0.803571428570997, 1.178571428571822, np.array([0, 1, 2, 3, 4, 5]), np.array([1, 3, 2, 5, 7, 8]))
            r_square_linear, correlation_linear = regression_metrics.linear_regression_metrics()
            r_square_quadratic, correlation_quadratic = regression_metrics.quadratic_regression_metrics()
            chart = regression_metrics.get_chart()
            resume_compare=lambda r_square_linear, r_square_quadratic: "Квадратичная функция аппроксимурует данные лучше" if r_square_linear < r_square_quadratic else "На допустимой точности ни одна из функций не имеет преимущества" if r_square_linear == r_square_quadratic else "Линейная функция аппроксимурует данные лучше"
            response = make_response(render_template_string(html,
                                                             tag=tag,
                                                             r_square_linear=r_square_linear,
                                                             correlation_linear=correlation_linear,
                                                             r_square_quadratic=r_square_quadratic,
                                                             correlation_quadratic=correlation_quadratic,
                                                             chart=chart,
                                                             resume=resume_compare(r_square_linear, r_square_quadratic)))
        else:
            response = make_response(render_template_string(html, tag=tag))
        response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        return response
    

def input_validate(data: list[str]) -> list | None:
    res = list()
    try:
        for row in data:
            res.append([float(i) for i in row])
        return res
    except Exception as e:
        return None

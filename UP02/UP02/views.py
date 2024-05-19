"""
Routes and views for the flask application.
"""

from datetime import datetime
import os
import time
from flask import request, jsonify
from flask import abort, make_response, render_template, render_template_string
from UP02 import app
from .code import create_chart

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

"""
Routes and views for the flask application.
"""

from datetime import datetime
import os
from flask import abort, render_template, render_template_string
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
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
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


@app.route('/load-html/<file>/<tag>')
def load_html(file, tag):
    with open(f'UP02/templates/{file}', 'r') as f:
        html = f.read()
        if file == "comparison.html":
            chart = create_chart()
            return render_template_string(html, tag=tag, chart=chart)
        return render_template_string(html, tag=tag)


@app.route('/theory')
def theory():
    """Renders the theory page."""
    return render_template(
        'theory.html',
        title="Theory",
                year=datetime.now().year
    )
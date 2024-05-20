"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

try:
    import UP02.views
except ImportError:
    ...
    
from .code import *
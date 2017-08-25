""" views.py """
from flask import render_template, request
from app import app

@app.route('/')
def index():
    """Handles rendering of index page
    """
    return render_template("index.html")
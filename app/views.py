""" views.py """
from flask import render_template
from app import app

@app.route('/')
def index():
    """Handles rendering of index page
    """
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles registeration of users
    """
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in
    """
    return render_template("login.html")

@app.route('/shoppinglist', methods=['GET', 'POST'])
def shoppinglist():
    """Handles shopping list creation
    """
    return render_template('shoppinglist.html')

@app.route('/shoppingitems', methods=['GET', 'POST'])
def shoppingitems():
    """Handles shopping items creation
    """
    return render_template('shoppingitems.html')

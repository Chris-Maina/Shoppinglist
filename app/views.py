""" views.py """
from flask import render_template, request, session
from app import app, user_object

@app.route('/')
def index():
    """Handles rendering of index page
    """
    return render_template("index.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handles registeration of users
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['confirm-password']

        msg = user_object.registeruser(username, email, password, cpassword)
        if msg == "Successfully registered. You can now login!":
            return render_template("login.html", resp=msg)
        else:
            return render_template("register.html", resp=msg)

    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        msg = user_object.login(email, password)
        if msg == "Successfully logged in, create buckets!":
            session['email'] = email
            session['logged_in'] = True
            return render_template('shoppinglist.html', resp=msg)
        else:
            return render_template('login.html', resp=msg)
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

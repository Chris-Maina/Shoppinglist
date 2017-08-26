""" views.py """
from flask import render_template, request, session
from app import app, user_object, shoplist_obj

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
    user = session['email']
    user_lists = shoplist_obj.get_owner(user)
    if request.method == 'POST':
        list_name = request.form['list-name']
        msg = shoplist_obj.create_list(list_name, user)
        if isinstance(msg, list):
            return render_template('shoppinglist.html', shoppinglist=msg)
        else:
            return render_template('shoppinglist.html', resp=msg, shoppinglist=user_lists)
    return render_template('shoppinglist.html', shoppinglist=user_lists)

@app.route('/edit-list', methods=['GET', 'POST'])
def save_edits():
    """ Handles editing of shopping lists """

    user = session['email']
    user_lists = shoplist_obj.get_owner(user)
    if request.method == 'POST':
        edit_name = request.form['list_name']
        org_name = request.form['list_name_org']
        msg = shoplist_obj.edit_list(edit_name, org_name, user)
        if msg == shoplist_obj.shopping_list:
            response = "Successfully edited bucket " + org_name
            return render_template('shoppinglist.html', resp=response, shoppinglist=msg)
        else:
            #existing = shoplist_obj.shopping_list
            return render_template('shoppinglist.html', resp=msg, shoppinglist=user_lists)
    return render_template('shoppinglist.html')

@app.route('/delete-list', methods=['GET', 'POST'])
def delete_shoppinglist():
    """Handles deletion of shoppinglist and its items
    """
    user = session['email']
    if request.method == 'POST':
        del_name = request.form['list_name']
        msg = shoplist_obj.delete_list(del_name, user)
        # Delete the its activies
        #activity_object.deleted_bucket_activities(del_name)
        response = "Successfuly deleted bucket " + del_name
        return render_template('shoppinglist.html', resp=response, shoppinglist=msg)

@app.route('/shoppingitems', methods=['GET', 'POST'])
def shoppingitems():
    """Handles shopping items creation
    """
    return render_template('shoppingitems.html')

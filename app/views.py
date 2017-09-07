""" views.py """
from functools import wraps
from flask import render_template, request, session
from app import app, user_object, shoplist_obj, shopitems_obj

# Variable stores user's email
user = None


def authorize(f):
    """Function to authenticate users when accessing other pages"""
    @wraps(f)
    def check(*args, **kwargs):
        """Function to check login status"""
        if "email" in session:
            return f(*args, **kwargs)
        msg = "Please login"
        return render_template("login.html", resp=msg)
    return check


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
        if msg == "Successfully logged in, create shoppinglist!":
            session['email'] = email
            global user
            user = email
            user_lists = shoplist_obj.get_owner(user)
            return render_template('shoppinglist.html', resp=msg, shoppinglist=user_lists)
        return render_template('login.html', resp=msg)
    return render_template("login.html")


@app.route('/shoppinglist', methods=['GET', 'POST'])
@authorize
def shoppinglist():
    """Handles shopping list creation
    """
    if user == session['email']:
        user_lists = shoplist_obj.get_owner(user)
    if request.method == 'POST':
        list_name = request.form['list-name']
        msg = shoplist_obj.create_list(list_name, user)
        if isinstance(msg, list):
            return render_template('shoppinglist.html', shoppinglist=msg)
        return render_template('shoppinglist.html', resp=msg, shoppinglist=user_lists)
    return render_template('shoppinglist.html', shoppinglist=user_lists)


@app.route('/edit-list', methods=['GET', 'POST'])
@authorize
def save_edits():
    """ Handles editing of shopping lists """
    user_lists = shoplist_obj.get_owner(user=user)
    if request.method == 'POST':
        edit_name = request.form['list_name']
        org_name = request.form['list_name_org']
        msg = shoplist_obj.edit_list(edit_name, org_name, user)
        if msg == shoplist_obj.shopping_list:
            response = "Successfully edited bucket " + org_name
            return render_template('shoppinglist.html', resp=response, shoppinglist=msg)
        #existing = shoplist_obj.shopping_list
        return render_template('shoppinglist.html', resp=msg, shoppinglist=user_lists)
    return render_template('shoppinglist.html')


@app.route('/delete-list', methods=['GET', 'POST'])
@authorize
def delete_shoppinglist():
    """Handles deletion of shoppinglist and its items
    """
    if request.method == 'POST':
        del_name = request.form['list_name']
        msg = shoplist_obj.delete_list(del_name, user=user)
        # Delete the its items
        shopitems_obj.deleted_list_items(del_name)
        response = "Successfuly deleted bucket " + del_name
        return render_template('shoppinglist.html', resp=response, shoppinglist=msg)


@app.route('/shoppingitems/<shoplist>', methods=['GET', 'POST'])
@authorize
def shoppingitems(shoplist):
    """Handles shopping items creation
    """
    # Get a list of users items for a specific shopping list
    user_items = shopitems_obj.owner_items(user, shoplist)
    # specific shopping list
    new_list = [item['name']
                for item in user_items if item['list'] == shoplist]
    if request.method == 'POST':
        item_name = request.form['item-name']
        msg = shopitems_obj.add_item(shoplist, item_name, user)
        if isinstance(msg, list):
            new_list = [item['name']
                        for item in msg if item['list'] == shoplist]
            return render_template("shoppingitems.html", itemlist=new_list, name=shoplist)
        # msg is not a list
        return render_template("shoppingitems.html", resp=msg, name=shoplist, itemlist=new_list)
    else:
        res = "You can now add your items"
        return render_template('shoppingitems.html', resp=res, name=shoplist, itemlist=new_list)


@app.route('/edit-item', methods=['GET', 'POST'])
@authorize
def edit_item():
    """ Handles editing of items
    """
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_name_org = request.form['item_name_org']
        list_name = request.form['list_name']
        msg = shopitems_obj.edit_item(
            item_name, item_name_org, list_name, user)
        if isinstance(msg, list):
            res = "Successfully edited item " + item_name_org
            # Get edited list of the current shopping list
            newlist = [item['name']
                       for item in msg if item['list'] == list_name]
            return render_template("shoppingitems.html", itemlist=newlist, name=list_name, resp=res)
        else:
            # Get user's items in the current shopping list
            user_items = shopitems_obj.owner_items(user, list_name)
            new_list = [item['name']
                        for item in user_items if item['list'] == list_name]
    return render_template("shoppingitems.html", itemlist=new_list, name=list_name, resp=msg)


@app.route('/delete-item', methods=['GET', 'POST'])
@authorize
def delete_item():
    """ Handles deletion of items
    """
    if request.method == 'POST':
        item_name = request.form['item_name']
        list_name = request.form['list_name']
        msg = shopitems_obj.delete_item(item_name, user, list_name)
        response = "Successfuly deleted item " + item_name
        return render_template("shoppingitems.html", itemlist=msg, name=list_name, resp=response)


@app.route('/logout')
def logout():
    """Handles logging out of users"""
    session.pop('email', None)
    return render_template("index.html")

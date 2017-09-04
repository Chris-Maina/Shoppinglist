""" app/__init__.py """

from flask import Flask
from app import useraccounts, shoppinglist, shoppingitems

# Initialize the app
app = Flask(  # pylint: disable=invalid-name
    __name__, instance_relative_config=True)
app.secret_key = 'dresscodesleepbehappy'

user_object = useraccounts.UserClass()  # pylint: disable=invalid-name
shoplist_obj = shoppinglist.ShoppinglistClass()  # pylint: disable=invalid-name
shopitems_obj = shoppingitems.ShoppingItemsClass()  # pylint: disable=invalid-name
# Load the views
from app import views

# Load the config file
app.config.from_object('config')

""" app/__init__.py """

from flask import Flask
from app import useraccounts, shoppinglist, shoppingitems

# Initialize the app
app = Flask(
    __name__, instance_relative_config=True)
app.secret_key = 'dresscodesleepbehappy'

user_object = useraccounts.UserClass()
shoplist_obj = shoppinglist.ShoppinglistClass()
shopitems_obj = shoppingitems.ShoppingItemsClass()


# Load the config file
app.config.from_object('config')

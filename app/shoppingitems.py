"""shoppingitems.py"""
import re


class ShoppingItemsClass(object):
    """Handles creation,editing and deletion of shopping items
    """

    def __init__(self):
        # list to hold items within a shopping list
        self.item_list = []

    def owner_items(self, user):
        """Returns items belonging to a user
        Args
             user
        returns
            list of user's items
        """
        user_items = [item for item in self.item_list if item['owner'] == user]
        return user_items

    def add_item(self, listname, item_name, user):
        """Handles adding an item to a shopping list
            Args
                shopping list name
            result
                list of items
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9_]*$", item_name):
            # Get users items
            my_items = self.owner_items(user)
            for item in my_items:
                if item['name'] == item_name:
                    return "Shopping item name already exists"
            activity_dict = {
                'name': item_name,
                'list': listname,
                'owner': user
            }
            self.item_list.append(activity_dict)
            return self.owner_items(user)
        else:
            return "No special characters (. , ! space [] )"

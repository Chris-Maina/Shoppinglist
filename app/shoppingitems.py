"""shoppingitems.py"""
import re


class ShoppingItemsClass(object):
    """Handles creation,editing and deletion of shopping items
    """

    def __init__(self):
        # list to hold items within a shopping list
        self.item_list = []

    def owner_items(self, user, list_name):
        """Returns items belonging to a user
        Args
             user
        returns
            list of user's items
        """
        user_items = [item for item in self.item_list if item['owner']
                      == user and item['list'] == list_name]
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
            my_items = self.owner_items(user, listname)
            for item in my_items:
                if item['name'] == item_name:
                    return "Shopping item name already exists"
            activity_dict = {
                'name': item_name,
                'list': listname,
                'owner': user
            }
            self.item_list.append(activity_dict)
            return self.owner_items(user, listname)
        return "No special characters (. , ! space [] )"

    def edit_item(self, item_name, org_item_name, list_name, user):
        """Handles editing of items
            Args
                editted name and original name
            returns
                error message or a list of items
        """
        # Get users items
        my_items = self.owner_items(user, list_name)
        for item in my_items:
            if item['list'] == list_name:
                if item['name'] != item_name:
                    if item['name'] == org_item_name:
                        del item['name']
                        edit_dict = {
                            'name': item_name,
                        }
                        item.update(edit_dict)
                else:
                    return "Item name already exists"
        return my_items

    def delete_item(self, item_name, user, list_name):
        """Handles deletion of bucket activities
        Args
            activity name
        returns
            list with activity name removed
        """
        # Get users activities
        for item in range(len(self.item_list)):
            if self.item_list[item]['name'] == item_name:
                del self.item_list[item]
                break
        deleted_item_list = []
        my_items = self.owner_items(user, list_name)
        for shopping in my_items:
            deleted_item_list.append(shopping['name'])
        return deleted_item_list

    def deleted_list_items(self, list_name):
        """Delete items for the list that was deleted
        Args
             shopping list name
        """
        self.item_list[:] = [
            item for item in self.item_list if item.get('list') != list_name]

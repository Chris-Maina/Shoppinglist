""" shoppinglist.py """
import re


class ShoppinglistClass(object):
    """
    Handles creation of shopping lists
    """

    def __init__(self):
        # list to hold shopping list a user creates
        self.shopping_list = []

    def get_owner(self, user):
        """Returns shopping lists belonging to a user
        Args
            user
        returns
            list of user's list(s)
        """
        user_shopping_list = [
            item for item in self.shopping_list if item['owner'] == user]
        return user_shopping_list

    def create_list(self, list_name, user):
        """Handles creation of shopping lists
            Args
                list name
            result
                shopping lists
        """
        # Check for special characters
        if re.match("^[a-zA-Z0-9_]*$", list_name):
            # Get users shopping lists
            my_shopping_lists = self.get_owner(user)
            # check if bucket name exists
            for item in my_shopping_lists:
                if list_name == item['name']:
                    return "Shopping list name already exists."
            shopping_dict = {
                'name': list_name,
                'owner': user,
            }
            self.shopping_list.append(shopping_dict)
        else:
            return "No special characters (. , ! space [] )"
        return self.get_owner(user)

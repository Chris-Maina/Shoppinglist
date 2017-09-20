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
        if re.match("^[a-zA-Z0-9 _]*$", list_name):
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

    def edit_list(self, edit_name, org_name, user):
        """Handles edits made to shopping list name
            Args
                editted name and original name
            returns
                error message or a list of shopping
        """
        if re.match("^[a-zA-Z0-9 _]*$", edit_name):
            # Get users lists
            my_shopping_lists = self.get_owner(user)
            for item in my_shopping_lists:
                if edit_name != item['name']:
                    if org_name == item['name']:
                        edit_dict = {
                            'name': edit_name,
                        }
                        item.update(edit_dict)
                else:
                    return "Shopping list name already exists"
        else:
            return "No special characters (. , ! space [] )"
        return self.get_owner(user)

    def delete_list(self, list_name, user):
        """Handles removal of shopping lists using list comprehension
            Args
                 list name
            returns
                 list with name removed
        """
        # Delete shopping list with name = list_name
        for item in range(len(self.shopping_list)):
            if self.shopping_list[item]['name'] == list_name:
                del self.shopping_list[item]
                break
        # Get users shopping list
        my_shopping_lists = self.get_owner(user)
        return my_shopping_lists
    
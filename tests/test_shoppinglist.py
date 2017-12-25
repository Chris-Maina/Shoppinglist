"""test_buckets.py"""
import unittest
from app.shoppinglist import ShoppinglistClass


class TestCasesShoppingList(unittest.TestCase):
    """
    Test for existence of list in shopping list creation
    Test for special character in list names
    Test for owner of shopping list
    Test for correct output(shopping list creation)
    Test for deletion of existing shopping list
    Test for editing list names
    Test for editing listnames with existing listnames
    """

    def setUp(self):
        """Setting up ShoppinglistClass
        """
        self.shopping_class_obj = ShoppinglistClass()

    def tearDown(self):
        """Removing ShoppinglistClass
        """
        del self.shopping_class_obj

    def test_existing_shoppinglist(self):
        """Check to see bucket name exists or not
         """
        self.shopping_class_obj.shopping_list = \
            [{'owner': 'mainachrisw@gmail.com', 'name': 'Easter'},
             {'owner': 'mainachrisw@gmail.com', 'name': 'Christmass'}]
        msg = self.shopping_class_obj.create_list(
            "Easter", "mainachrisw@gmail.com")
        self.assertIn("name already exists.", msg)

    def test_special_characters(self):
        """Check for special characters in list name
        """
        user = "mainachrisw@gmail.com"
        msg = self.shopping_class_obj.create_list("Back.to-School", user)
        self.assertEqual(msg, "No special characters (. , ! space [] )")

    def test_owner(self):
        """ Check for shopping list belonging to owner"""
        self.shopping_class_obj.shopping_list = [{'owner': 'maina@gmail.com', 'name': 'Easter'},
                                                 {'owner': 'njekama@gmail.com',
                                                  'name': 'School'},
                                                 {'owner': 'maina@gmail.com', 'name': 'Christmass'}]
        user = "maina@gmail.com"
        msg = self.shopping_class_obj.get_owner(user)
        self.assertEqual(msg, [{'owner': 'maina@gmail.com', 'name': 'Easter'}, {
            'owner': 'maina@gmail.com', 'name': 'Christmass'}])

    def test_correct_output(self):
        """Check for correct shopping list creation
        """
        msg = self.shopping_class_obj.create_list(
            'Rave', "mainachrisw@gmail.com")
        self.assertEqual(
            msg, [{'owner': 'mainachrisw@gmail.com', 'name': 'Rave'}])

    def test_editing_shoppinglist(self):
        """Check for edits to shoppinglist name
        """
        self.shopping_class_obj.shopping_list = [{'owner': 'maina@gmail.com', 'name': 'Rave'}, {
            'owner': 'maina@gmail.com', 'name': 'Easter'}]
        msg = self.shopping_class_obj.edit_list(
            'Christmass', 'Rave', "maina@gmail.com")
        self.assertEqual(msg, [{'owner': 'maina@gmail.com', 'name': 'Christmass'}, {
            'owner': 'maina@gmail.com', 'name': 'Easter'}])

    def test_editing_invalid_shoppinglist_name(self):
        """Check for edits to shoppinglist name
        """
        self.shopping_class_obj.shopping_list = [{'owner': 'maina@gmail.com', 'name': 'Rave'}, {
            'owner': 'maina@gmail.com', 'name': 'Easter'}]
        msg = self.shopping_class_obj.edit_list(
            'Christmass!', 'Rave', "maina@gmail.com")
        self.assertIn("No special characters", msg)

    def test_edit_existing_shoppinglist(self):
        """Check if edit name provided is similar to an existing shoppinglist
        """
        self.shopping_class_obj.shopping_list = [{'owner': 'maina@gmail.com', 'name': 'Rave'}, {
            'owner': 'maina@gmail.com', 'name': 'Shagz'}]
        msg = self.shopping_class_obj.edit_list(
            'Shagz', 'Rave', "maina@gmail.com")
        self.assertIn("name already exists", msg)

    def test_delete_shoppinglist(self):
        """Check to see if shoppinglist is deleted
        """
        self.shopping_class_obj.shopping_list = \
            [{'owner': 'maina@gmail.com', 'name': 'Rave'},
             {'owner': 'maina@gmail.com', 'name': 'Adventure'},
             {'owner': 'maina@gmail.com', 'name': 'Shagz'}]
        msg = self.shopping_class_obj.delete_list(
            'Rave', "maina@gmail.com")
        self.assertEqual(msg,
                         [{'owner': 'maina@gmail.com', 'name': 'Adventure'},
                          {'owner': 'maina@gmail.com', 'name': 'Shagz'}])


if __name__ == '__main__':
    unittest.main()

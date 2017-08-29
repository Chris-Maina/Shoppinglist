"""test_shoppingitems.py"""
import unittest
from app.shoppingitems import ShoppingItemsClass


class TestCasesItems(unittest.TestCase):
    """
    Test for existence of activity in activity creation
    Test for special character activitynames
    Test for correct owner
    Test for correct output(activity creation)
    Test for deletion of existing activity
    Test for editing activity names
    Test for editing activity names with existing activity names
    Test for deletion of bucket with its activities
    """

    def setUp(self):
        """Setting up ShoppingItems class
        """
        self.item_class_obj = ShoppingItemsClass()

    def tearDown(self):
        """Removing ShoppingItems class
        """
        del self.item_class_obj

    def test_existing_item(self):
        """Check to see item name exists or not
         """
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'list': 'Easter', 'name': 'Bread'}, {
            'owner': 'maina@gmail.com', 'list': 'Easter', 'name': 'Blueband'}]
        msg = self.item_class_obj.add_item(
            "Easter", "Bread", "maina@gmail.com")
        self.assertEqual(msg, "Shopping item name already exists")

    def test_special_characters_name(self):
        """Check for special characters in item name
        """
        msg = self.item_class_obj.add_item(
            "Easter", "Bread!", "mainachrisw@gmail.com")
        self.assertEqual(msg, "No special characters (. , ! space [] )")

    def test_owner(self):
        """ Check for shopping items belonging to owner"""
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'list': 'Easter', 'name': 'Bread'},
                                         {'owner': 'njekama@gmail.com',
                                          'list': 'Easter', 'name': 'Blueband'},
                                         {'owner': 'maina@gmail.com', 'list': 'Easter', 'name': 'Blueband'}]
        user = "njekama@gmail.com"
        shoppinglist = "Easter"
        msg = self.item_class_obj.owner_items(user, shoppinglist)
        self.assertEqual(
            msg, [{'owner': 'njekama@gmail.com', 'list': 'Easter', 'name': 'Blueband'}])

    def test_correct_output_item(self):
        """Check for correct item creation
        """
        msg = self.item_class_obj.add_item(
            "Easter", "Bread", "mainachrisw@gmail.com")
        self.assertEqual(
            msg, [{'owner': 'mainachrisw@gmail.com', 'list': 'Easter', 'name': 'Bread'}])

    def test_editing_item(self):
        """Check for edits to item name
        """
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item_class_obj.edit_item(
            'Soda', 'Booze', 'Adventure', "maina@gmail.com")
        self.assertEqual(msg, [{'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Soda'}])

    def test_edit_existing_itemname(self):
        """Check if edit name provided is similar to an existing item
        """
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item_class_obj.edit_item(
            'Snacks', 'Booze', 'Adventure', "maina@gmail.com")
        self.assertEqual(msg, "Item name already exists")

    def test_delete_item(self):
        """Check to see if item is deleted
        """
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        msg = self.item_class_obj.delete_item(
            'Booze', "maina@gmail.com", 'Adventure')
        self.assertEqual(msg, ['Snacks'])

    def test_deleted_list(self):
        """Check if bucket deleted will have its activities deleted to
        """
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Snacks'}, {
            'owner': 'maina@gmail.com', 'list': 'Adventure', 'name': 'Booze'}]
        res = self.item_class_obj.deleted_list_items('Adventure')
        self.assertEqual(res, None)


if __name__ == '__main__':
    unittest.main()

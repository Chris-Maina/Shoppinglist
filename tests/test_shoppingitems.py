"""test_shoppingitems.py"""
import unittest
from app.shoppingitems import ShoppingItemsClass


class TestCasesItems(unittest.TestCase):
    """
    Test for existence of activity in activity creation
    Test for special character activitynames
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
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'bucket': 'Easter', 'name': 'Bread'}, {
            'owner': 'maina@gmail.com', 'bucket': 'Easter', 'name': 'Blueband'}]
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
        self.item_class_obj.item_list = [{'owner': 'maina@gmail.com', 'bucket': 'Easter', 'name': 'Bread'},
                                         {'owner': 'njekama@gmail.com',
                                          'bucket': 'Easter', 'name': 'Blueband'},
                                         {'owner': 'maina@gmail.com', 'bucket': 'Easter', 'name': 'Blueband'}]
        user = "njekama@gmail.com"
        msg = self.item_class_obj.owner_items(user)
        self.assertEqual(
            msg, [{'owner': 'njekama@gmail.com', 'bucket': 'Easter', 'name': 'Blueband'}])


if __name__ == '__main__':
    unittest.main()

"""Test routes"""
import unittest
from app import app
from app.shoppinglist import ShoppinglistClass
from app.shoppingitems import ShoppingItemsClass


class TestCaseViews(unittest.TestCase):
    """
    This class tests routes
    """

    def setUp(self):
        self.app = app.test_client()
        self.user_reg_details = {
            'username': 'chris',
            'email': 'mainachris@gmail.com',
            'password': 'password123',
            'confirm-password': 'password123'
        }
        self.user_login_details = {
            'email': 'mainachris@gmail.com',
            'password': 'password123'
        }
        self.shopping_class_obj = ShoppinglistClass()
        self.item_class_obj = ShoppingItemsClass()

    def tearDown(self):
        self.app = None
        self.user_reg_details = None
        self.user_login_details = None
        self.item_class_obj = None
        self.shopping_class_obj = None

    def test_index_page(self):
        """Test is root page is accessible"""
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)

    def test_registration_page(self):
        """Test is register page is accessible"""
        res = self.app.post('/register')
        self.assertEqual(res.status_code, 400)
        res = self.app.get('/register')
        self.assertEqual(res.status_code, 200)

    def test_correct_registration(self):
        """Test correct registration of user"""
        res = self.app.post('/register', data=self.user_reg_details)
        self.assertEqual(res.status_code, 200)

    def test_user_exists_error(self):
        """Test error in registration of user e.g user already exists"""
        user = {
            'username': 'chris',
            'email': 'mainachris@gmail.com',
            'password': 'password123',
            'confirm-password': 'password123'
        }
        res = self.app.post('/register', data=user)
        self.assertEqual(res.status_code, 200)
        self.assertIn("User already exists", str(res.data))

    def test_login_page(self):
        """Test is login page is accessible"""
        res = self.app.post('/login')
        self.assertEqual(res.status_code, 400)
        res = self.app.get('/login')
        self.assertEqual(res.status_code, 200)

    def test_correct_login(self):
        """Test correct login for registered user"""
        self.app.post('/register', data=self.user_reg_details)
        res = self.app.post('/login', data=self.user_login_details)
        self.assertEqual(res.status_code, 200)
        self.assertIn("Successfully logged in", str(res.data))

    def test_non_existing_user_login(self):
        """Test is login with non esisting user details"""
        user = {
            'email': 'test@gmail.com',
            'password': 'password123'}
        res = self.app.post('/login', data=user)
        self.assertEqual(res.status_code, 200)
        self.assertIn("You have no account", str(res.data))

    def test_shoppinglist_page(self):
        """Test is shoppinglist page is accessible"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # send a GET request
        res = self.app.get('/shoppinglist')
        self.assertEqual(res.status_code, 200)
        # check if page was loaded by looking for text in the page
        self.assertIn("Shopping List", str(res.data))

    def test_shoppinglist_creation(self):
        """Test is shoppinglist creation"""
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        res = self.app.post(
            '/shoppinglist', data={'list-name': 'Easter'})
        self.assertEqual(res.status_code, 200)
        response = self.shopping_class_obj.create_list(
            'Easter', 'maina@gmail.com')
        self.assertIsInstance(response, list)
        self.assertIn("Easter", str(res.data))

    def test_shoppinglist_creation_with_error(self):
        """Test is shoppinglist creation with special characters raises an error"""
        res = self.app.post(
            '/shoppinglist', data={'name': 'Easter!'})
        self.assertEqual(res.status_code, 200)
        response = self.shopping_class_obj.create_list(
            'Easter!', 'maina@gmail.com')
        self.assertIn("No special characters", response)

    def test_shoppinglist_edit_get_request(self):
        """Test edit get request"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # send a GET request
        res = self.app.get('/edit-list')
        self.assertEqual(res.status_code, 200)
        # check if page was loaded by looking for text in the page
        self.assertIn("Shopping List", str(res.data))

    def test_shoppinglist_editing(self):
        """Test is shoppinglist editing"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # make a post request with the edit name and original name
        res = self.app.post(
            '/edit-list', data={'list_name_org': 'Easter shopping', 'list_name': 'Easter'})
        self.assertEqual(res.status_code, 200)
        response = self.shopping_class_obj.edit_list(
            'Easter shopping', 'Easter', 'maina@gmail.com')
        self.assertIsInstance(response, list)
        # check if edit was successful by looking for the edited name
        self.assertIn("Easter", str(res.data))

    def test_shoppinglist_editing_with_error(self):
        """Test is shoppinglist editing with error e.g. special characters in edits"""
        # create a shopping list
        self.shopping_class_obj.create_list(
            'Christmass', 'maina@gmail.com')
        # send a post request to edit
        res = self.app.post(
            '/edit-list', data={'list_name_org': 'Christmass', 'list_name': 'Furniture!'})
        self.assertEqual(res.status_code, 200)
        # edit the shopping list
        response = self.shopping_class_obj.edit_list(
            'Furniture!', 'Christmass', 'maina@gmail.com')
        self.assertIn("No special characters", response)

    def test_shoppinglist_deletion(self):
        """Test is shoppinglist deletion"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # create a shopping list
        self.shopping_class_obj.create_list(
            'Christmass', 'maina@gmail.com')
        # make a post request with the delete name
        res = self.app.post(
            '/delete-list', data={'list_name': 'Christmass'})
        self.assertEqual(res.status_code, 200)
        self.shopping_class_obj.delete_list(
            'Christmass', 'maina@gmail.com')
        # check if delete was successful by looking for the deleted name
        self.assertIn("Christmass", str(res.data))

    def test_shoppingitems_page(self):
        """Test is shoppingitems page is accessible"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # send a GET request
        res = self.app.get('/shoppingitems/Easter')
        self.assertEqual(res.status_code, 200)
        self.assertIn("You can now add your items", str(res.data))

    def test_shoppingitems_creation(self):
        """Test is shoppingitems creation"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # create a shopping list
        self.shopping_class_obj.create_list(
            'Easter', 'maina@gmail.com')
        # make a post request to add an item
        res = self.app.post(
            '/shoppingitems/Easter', data={'item-name': 'Bread'})
        self.assertEqual(res.status_code, 200)
        response = self.item_class_obj.add_item(
            'Easter', 'Bread', 'maina@gmail.com')
        self.assertIsInstance(response, list)
        # check if item was successfully created
        self.assertIn("Bread", str(res.data))

    def test_shoppingitems_creation_with_error(self):
        """Test is shoppingitems creation with special characters raises an error"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # create a shopping list
        self.shopping_class_obj.create_list(
            'Easter', 'maina@gmail.com')
        # make a post request to add an item
        res = self.app.post(
            '/shoppingitems/Easter', data={'item-name': 'Bread-'})
        self.assertEqual(res.status_code, 200)
        response = self.item_class_obj.add_item(
            'Easter', 'Bread-', 'maina@gmail.com')
        # test response from shoppingitems class
        self.assertIn("No special characters", response)
        # check if item was successfully created
        self.assertIn("No special characters", str(res.data))

    def test_shoppingitems_editing(self):
        """Test is shoppingitems editing"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # create a shopping list
        self.shopping_class_obj.create_list(
            'Easter', 'maina@gmail.com')
        # make a post request with the edit name and original name
        res = self.app.post(
            '/edit-item',
            data={'item_name_org': 'Bread', 'item_name': 'Juice', 'list_name': 'Easter'})
        self.assertEqual(res.status_code, 200)
        response = self.item_class_obj.edit_item(
            'Juice', 'Bread', 'Easter', 'maina@gmail.com')
        # test response from shoppingitems class
        self.assertIsInstance(response, list)
        # check if edit was successful by looking for the edited name
        self.assertIn("Juice", str(res.data))

    def test_shoppingitem_deletion(self):
        """Test is shoppingitem deletion"""
        # register and login a user
        self.app.post('/register', data=self.user_reg_details)
        self.app.post('/login', data=self.user_login_details)
        # create a shopping list
        self.shopping_class_obj.create_list(
            'Christmass', 'maina@gmail.com')
        # create an item
        self.item_class_obj.add_item(
            'Christmass', 'Bread', 'maina@gmail.com')
        # make a post request with the delete name
        res = self.app.post(
            '/delete-item', data={'list_name': 'Christmass', 'item_name': 'Bread'})
        self.assertEqual(res.status_code, 200)
        self.item_class_obj.delete_item(
            'Bread', 'maina@gmail.com', 'Christmass')
        # check if delete was successful
        self.assertIn("Successfuly deleted item ", str(res.data))

    def test_logout(self):
        """"Test logging out feature"""
        res = self.app.get('/logout')
        self.assertEqual(res.status_code, 200)
        self.assertIn("Shoppinglist Application", str(res.data))

"""Test routes"""
import unittest
from app import app


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

    def tearDown(self):
        self.app = None
        self.user_reg_details = None
        self.user_login_details = None

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
        res = self.app.post('/shoppinglist')
        self.assertEqual(res.status_code, 200)
        res = self.app.get('/shoppinglist')
        self.assertEqual(res.status_code, 200)

    def test_shoppinglist_creation(self):
        """Test is shoppinglist creation is accessible"""
        res = self.app.post('/shoppinglist', data={'owner': 'maina@gmail.com', 'name': 'Easter'})
        self.assertEqual(res.status_code, 200)

    def test_shoppingitems_page(self):
        """Test is shoppingitems page is accessible"""
        res = self.app.post('/shoppingitems/1')
        self.assertEqual(res.status_code, 200)
        res = self.app.get('/shoppingitems/1')
        self.assertEqual(res.status_code, 200)

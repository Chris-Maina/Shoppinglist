""" test_useraccounts.py"""
import unittest
# import module useraccounts
from app.useraccounts import UserClass


class AccountTestCases(unittest.TestCase):
    """
    Test for duplicate accounts(user already exists)
    Test for short passwords
    Test for correct output/account creation
    Test login with no account
    Test login with wrong password
    Test login with existing email and password
    """

    def setUp(self):
        """Setting up UserClass before anything
        """
        self.user = UserClass()

    def tearDown(self):
        """Removing UserClass after everything
        """
        del self.user

    def test_case_pwd_equals_cpwd(self):
        """
        Args
            password =! confrim password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Chris", "mainachris@gmail.com", "chrismaina", "chrismainaw")
        self.assertEqual(msg, "Password mismatch")

    def test_case_existing_user(self):
        """
        Args
            registered user
        Returns
            error message
        """
        self.user.registeruser(
            "chris", "mainachris@gmail.com", "chrismaina", "chrismaina")
        msg = self.user.registeruser(
            "chris", "mainachris@gmail.com", "chrismaina", "chrismaina")
        self.assertIn("User already exists", msg)

    def test_case_short_pwd(self):
        """
        Args
            username
            email
            short password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Chris", "mainachris@gmail.com", "chris", "chris")
        self.assertEqual(
            msg, "Your password should be at least 6 characters long")

    def test_case_special_char(self):
        """
        Args
            username(string):name of user
            email(string):user email
            password(string):user password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Chris maina", "mainachris@gmail.com", "chrismaina", "chrismaina")
        self.assertIn("No special characters ", msg)

    def test_case_invalid_email(self):
        """
        Args
            username(string):name of user
            email(string):user email
            password(string):user password
        Returns
            error message
        """
        msg = self.user.registeruser(
            "Chris", "mainachris@gmail", "chrismaina", "chrismaina")
        self.assertEqual(msg, "Please provide a valid email address")

    def test_case_correct_input(self):
        """
        Args
            username(string):name of user
            email(string):user email
            password(string):user password
        Returns
            success message
        """
        msg = self.user.registeruser(
            "Chris", "mainachris@gmail.com", "chrismaina", "chrismaina")
        self.assertIn("Successfully registered", msg)

    def test_case_login_noaccount(self):
        """
        Args
            non existent email and password
        Returns
            error message
        """
        self.user.user_list = [
            {'username': 'chris', 'password': 'chrismaina', 'email': 'mainachrisw@gmail.com'}]
        msg = self.user.login("njekama@gmail.com", "chrismaina")
        self.assertEqual(msg, "You have no account,please sign up")

    def test_case_login_wrong_password(self):
        """
        Args
            existent email and wrong password
        Returns
            error message
        """
        self.user.user_list = [
            {'username': 'chris', 'password': 'chrismaina', 'email': 'mainachrisw@gmail.com'}]
        msg = self.user.login("mainachrisw@gmail.com", "mainachris")
        self.assertEqual(msg, "Password mismatch")

    def test_case_correct_login(self):
        """
        Args
            existent email and password
        Returns
            success message
        """
        self.user.user_list = [
            {'username': 'chris', 'password': 'chrismaina', 'email': 'mainachrisw@gmail.com'}]
        msg = self.user.login("mainachrisw@gmail.com", "chrismaina")
        self.assertIn("create shoppinglist!", msg)


if __name__ == '__main__':
    unittest.main()

""" useraccounts.py """


class UserClass(object):
    """
    Class to handle registration and loggin of users
    """

    def __init__(self):
        # list to contain users
        self.user_list = []

    def registeruser(self, username, email, password, cpassword):
        """
        Args
            username(string):name
            email(string):user email
            upasswd(string):password
        Return
           error msg or success msg
        Purpose
           register users that have signed up by adding to dictionary
        """
        # empty dict to hold each user
        user_dict = {}
        # check for existing user
        for user in self.user_list:
            if email == user['email']:
                return "User already exists. Please login"
        else:
            # check for password length and mismatch
            if len(password) < 6:
                return "Your password should be at least 6 characters long"
            elif password == cpassword:
                user_dict['username'] = username
                user_dict['email'] = email
                user_dict['password'] = password
                self.user_list.append(user_dict)
            else:
                return "Password mismatch"
        return "Successfully registered. You can now login!"

    def login(self, email, password):
        """
        Args
            email(string):user email
            userpassword(string):password
        Return
           error msg or success msg
        Purpose
           Login users
        """
        for user in self.user_list:
            if email == user['email']:
                if password == user['password']:
                    return "Successfully logged in, create buckets!"
                else:
                    return "Password mismatch"
        return "You have no account,please sign up"

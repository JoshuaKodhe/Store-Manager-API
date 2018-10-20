"""User class"""


class User:
    """User class defining methods related to the class"""
    users_list = []

    def __init__(self, username, password):
        self.user_id = len(self.users_list)+1
        self.username = username
        self.password = password

    def save_user(self):
        """ save a new user """
        pass

    def single_user(self, username):
        """ Method to get a user"""
        pass

import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
   
    def setUp(self):
        """
        a method that runs before the test

        """
        self.new_user= User("kennedy","kentoz8410")

    def __init__(self):
        self.assertEqual(self.new_user.user_name,"kennedy")
        self.assertEqual(self.new_user.user_password,"kentoz8")
    
    def test_save_user(self):
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()
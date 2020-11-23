import unittest
from user import User
from user import Credentials

class TestClass(unittest.TestCase):

    def test_init(self):
        self.assertEqual(self.new_user.user_name,"kennedy")
        self.assertEqual(self.new_user.user_password,"1234")

    def setUp(self):

        self.new_user = User("kennedy","1234")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len( User.user_list),1)

class TestCredentials(unittest.TestCase):
    
    def setUp(self):

        self.new_credentials = Credentials("account","kennedy","1234")
    
    def tearDown(self):
        Credentials.user_credentials = []

    def test_details(self):
        self.assertEqual(self.new_credentials.account,"account")
        self.assertEqual(self.new_credentials.user_name,"kennedy")
        self.assertEqual(self.new_credentials.user_password,"1234")

   
    def test_exist(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("account","user_name","user_password")
        test_credential.save_credentials()

        search_credential = Credentials.credential_user_exist("account")
        self.assertTrue(search_credential)

    def delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("account","user_name","user_password")
        test_credential.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials),1)

if __name__ == "__main__" :
        unittest.main()
    


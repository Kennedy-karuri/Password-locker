import random
import string



class User:
    """
    Class that generates new instances of users
    """
    user_list = [] # Empty user list

    def __init__(self,user_name,user_password,):

        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        """
        save_user method saves a new user object to user list
       
        """
        
        User.user_list.append(self)

  
    @classmethod   
    def my_user(cls,user_name,user_password):
        current_user = ''
        for user in User.user_list:
            if user.user_name == user_name and user.user_password == user_password:
                current_user = user.user_name
        return current_user



class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,account,user_name,user_password):

        '''
        __init__ method that helps us define properties for our objects.
        '''
        self.account = account
        self.user_name = user_name
        self.user_password = user_password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.append(self)

    @classmethod
    def credential_user_exist(cls,account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def find_account(cls,account):
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
    
    @classmethod
    def show_credentials(cls):
        return cls.credentials_list

    def generate_password (self,string_len = 5):
                        password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "(|/~!.@,)#{?&[%]^}&*"
                        return ''.join(random.choice(password) for i in range(string_len))


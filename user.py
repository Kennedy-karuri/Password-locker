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

    def __init__(self,c_name,c_password,):

        '''
        __init__ method that helps us define properties for our objects.
        '''

        self.c_name = c_name
        self.c_password = c_password

    @classmethod
    def verify_user(cls,user_name,password):
        entered_default = ""
        for user in User.user_list:
            if(user.user_name == user_name and user.password == password):
                entered_default == user.user_name
        return entered_default

    def save_user_credentials(self):
        """
        save_user_credentials method saves a new user object to credentials list

        """

        Credentials.credentials_list.append(self)     

    def delete_credentials(self):
            """
            delete_credentials method deletes a saved credential from the credentials_list

            """   

            Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_number(cls,user_name): 
        """
        Method that takes in a password and returns a password that matches the password.

        """  
        for credentials in cls.credentials_list:
            if (credentials.c_username == user_name):
                return credentials
    

    @classmethod
    def credentials_exist(cls,user_name):
        """
        Method that checks if a credential exists from the user details list.
        Args:
        number: Phone number to search if the user details exists
        Returns :
        Boolean : True or false depending on the user details existance

        """
        for credentials in cls.credentials_list:
            if credentials.c_username == user_name:
                return True
                  
        return False

    def generate_password(self):
        """
        generate a random password consisting of letters

        """

        password = string.ascii_lowercase + string.ascii_uppercase + "havertz"
        return''.join(random.choice(password)for i in range(1,9))
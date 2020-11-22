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

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod   
    def display_user(cls):
        return cls.user_list



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


from user import Credentials
from user import User

def createUser (user_name,user_password):
    New_user = User(user_name,user_password)
    return New_user

def log_in (user_name,user_password):
    my_user = User.my_user(user_name,user_password)
    return my_user

def save_user(User):
    User.save_user()

def create_credentials(account,user_name,user_password):
    New_credentials = Credentials(account,user_name,user_password)
    return New_credentials

def save_credentials(credentials):
    credentials.save_credeentials(credentials)

def delete_credentials(credentials):
    return credentials.delete_credentials()


def show_credentials():
    return Credentials.show_credentials()

def credential_user_exist(account):
    return Credentials.credential_user_exist(account)

def find_account(account):
    return Credentials.find_account(account)

def generate_password ():
    generate_password = Credentials.generate_password()
    return generate_password

def main():
    while True:
        print('Welcome to Password-locker. To create account us cr,lg to login and ex to exit')
        userinput = input().lower()

        if userinput == "cr":
            print("Please enter your account details")
            user_name = input("Type in your username:")

            print("use E to enter password, use Gen to generate password, and X to exit")
            user_password = input().lower()
            if user_password == "e":
                user_password = input("Tpye your password:")
            elif user_password == "g" :
                user_password = generate_password()
            else :
                print("Try again")

            save_user(createUser(user_name,user_password))
            print(f" Password-Locker welcome's {user_name} and your password is {user_password} ")

        elif userinput == "lg":
            print("Type in username and password to login")
            print("enter your username:")
            user_name = input()
            print("enter your password")
            user_password = input()
            my_user = log_in (user_name,user_password)
            if my_user == user_name:
                print(f"Hey {user_name}")
                while True:
                    print("use CR to create credentials, D to delete credential , DIS to display credentials, F to find credentials, X to exit")
                    credentials_selection = input().lower

                    if credentials_selection == "cr":
                        print("create credentials")
                        input("enter account name:")
                        account = input()
                        print("enter username:")
                        user_name = input()
                        print("use E to enter password , use Gen to generate password , and X to exit")
                        user_password = input().lower()
                        if user_password == "e":
                            user_password = input("enter password:")
                        elif user_password == "gen":
                             user_password = generate_password()
                        else:
                            print("Try Again")

                        save_credentials(create_credentials(account,user_name,user_password))
                        print(f"Your credentials are {account} , {user_name} , {user_password} has been succesfully created.")

                    elif credentials_selection == "d":
                        print("enter account to delete")
                        account = input()
                        if find_account(account):
                            account_delete = find_account(account)
                            account_delete.delete_credentials()
                            print("account sucssesfully deleted")

                        else:
                            print("Credentials does not exist.")

                    elif credentials_selection == "dis":
                        print("Your credentials are:")
                        if show_credentials():
                                for account in show_credentials():
                                    print(f"account: {account} \n username: {user_name} \n password: {user_password} \n")
                        else:
                            print("no credentials found")

                    elif credentials_selection == "f":
                        print("enter account to be found:")
                        account = input("enter account name:")
                        if find_account(account):
                                account_name = find_account(account)
                                print(f"account: {account_name.account} \n username: {account_name.user_name} \n password: {account_name.user_password} \n") 

                        else:
                            print("Goodbye")


    else:
        print("Thank you for your time.") 


        
if __name__ == "__main__":
    main()
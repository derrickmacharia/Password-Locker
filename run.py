from user import User
from credentials import Credentials

def create_user(first_name, last_name, username, password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name, last_name, username, password)
    return new_user

def save_user(user):
    '''
    Function to save contact
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a contact
    '''
    user.delete_user()

def find_user(first_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_username(first_name)

def check_existing_user(first_name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exists(first_name)

def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()



def create_new_credential(account_site, account_username, account_password):
    '''
    function to create a new account
    '''
    new_credential = Credentials(account_site, account_username, account_password)
    return new_credential


def save_social_credentials(credentials):  # save credentials
    '''
    function to save credentials
    '''
    credentials.save_credentials()


def display_social_credentials():  # display credentials
    """
    funtion to display credentials
    """
    return Credentials.display_credentials()


def delete_social_credential(credentials):  # delete credential
    '''
    function to delete credentials
    '''
    credentials.delete_credentials()


def find_credential(credentials):  # find a credential
    '''
    find credentials to delete
    '''
    credentials.find_by_account_site()


def generate_password(password_length):  # generate password
    """
    generate a random password for the user
    """
    return Credentials.generate_password(password_length)

def main():
    print("Hello Welcome to your contact list. What is your name?")
    uname = input()

    print(f"Hello {uname}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new user, lg - login into your account, dc - display user, fc -find user, ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New User")
                            print("-"*30)

                            print ("First name ....")
                            first_name = input()

                            print("Last name ...")
                            last_name = input()

                            print("Username ...")
                            username = input()

                            print("Password ...")
                            password = input()

                            save_user(create_user(first_name, last_name, username, password)) # create and save new user.
                            print ('\n')
                            print(f"New User {first_name} {last_name} created")
                            print ('\n')

                            print('You can now log in using the username and password created')

                            print('Username...')
                            login_username = input()

                            print('Password...')
                            login_password = input()

                            if username != login_username or password != login_password:
                                print('Invalid Username or password!')
                                print('Please enter your password....')
                                login_username = input()

                                print('Please enter your password...')
                                login_password = input()

                            else :
                                print ('\n')
                                print(f'Hello {login_username}. Welcome to your password locker account!')
                                print ('\n')

                                socialmedia()
    
                    elif short_code == 'lg':
             
                        print('Log in to your existing account')
                        print('Username....')
                        lg_username = input()

                        print('Password....')
                        lg_password = input()

                        if lg_username != 'username' and lg_password != 'derrick123':
                            print('The account does not exist, please create an account')
                        else:
                            print(f'Hello {lg_username}. This is your password locker account, Welcome!')
                            print ('\n')

                            socialmedia()

                    elif short_code == 'dc':

                            if display_users():
                                    print("Here is a list of all your user")
                                    print('\n')

                                    for contact in display_users():
                                            print(f"{contact.first_name} {contact.last_name} .....{contact.username}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any user saved yet")
                                    print('\n')

                                    socialmedia()

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_username = input()
                            if check_existing_user(search_username):
                                    search_username = find_user(search_username)
                                    print(f"{search_username.first_name} {search_username.last_name}")
                                    print('-' * 20)

                                    print(f"Usename.......{search_username.username}")
                                    print(f"Password.......{search_username.password}")
                            else:
                                    print("That contact does not exist")

                                    socialmedia()

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")

def  socialmedia():
    print("Hello You can store your social account here")

    print("Use this code to navigate through")
    print('\n')
    while True:
            print('ana - Add a new social account credentials')
            print('exs - Add an existing social account credentials')
            print('dis - Display your available social accounts credentials')
            print('del - Delete a saved account credentials')
            print('ex - Exit from the account')
            
            user_code = input().lower()

            if user_code == 'ana':
                print('Add a new social account credentials')
                print("-"*20)

                print('What is your new Social Account Name? ...')
                account_site = input()

                print('What is your username in the Social Account Name...')
                account_username= input()
                
                print ('\n')
                print('Use:')
                print('gp - To get the password generated for you')
                print('cp - To create your own password')

                short_code2 = input().lower()
                if short_code2 == 'gp':
                    print(
                        "Enter length of your desired password?")
                    password_length = int(input())
                    account_password = generate_password(
                        password_length)
                    print(
                        f"Your generated password is {account_password}")
                elif short_code2 == 'cp':
                    print('Input your password....')
                    password = input()
                else:
                    print('Invalid short code')     
                save_social_credentials(create_new_credential(account_site, account_username, account_password))
                   
                print(f'{account_site} account credentials have been saved and stored')

if __name__ == '__main__':
    main()
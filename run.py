from user import User
from credentials import Credentials

def create_user(fname,lname,email):
    '''
    Function to create a new user
    '''
    new_user = User(fname,lname,email)
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
    return User.find_by_first_name(first_name)

def check_existing_user(first_name):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(first_name)

def display_users():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_users()


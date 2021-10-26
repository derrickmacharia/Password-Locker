import random
import string

class Credentials():

    user_credentials = []

    def __init__(self, account_platform, account_username, account_password):

        self.account_platform = account_platform
        self.account_username =  account_username
        self.account_password =  account_password

    def save_credentials(self):
        '''
        save credentials into user_credentials
        '''
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        '''
        delete save credentials
        '''
        Credentials.user_credentials.remove(self)
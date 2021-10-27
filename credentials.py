import random
import string

class Credentials():

    user_credentials = []

    def __init__(self, account_site, account_username, account_password):

        self.account_site = account_site
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

    @classmethod
    def find_by_account_site(cls, account_site):
        '''
        method that takes in a account_site and returns credentials
        '''
        for credentials in cls.user_credentials:
            if credentials.account_site == account_site:
                return credentials
        return False

    @classmethod
    def display_credentials(cls):
        '''
        return credentials list
        '''
        return cls.user_credentials

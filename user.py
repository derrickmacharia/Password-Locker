# import pyperclip

class User:

    """
    Class that generates new users
    """

    user_list = [] # Empty user list   

    def __init__(self, first_name, last_name, username, password):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save_user(self):

        '''
        save_uer method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        for user in cls.user_list:
            if user.username == username:
                return user




    @classmethod
    def user_exists(cls, username):
        for user in cls.user_list:
            if user.username == username:
                return True
        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list


    # @classmethod
    # def copy_email(cls,first_name):
    #     contact_found = User.find_by_first_name(first_name)
    #     pyperclip.copy(contact_found.email)
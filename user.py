class User:

    """
    Class that generates new users
    """

    user_list = [] # Empty user list   

    def __init__(self, first_name, last_name, email):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email

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
    def find_by_first_name(cls, first_name):
        for user in cls.user_list:
            if user.first_name == first_name:
                return user

    @classmethod
    def user_exists(cls, first_name):
        for user in cls.user_exists:
            return True
        return False

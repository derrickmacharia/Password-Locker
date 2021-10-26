class User:

    """
    Class that generates new users
    """

    userlist = [] # Empty user list   

    def __init__(self, first_name, last_name, email):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
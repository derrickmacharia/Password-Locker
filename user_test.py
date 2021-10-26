import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''

    Test class that defines test cases for the user class behaviours

    Args:
        unittest.TestCase class that helps in creating test cases

    '''
    def setUp(self):

        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Der","Rick","derrick@gm.com") #create user object

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Der")
        self.assertEqual(self.new_user.last_name,"Rick")
        self.assertEqual(self.new_user.email,"derrick@gm.com")

    def test_save(self):
        '''
        test_save test case to test if the user object is saved into
         the user_list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_multiple_user(self):

        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''

        self.new_user.save_user()
        another_user = User("User","name","username@gm.com")
        another_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.new_user.save_user()
        another_user = User("User","name","username@gm.com")
        another_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
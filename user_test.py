import unittest # Importing the unittest module
from user import User # Importing the user class
# import pyperclip

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
        self.new_user = User("Der","Rick", "username", "derrick@gm.com") #create user object

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
        self.assertEqual(self.new_user.username,"Rick")
        self.assertEqual(self.new_user.password,"derrick@gm.com")

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
        another_user = User("user","name","username", "username@gm.com")
        another_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        self.new_user.save_user()
        another_user = User("user","name","username", "username@gm.com")
        another_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)

    def test_find_by_username(self):
        self.new_user.save_user()
        another_user = User("user","name","username", "username@gm.com")
        another_user.save_user()

        found_user = User.find_by_username("username")

        self.assertEqual(found_user.password, another_user.password)

    def test_user_exists(self):
        self.new_user.save_user()
        another_user = User("user","name","username" ,"username@gm.com")
        another_user.save_user()

        user_exists = User.user_exists("user")

        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_list)

    # def test_copy_first_name(self):
    #     '''
    #     Test to confirm that we are copying the email address from a found contact
    #     '''

    #     self.new_user.save_user()
    #     User.copy_first_name("user")

    #     self.assertEqual(self.new_user.email,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
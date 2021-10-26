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

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Der")
        self.assertEqual(self.new_user.last_name,"Rick")
        self.assertEqual(self.new_user.email,"derrick@gm.com")


if __name__ == '__main__':
    unittest.main()
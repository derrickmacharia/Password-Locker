import unittest
from credentials import Credentials 

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Setup for the test
        """
        self.new_credentials = Credentials("Twitter","tweetUser", "pass123")

    def test_init(self):
        """
            test to check credentials object is created
        """
        self.assertEqual(self.new_credentials.account_platform, "Twitter")
        self.assertEqual(self.new_credentials.account_username, "tweetUser")
        self.assertEqual(self.new_credentials.account_password, "pass123")
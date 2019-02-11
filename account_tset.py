import unittest # Importing the unittest module
from account import Account # Importing the Account class

class TestAccount(unittest.TestCase):

    '''
    Test class that defines test cases for the Account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''    # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_account = Account("Github","omukankurunziza","rukundo11") # create account object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Github")
        self.assertEqual(self.new_account.user_name,"omukankurunziza")
        self.assertEqual(self.new_account.password,"rukundo11")
       


if __name__ == '__main__':
    unittest.main()
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

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account() # saving the new account
        self.assertEqual(len(Account.account_list),1)

    # Items up here...

    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("yahoo.fr","nshutioppo@yahoo.fr","rukundo") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)

    #setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Account.account_list = []

# other test cases here
    def test_save_multiple_account(self):
            '''
            test_save_multiple_account to check if we can save multiple account
            objects to our account_list
            '''
            self.new_account.save_account()
            test_account = Account("yahoo.fr","nshutioppo@yahoo.fr","rukundo") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)
    # More tests above
    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("yahoo.fr","nshutioppo@yahoo.fr","rukundo") # new contact
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(Account.account_list),1)

       


if __name__ == '__main__':
    unittest.main()
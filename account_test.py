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
        self.new_account = Account("Mukankurunziza","omukankurunziza","rukundo11") # create account object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name,"Mukankurunziza")
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
            test_account = Account("Mukankurunziza","nshutioppo@yahoo.fr","rukundo") # new account
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
            test_account = Account("Mukankurunziza","nshutioppo@yahoo.fr","rukundo") # new account
            test_account.save_account()
            self.assertEqual(len(Account.account_list),2)
    # More tests above
    def test_delete_account(self):
            '''
            test_delete_account to test if we can remove a account from our account list
            '''
            self.new_account.save_account()
            test_account = Account("Mukankurunziza","nshutioppo@yahoo.fr","rukundo") # new contact
            test_account.save_account()

            self.new_account.delete_account()# Deleting a account object
            self.assertEqual(len(Account.account_list),1)


    def test_find_account_by_account_name(self):
        '''
        test to check if we can find a account by account_name  and display information
        '''

        self.new_account.save_account()
        test_account = Account("Mukankurunziza","nshutioppo@yahoo.fr","rukundo") # new account
        test_account.save_account()

        found_account = Account.find_by_account_name("Mukankurunziza")

        self.assertEqual(found_account.user_name,test_account.user_name)

    @classmethod
    def find_by_account_name(cls,account_name):
        '''
        Method that takes in a account_name  and returns a account that matches that account_name.

        Args:
            account_name: account_name to search for
        Returns :
            account of person that matches the account_name.
        '''

        for account in cls.account_list:
            if account.account_name == account_name:
                return account
    
    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account() # new contact
        test_account.save_account("Mukankurunziza","nshutioppo@yahoo.fr","rukundo")

        account_exists = Account.account_exist("Mukankurunziza")

        self.assertTrue(account_exists)

    @classmethod
    def account_exist(cls,account_name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            account_name: account_name to search for
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.account_name == account_name:
                    return True

        return False

       


if __name__ == '__main__':
    unittest.main()
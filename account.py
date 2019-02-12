class Account:
    """
    Class that generates new instances of users.
    """

    account_list = [] # Empty account list

    def __init__(self,account_name,user_name,password):

      # docstring removed for simplicity

        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    # Init method up here
    def save_account(self):

        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)
    # delete account
    def delete_account(self):

        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list

    def create_account(account_name,user_name,password):
        '''
        Function to create a new account
        '''
        new_account = Account(account_name,user_name,password)
        return new_account

    def save_accounts(account):
        '''
        Function to save account
        '''
        account.save_account()

    def del_ account( account):
        '''
        Function to delete a  account
        '''
         account.delete_ account()

    def find_account(account_name):
        '''
        Function that finds a account by account_name and returns the account
        '''
        return Account.find_by_account_name(account_name)

    def check_existing_accounts(account_name):
        '''
        Function that check if a account exists with that account_name and return a Boolean
        '''
        return Account.account_exist(account_name)

    def display_accounts():
        '''
        Function that returns all the saved accounts
        '''
        return Account.display_accounts()
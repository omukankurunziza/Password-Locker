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

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
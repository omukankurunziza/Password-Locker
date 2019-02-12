class Credentials:

    """
    Class that generates new instances of users.
    """
    credentials_list = [] #empty credentials list


    def __init__(self,credentials_name,usr_name,password):
        self.credentials_name = credentials_name
        self.usr_name = usr_name
        self.password = password
      

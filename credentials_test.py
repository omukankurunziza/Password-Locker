
import unittest # Importing the unittest module

from credentials import Credentials # Importing the credentials class




class TestCredentials(unittest.TestCase):
    def setUp(self):
       
        self.new_credentials = Credentials("Mukankurunziza","nshutioppo@yahoo.fr","rukundo") # create credentials object


    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''


        self.assertEqual(self.new_credentials.credentials_name,"Mukankurunziza")
        self.assertEqual(self.new_credentials.usr_name,"nshutioppo@yahoo.fr")
        self.assertEqual(self.new_credentials.password,"rukundo")

    
    def test_save_credentials(self):
        '''
        test_save credentials test case to test if thecredentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)  


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []  

    
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Mukankurunziza","nshutioppo@yahoo.fr","rukundo") # new credential
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove an credential from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Mukankurunziza","nshutioppo@yahoo.fr","rukundo") # credential
            test_credentials.save_credentials()


            self.new_credentials.delete_credentials()# Deleting an credential object
            self.assertEqual(len(Credentials.credentials_list),1) 








if __name__ == '__main__':
    unittest.main()
        



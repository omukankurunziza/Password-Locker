
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

if __name__ == '__main__':
    unittest.main()
        



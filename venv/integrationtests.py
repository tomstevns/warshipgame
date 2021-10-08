import unittest

from CLass_Offline import Offline
from Class_Online import Online
from Class_Client_Server_Login import Client_Server_Login
from Class_Start import Start
from Class_Skibe import Skibe
from Class_Spil import Spil





class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_integrationsTest_af_Offline_Start(self):
        offLineSpiller = Offline()
        self.assertTrue(offLineSpiller.spilModComputer())


    def test_integrationsTest_af_Online_Start(self):
        onLineSpiller = Online()
        self.assertTrue(onLineSpiller.spilModSpiller())

    def test_integrationsTest_af_Class_Client_Server_Login(self):
        client = Client_Server_Login()
        #To be implemented
        self.assertTrue(False)

    def test_integrationsTest_af_Class_Skibe(self):
        skibe = Skibe()
        #To be implemented
        self.assertTrue(False)
    
    def test_integrationsTest_af_Class_Spil(self):
        spil = Spil()
        #To be implemented
        self.assertTrue(False)



if __name__ == '__main__':
    unittest.main()

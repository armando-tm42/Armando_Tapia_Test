import unittest
#import sys
#sys.path.append('../')
from to_numeric_lib import Deci, Inte


class TestToNumericalMethods(unittest.TestCase):
 
    def setUp(self):
        pass

    '''
    If  a string doesn't have any numbers, to_float and to_int should return a ValueError.
    '''

    def testtofloat(self):
        self.assertRaises(ValueError,Deci('asdasdsasdasd').to_float)
    
    '''
    If there is at least one number in the string to_int should return an int object and
    to_float could return both int or float objects
    '''
    def testtoint(self):
        self.assertIsInstance(Deci('1asdasdsa').to_float(),int)
    
    '''
    Comp function must receive only as argument objects with the same type of the instance 
    that calls the method
    '''
    def testcomp(self):
        with self.assertRaises(TypeError):
            Inte('123131asds').comp(Deci('1.23sad'))
    '''
    if compS, CompS and CompI receive objects different to those they were designed to 
    handle, all of them should return a Type Error
    '''
    def testcompS(self):
        with self.assertRaises(TypeError):
            Inte('123131asds').comps(Inte('11231sad'))
    
    '''
    when to_int receive a string with float format it going to ignore
    the dot and threat the float as a whole number
    '''

    def testtointfloat(self):
        self.assertEqual(Inte('1.3434').to_int(),13434)

if __name__ == '__main__':
    unittest.main()
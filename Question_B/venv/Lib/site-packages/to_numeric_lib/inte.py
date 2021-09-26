import regex as re
from .Number import Number

class Inte(Number):
    def __init__(self,string):
        Number.__init__(self,string)
        self.clean = re.sub('[^0-9$]','',self.string)
        if self.sign == -1:
            self.clean = '-' + self.clean
        
    def to_int(self):

        '''
        converts any string that has a number in a int object

        Raises
        ------
        ValueError
            if no number is found in the string 

        '''

        if self.clean != '':
            num = 0
            n = self.clean
            if self.sign == -1:
                n = self.clean[1:] 
            for i in n:
                num = num*10+ord(i) - ord('0')
                num = num
            return num*self.sign
        else:
            raise ValueError("Could not convert string to an integer.")

    
    def comp(self,Num):

        '''

        compare two Inte objects and return wheter is the object that calls 
        method is less, greater or equal to other

        Parameters
        ----------
        Num: Inte, required
            The Inte object to compare with 

        Raises
        ------
        TypeError
            if no number or invalid object is passed to compare

        '''

        if isinstance(Num,Inte) is  not True:
            raise TypeError('Not an Inte object')
        else:
            n = self.to_int() - Num.to_int()
            if n < 0 : 
                print(self.clean, ' is less than ',Num.clean)
            elif n > 0:
                print(self.clean, ' is greater than ',Num.clean)
            elif n == 0:
                print(self.clean, ' is equal to ',Num.clean)
            
    def comps(self,string):

        '''
        compare an Inte object to any string with at least one number

        Parameters
        ----------
        string: str, required
            the string to compare with
        
        Raises
        ------
        TypeError
            if no string or invalid object is passed to compare
        
        ValueError
            if no number is found in the string

        '''

        if isinstance(string,str) is not True:
            raise TypeError("Not a str object")
        else:
            n =self.to_int() - Inte(string).to_int()
            if n < 0 : 
                print(self.clean, ' is less than ',Inte(string).clean)
            elif n > 0:
                print(self.clean, ' is greater than ',Inte(string).clean)
            elif n == 0:
                print(self.clean, ' is equal to ',Inte(string).clean)
    
    def compD(self,Num):

        '''
        Compare an Inte to a Deci object and return wheter is the object that calls 
        method is less, greater or equal to the Deci object

        Parameters
        ----------
        Nun: Deci, required

        TypeError
            if no Deci or invalid object is passed to compare

        ValueError
            if the Deci object dosen't have any number

        '''

        from deci import Deci
        if isinstance(Num,Deci) is not True:
            raise TypeError("Not a Deci object")
        else:
            n =self.to_int() - Num.to_float()
            if n < 0 : 
                print(self.clean, ' is less than ',Num.clean)
            elif n > 0:
                print(self.clean, ' is greater than ',Num.clean)
            elif n == 0:
                print(self.clean, ' is equal to ',Num.clean)
import regex as re
from .Number import Number
from .inte import Inte

class Deci(Number):
    def __init__(self,string):
        Number.__init__(self,string)
        pattern_1 = re.compile("\.")
        dot = pattern_1.search(self.string)
        if dot != None:
                self.number_part = re.sub(r'[^-0-9.$]','',self.string[:dot.span()[1]])
                self.fractional_part = re.sub(r'[^0-9$]','',self.string[dot.span()[1]:])
                self.clean = self.number_part + self.fractional_part
        else:
            self.clean = Inte(self.string).clean
    
    def to_float(self):
        '''
        convert any string that has a number in a float or an int objects
        depending if it finds a dot in the string or not

        Raises
        ------
        ValueError
            if no number is found in the string 

        '''
        if self.clean != '':
            if re.search("\.",self.string) == None:
                return Inte(self.string).to_int()
            else:
                num=0.0
                for i in range(1,len(self.fractional_part)+1,1):
                    num = num + ((ord(self.fractional_part[i-1]) - ord('0'))/(10**i))
            return Inte(self.number_part).to_int()+(num*self.sign)
        else:
            raise ValueError("Could not convert string to float.")
    
    def comp(self,Num):
        '''
        compare two Deci objects and return wheter is the object that calls 
        method is less, greater or equal to other

        Parameters
        ----------
        Num: Deci, required
            The Deci object to compare with 

        Raises
        ------
        TypeError
            if no number or invalid object is passed to compare

        '''
        if isinstance(Num,Deci) is not True:
            raise TypeError("Not a Deci object")
        else:
            n = self.to_float() - Num.to_float()
            if n < 0 : 
                print(self.clean, ' is less than ',Num.clean)
            elif n > 0:
                print(self.clean, ' is greater than ',Num.clean)
            elif n == 0:
                print(self.clean, ' is equal to ',Num.clean)
            
    def comps(self,string):

        '''
        compare a Deci object to any string with at least one number

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
            n = self.to_float() - Deci(string).to_float()
            if n < 0 : 
                print(self.clean, ' is less than ',Deci(string).clean)
            elif n > 0:
                print(self.clean, ' is greater than ',Deci(string).clean)
            elif n == 0:
                print(self.clean, ' is equal to ',Deci(string).clean)
    
    def compI(self,Num):

        '''
        Compare a Deci to a Inte object and return wheter is the object that calls 
        method is less, greater or equal to the Intr object

        Parameters
        ----------
        Nun: Inte, required

        TypeError
            if no Inte or invalid object is passed to compare

        ValueError
            if the Inte object dosen't have any number

        '''

        if isinstance(Num,Inte) is not True:
            raise TypeError("Not an Inte object")
        else:
            n = self.to_float() - Num.to_int()
            if n < 0 :
                print(self.clean, ' is less than ',Num.clean)
            if n > 0 :
                print(self.clean, ' is greater than ', Num.clean)
            if n == 0:
                print(self.clean, ' is equal too ', Num.clean)
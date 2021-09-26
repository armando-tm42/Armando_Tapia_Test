import sys
sys.path.append(".")
class Number(object):
    def __init__(self,string):
        self.string = string
        if bool(self.string) is  not False:
            if self.string[0] == '-':
                self.sign = -1
            else:
                self.sign = 1
        else:
            raise TypeError('No characters in string')
    def __str__(self):
        return self.string
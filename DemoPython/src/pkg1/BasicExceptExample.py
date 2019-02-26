'''
Created on Feb 15, 2019

@author: sipika
'''
from builtins import ZeroDivisionError, ArithmeticError
list = [1,2,3,4]

try:
    print(list[2]/9)
except ArithmeticError:
    print("Arithmetic Error")
except ZeroDivisionError:
    print("Zero Division Error")
except NameError:
    print("Name Error")
else:
    print("Error not in list")   
def show():
    print("rest code is running properly")
    
show()
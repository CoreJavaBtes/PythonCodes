'''
Created on Feb 12, 2019

@author: sipika
'''
from Inheritance import Polygon

class MyClass(Polygon.MyClass):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def area(self):
        s = self.a+self.b+self.c/2
        print("Area = ",s)
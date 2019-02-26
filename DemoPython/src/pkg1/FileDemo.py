'''
Created on Feb 6, 2019

@author: sipika
'''
"""obj=open("abcd.txt","w")  
obj.write("Hi, How are You..!! Welcome to the world of Python \n")  
obj.close() """
value = input("Enter to Print")
obj1=open("abcd.txt","r+")  
s=obj1.read()  
s = str(s)
s1 = value.upper()

s1="\n"+s1
obj1.write(s1)
print(s1)  
obj1.close()
"""obj=open("abcd.txt","a")  
obj.write(s1)  
obj.close() """

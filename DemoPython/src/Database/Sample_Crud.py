'''
Created on Feb 20, 2019

@author: sipika
'''
import sqlite3
db = sqlite3.connect("MyDataBase")
print(db)
#CRUD Operations 
cur = db.cursor()
print(cur)
#Create Table
 
cur.execute("Create table if not exists tb_First(id INTEGER PRIMARY KEY, name TEXT, pass Text)")
db.commit()
# Insert Query

id = int(input("Enter your Id"))
name = input("Enter your name")
password = input("Enter your Pass")

i = cur.execute("Insert into tb_First(id, name,pass) VALUES(?,?,?)",(id,name,password))
db.commit()
if i:
 print("Successfull")
else:
 print("Try Again") 


cur.execute("Select * from tb_First ")
for i in cur:
    
    print ('{0}, {1}, {2}'.format(i[0],i[1],i[2]))
    
db.commit()
'''
Created on Feb 20, 2019

@author: sipika
'''
import webbrowser

message = """<html>
                <body>
                <h1><Hi, Welcome User></h1>
                <div>
                    <form>
                        Enter Number <input type="password"  name = "passs"/>
                    </form>
                </div>
                </body>
            </html>"""
obj=open("abcd.html","w")  

obj.write(message)  

obj.close()
webbrowser.open_new_tab('abcd.html')

obj = open("abcd.html","r")
s=obj.read()
print(s)
obj.close()

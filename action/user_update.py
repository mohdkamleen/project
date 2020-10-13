#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\r\n\r\n")

import cgi,cgitb
result=cgi.FieldStorage()

id = result.getvalue("user_id")  
name = result.getvalue("user_name")  
email = result.getvalue("user_email")  
password = result.getvalue("user_password")  

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kamleen"
)
mycursor=mydb.cursor()

up="update signin set name='%s', email='%s', password='%s' where id=%s"%(name,email,password,id)
mycursor.execute(up)
mydb.commit()
print("<script>window.location.href='user.py#user';</script>")
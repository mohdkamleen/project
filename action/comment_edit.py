#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\r\n\r\n")

import cgi,cgitb
result=cgi.FieldStorage()

id = result.getvalue("comment_id") 
user = result.getvalue("user") 
comm = result.getvalue("edit_comment")
date = result.getvalue("date_comment")

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kamleen"
)
mycursor=mydb.cursor()

up="update comments set user='%s', comment='%s', date='%s' where id=%s"%(user,comm,date,id)
mycursor.execute(up)
mydb.commit()
print("<script>window.location.href='user.py#comment';</script>")
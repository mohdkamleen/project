#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")
 
import cgi,cgitb
result=cgi.FieldStorage()

delid=result.getvalue("qid")

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kamleen"
)

mycursor=mydb.cursor()
dell="delete from signin where id=%s"%(delid)
mycursor.execute(dell)
mydb.commit()
print("<script>window.location.href='user.py#user';</script>")





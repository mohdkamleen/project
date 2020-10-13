#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")  
import cgi


form = cgi.FieldStorage() 
email = form["email"].value
password = form["password"].value
 

if email == "mohdkamleen" and password == "kamleen3052":
    print("<script>window.location.href='user.py';</script>")
else:
    print("<script>window.location.href='../404.html';</script>")



import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kamleen"
)
mycursor=mydb.cursor()
 
sql = "select * from signin where email='%s' && password='%s'",(email, password)  
if(mycursor.execute(sql)):  
    mydb.commit()  
    print(" <h2>successfully login</h2> ")
else: 
    mydb.commit()  
    print("<h2>fail</h2>")  
 








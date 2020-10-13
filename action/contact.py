#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")
 
import mysql.connector  
import cgi  
form = cgi.FieldStorage()  
name = form["name"].value
email = form["email"].value
subject = form["subject"].value
message = form["message"].value 

print(""" 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>success</title>
    <meta http-equiv="refresh" content="1; url=../contact.py">
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script> 
</head>
<body>  
<script>
       swal("Success", "", "success"); 
</script>
</body>
</html> 
""") 

db = mysql.connector.connect(host="localhost", user="root", password="", database="kamleen") 
cr = db.cursor() 

cr.execute("INSERT INTO `contact`(`name`, `email`, `subject`, `message`) VALUES ('%s','%s','%s','%s')"%(name,email,subject,message))

db.commit()  
 
 

 
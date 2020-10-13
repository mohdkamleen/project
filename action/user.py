#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe
print("Content-Type: text/html\r\n\r\n")

print("""

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="rgb(214, 218, 215)">
    <meta name="Keywords"
        content="HTML,CSS,JavaScript,SQL,PHP,jQuery,Bootstrap,Python,C,C++,digicoders,training,summer training">
    <meta name="Description"
        content=" In this Website Im trained with digicoders and its makeing for my all Projet, Assignment and about me and my training company....... ">
    <meta property="og:logo"
        content="https://digicoders.in/images/Logo/DigiCoders%20Technologies%20Logo%20Transparent.png">
    <meta property="og:url" content="https://mohdkamleen.github.io/digicoders/">
    <meta property="og:type" content="website">
    <meta property="og:title" content="Plink - Create payment links and send them to your clients">
    <meta property="og:description" content="Im trained with digicoders and its makeing for my all Projet.">
    <meta property="og:image"
        content="https://digicoders.in/images/Logo/DigiCoders%20Technologies%20Logo%20Transparent.png">
    <meta property="og:site_name" content="digicoders">
    <meta property="og:locale" content="en-EN">
    <meta property="og:locale:alternate" content="nl-NL">
    <meta property="og:locale:alternate" content="de-DE">
    <meta property="og:locale:alternate" content="fr-FR">
    <meta name='robots' content='index,follow' />
    <meta name="msapplication-TileColor" content="rgb(214, 218, 215)">
    <link rel="apple-touch-icon"
        href="https://digicoders.in/images/Logo/DigiCoders%20Technologies%20Logo%20Transparent.png">
    <title>Mohd Kamleen | User's</title>
    <!-- title image favicon  -->
    <link rel="shortcut icon" href="../media/image/logo.svg" type="image/x-icon">
    <!-- manually style sheet  -->
    <link rel="stylesheet" href="../css/loader.css">
    <link rel="stylesheet" href="../css/nav.css">
    <link rel="stylesheet" href="../css/user.css">
    <link rel="stylesheet" href="../css/main.css"> 
    <link rel="stylesheet" href="../css/bootstraph.css"> 
    <!-- dark mode access style sheet  -->
    <link rel="stylesheet" href="../css/dark.css">

</head>



<body>
    <div id="main_div">

        <div class="header">

            <!-- preloader  -->
            <div class="preloader">
                <span><b>0</b>%</span>
                <p>Loading<b>.</b><b>.</b><b>.</b></p>
            </div> 

            <!-- navigation seceion  -->
            <nav>
                <div class="navigation">
                    <div class="logo">
                        <h1>kam<span>leen</span></h1>
                    </div>

                    <div class="navbar">
                        <ul>
                            <li><a href="../index.py">Home </a></li>
                            <li><a href="../project.py">Project</a></li>
                            <li><a href="../contact.py">Contact</a></li>
                            <li><a href="../other.py">Other</a></li>
                        </ul>
                    </div>
                    <div class="hamburger"></div>
                </div>
                <div class="menu_background1"></div>
                <div class="menu_background2"></div>
            </nav>

            <header>
                <section>
                    <div class="body_content_header">
                        <div class="nav_background"></div>
                        <div class="nav_hamburger_background"></div>

                        <div class="header_top">
                            <div class="about-me">
                                <h3>
                                    Authentication is the process of determining if the request has come from a valid
                                    user who has the required privileges to use the system. In the world of computer
                                    networking this is a very vital requirement as many systems keep interacting with
                                    each other and proper mechanism needs to ensure that only valid interactions happen
                                    between these programs.
                                    <br><br>

""") 

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kamleen"
)
mycursor=mydb.cursor()

sel="select * from signin"
mycursor.execute(sel)
data=mycursor.fetchall() 
    

print("""  
    <button>%s user available</button>
"""%len(data))

print("""
                            
                                </h3>
                            </div>
                            <div class="header_img">
                                <img class="nav_background_img" src="../media/image/undraw_smart_home_28oy.svg"
                                    alt="header image">
                            </div>
                        </div>

                    </div>

        <div class="show_user">
           <table class="table table-responsive table-hover table-bordered" id="user"> 
      <tr class="thead">
        <th> <h3 style="font-size: 15px;">id</h3></th>
        <th> <h3 style="font-size: 15px;">name</h3></th>
        <th> <h3 style="font-size: 15px;">email</h3></th>
        <th> <h3 style="font-size: 15px;">password</h3></th> 
        <th> <h3 style="font-size: 15px;">delete</h3></th>
        <th> <h3 style="font-size: 15px;">edit</h3></th>
      </tr> 

""")
for x in data: 
    print("""
    <form action="user_update.py"> 
      <tr>
        <td class="text-center"><input type="text" name="user_id" style="border: none; outline: none; background: transparent;" value="%s"></td> 
        <td class="text-center"><input type="text" name="user_name" style="border: none; outline: none; background: transparent;" value="%s"></td> 
        <td class="text-center"><input type="text" name="user_email" style="border: none; outline: none; background: transparent;" value="%s"></td> 
        <td class="text-center"><input type="text" name="user_password" style="border: none; outline: none; background: transparent;" value="%s"></td>  
        <td class="text-center"><button class="btn "><a href="user_delete.py?qid=%s">delete</a></button></td> 
        <td class="text-center"> <button class="btn "><input style="border: none; outline: none; background: transparent;" type="submit" value="edit"> </button></td> 
      </tr>
    </form>
"""%(x[0],x[1],x[2],x[3],x[0]))                  
                        
                       
print("""

  </table> 
        
        <h3>The contact page is extremely important because if a visitor is on this page, they trying 
            to speak with you or ask some critical questions. This can be a turning point for your business 
            relationship. Make sure you direct them to the right person or department so both parties can benefit.  <br><br>
""") 

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kamleen"
)
mycursor=mydb.cursor()

sel="select * from contact"
mycursor.execute(sel)
data=mycursor.fetchall() 
    

print("""  
    <button>%s user contact's</button>
"""%len(data))

print("""
</h3>
<table class="table table-responsive table-hover  table-bordered" id="contact"> 
    <tr class="thead">
      <th> <h3 style="font-size: 15px;">id</h3></th>
      <th> <h3 style="font-size: 15px;">name</h3></th>
      <th> <h3 style="font-size: 15px;">email</h3></th>
      <th> <h3 style="font-size: 15px;">subject</h3></th> 
      <th> <h3 style="font-size: 15px;">message</h3></th> 
      <th> <h3 style="font-size: 15px;">action</h3></th>
    </tr> 

""")
for x in data: 
  print("""
    <tr>
      <td class="text-center">%s</td>
      <td class="text-center">%s</td>
      <td class="text-center">%s</td>
      <td class="text-center">%s</td> 
      <td class="text-center">%s</td> 
      <td class="text-center"><button class="btn "><a href="contact_delete.py?qid=%s">delete</a></button></td> 
    </tr>
"""%(x[0],x[1],x[2],x[3],x[4],x[0]))                  
                      
                     
print("""

</table> 
        <h3>The comments you are leaving are building your reputation. 
            Make it a good one that shows you are knowledgeable 
            and even-handed, instead of a disagreeable jerk with 
            little to add to the conversation.  <br><br>
""") 

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kamleen"
)
mycursor=mydb.cursor()

sel="select * from comments"
mycursor.execute(sel)
data=mycursor.fetchall() 
    

print("""  
    <button>%s user comment's</button>
"""%len(data))

print("""
</h3>
<table class="table table-responsive table-hover table-bordered" id="comment"> 
    <tr class="thead">
      <th> <h3 style="font-size: 15px;">id</h3></th>
      <th> <h3 style="font-size: 15px;">user</h3></th>
      <th> <h3 style="font-size: 15px;">comment</h3></th>
      <th> <h3 style="font-size: 15px;">date</h3></th> 
      <th> <h3 style="font-size: 15px;">delete</h3></th>
      <th> <h3 style="font-size: 15px;">edit</h3></th>
    </tr> 

""")
for x in data: 
  print("""
  <form action="comment_edit.py"> 
    <tr>
      <td class="text-center">%s</td>
      <td class="text-center"><input type="text" name="user" style="border: none; outline: none; background: transparent;" value="%s"></td>
      <td class="text-center"><input type="text" name="edit_comment" style="border: none; outline: none; background: transparent;" value="%s"></td>
      <td class="text-center"><input type="text" name="date_comment" style="border: none; outline: none; background: transparent;" value="%s"></td> 
      <td class="text-center"><button class="btn "><a href="comment_delete.py?qid=%s">delete</a></button></td> 
      <td class="text-center"><button class="btn "><input type="hidden" name="comment_id" style="border: none; outline: none; background: transparent;" value="%s"> <input style="border: none; outline: none; background: transparent;" type="submit" value="edit">  </button></td> 
    </tr>
  </form>
"""%(x[1],x[3],x[2],x[0],x[1],x[1]))                  
                      
                     
print("""

</table> 
        </div>
                </section>
            </header> 
        </div>
    </div>


    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="../js/main.js"></script>
    <script src="../js/nav.js"></script>
</body>

</html>

""")
#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")

print("""


<!DOCTYPE html>
<html lang="en">

<head>
    <style>
        h1 {
            color: #555555;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: lighter;
        }

        .container {
            position: relative;
            top: 0;
            left: 0;
            text-align: center;
            overflow: auto;
            width: 700px;
        }

        .text {
            color: #555555;
            font-size: 20px;
        }

        span {
            font-weight: bolder;
            font-size: 30px;
            color: #999999;
        }

        img {
            height: 160px;
            width: 150px;
            background: rgb(214, 214, 214);
            display: inline-block;
            border: 1px solid gray;
            border-radius: 3px;
            margin: 5px;
        }
    </style>
</head>

<body>
    <h1> 3. Design a webpage like this.</h1>

    <div class="container">
        <div class="text">Our work <br> <span>.</span><span>.</span><span>.</span> </div>
        <div>
            <img src="https://source.unsplash.com/150x160/?java,phone" alt="work">
            <img src="https://source.unsplash.com/150x160/?computer,mobile" alt="work">
            <img src="https://source.unsplash.com/150x160/?contact,company" alt="work">
            <img src="https://source.unsplash.com/150x160/?css,html" alt="work">
        </div>
    </div>
</body>

</html>

""")
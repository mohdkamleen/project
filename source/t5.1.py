#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")

print("""


<!DOCTYPE html>
<html lang="en">

<head>
    <style>
        * {
            user-select: none;
        }

        h1 {
            color: #555555;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: lighter;
        }

        .container {
            position: relative;
            top: 0;
            left: 0;
            height: 200px;
            width: 1000px;
            background: rgb(112, 190, 136);
            overflow: auto;
        }

        nav {
            position: absolute;
            top: 20px;
            left: 20px;
            right: 20px;
            background: #ffffff;
            height: 50px;
        }

        nav li {
            list-style: none;
            font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            font-size: 20px;
            float: left;
            margin: 0px 10px;
            text-transform: uppercase;
            text-align: center;
            color: rgb(112, 190, 136);
        }

        nav li:hover {
            color: rgb(6, 119, 6);
        }
    </style>
</head>

<body>

    <h1> 1. Design a menu bar using html and css. </h1>

    <div class="container">
        <!-- nav bar task........  -->

        <nav>
            <ul>
                <li> home </li>
                <li> tutorial </li>
                <li> wallpaper </li>
                <li> team work </li>
                <li> feedback </li>
                <li> contact us </li>
                <li> about us </li>
                <li> blog </li>
            </ul>
        </nav>

    </div>
</body>

</html>

""")
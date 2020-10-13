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
            height: 300px;
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

        nav ul li {
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
            color: rgb(1, 78, 1);
        }

        nav ul li ul li {
            color: rgb(112, 190, 136);
            float: none;
            position: relative;
            margin: 5px 0;
            padding: 2px;
        }

        nav ul li ul li ul li {
            float: none;
            color: rgb(112, 190, 136);
            margin: 5px 0;
        }

        nav ul li:hover>ul {
            display: block;
        }

        nav ul li ul li:hover>ul {
            display: block;
        }

        nav ul li ul {
            display: none;
            background: #ffffff;
            padding: 0;
        }

        nav ul li ul li ul {
            display: none;
            position: absolute;
            background: #ffffff;
            left: 125px;
            padding: 0 10px;
        }
    </style>
</head>

<body>
    <h1> 2. Design a sub-menu bar using html and css. </h1>
    <div class="container">
        <!-- nav bar task........  -->

        <nav>
            <ul>
                <li> home </li>
                <li> tutorial </li>
                <li> wallpaper </li>
                <li> team work &#x21d3
                    <ul>
                        <li>project 1</li>
                        <li>project 2 &#x21d3
                            <ul>
                                <li>module1</li>
                                <li>module2</li>
                                <li>module3</li>
                                <li>module4</li>
                                <li>module5</li>
                            </ul>
                        </li>
                        <li>project 3</li>
                    </ul>
                </li>
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
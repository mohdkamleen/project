#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")

print("""


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <style>
        * {
            padding: 0;
            margin: 0;
            box-sizing: border-box;
        }

        .game {
            display: flex;
            flex-wrap: wrap;
            margin: 20px;
            position: relative;
            width: 500px;
            height: 500px;
        }

        .green {
            background-color: green;
        }

        .red {
            background-color: red;
            border: none;
        }

        .yellow {
            background-color: rgb(246, 246, 87);
            border: none;
        }

        .blue {
            background-color: blue;
            border: none;
        }

        .house {
            display: inline-block;
            position: absolute;
            width: 40%;
            height: 40%;
            padding: 7%;
        }

        .box {
            position: relative;
            width: 100%;
            height: 100%;
            background-color: white;
            padding: 20%;
        }

        .square {
            position: absolute;
            width: 25%;
            height: 25%;
            border-radius: 50%;

        }

        .square-one {
            top: 20%;
            left: 20%;
        }

        .square-two {
            top: 20%;
            right: 20%;
        }

        .square-three {
            bottom: 20%;
            left: 20%;
        }

        .square-four {
            bottom: 20%;
            right: 20%;
        }

        .home {
            position: absolute;
            top: 40%;
            left: 40%;
            width: 20%;
            height: 20%;
            border-bottom: 50px solid red;
            border-top: 50px solid rgb(246, 246, 87);
            border-left: 50px solid green;
            border-right: 50px solid blue;
        }

        .cells {
            position: absolute;
            width: 6.66%;
            height: 6.66%;
            border-collapse: collapse;
            border: 1px solid #e5e5e569;
        }

        h1 {
            color: #555555;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: lighter;
        }
    </style>
</head>

<body>
    <h1> 1. Design a chesboard using div tag. </h1>

    <div class="game">
        <div class="house green">
            <div class="box">
                <div class="square square-one green"></div>
                <div class="square square-two green"></div>
                <div class="square square-three green"></div>
                <div class="square square-four green"></div>
            </div>
        </div>

        <div class="house yellow" style="right: 0">
            <div class="box">
                <div class="square square-one yellow"></div>
                <div class="square square-two yellow"></div>
                <div class="square square-three yellow"></div>
                <div class="square square-four yellow"></div>
            </div>
        </div>

        <div class="house red" style="bottom: 0">
            <div class="box">
                <div class="square square-one red"></div>
                <div class="square square-two red"></div>
                <div class="square square-three red"></div>
                <div class="square square-four red"></div>
            </div>
        </div>

        <div class="house blue" style="bottom: 0;right: 0">
            <div class="box">
                <div class="square square-one blue"></div>
                <div class="square square-two blue"></div>
                <div class="square square-three blue"></div>
                <div class="square square-four blue"></div>
            </div>
        </div>

        <div class="home"></div>
        <div class="cells" style="top: 40%;"></div>
        <div class="cells" style="top: 40%;left:6.66%; background: green;"></div>
        <div class="cells" style="top: 40%;left:13.32%;"></div>
        <div class="cells" style="top: 40%;left:19.98%;"></div>
        <div class="cells" style="top: 40%;left:26.64%;"></div>
        <div class="cells" style="top: 40%;left:33.3%;"></div>

        <div class="cells" style="top: 0;left:40%;"></div>
        <div class="cells" style="top: 6.66%;left:40%;"></div>
        <div class="cells safe" style="top: 13.32%;left:40%;"></div>
        <div class="cells" style="top: 19.98%;left:40%;"></div>
        <div class="cells" style="top: 26.64%;left:40%;"></div>
        <div class="cells" style="top: 33.3%;left:40%;"></div>

        <div class="cells" style="top: 0;left:46.66%;"></div>
        <div class="cells yellow" style="top: 6.66%;left:46.66%;"></div>
        <div class="cells yellow" style="top: 13.32%;left:46.66%;"></div>
        <div class="cells yellow" style="top: 19.98%;left:46.66%;"></div>
        <div class="cells yellow" style="top: 26.64%;left:46.66%;"></div>
        <div class="cells yellow" style="top: 33.3%;left:46.66%;"></div>

        <div class="cells" style="top: 0;left:53.32%;"></div>
        <div class="cells" style="top: 6.66%;left:53.32%; background: rgb(246, 246, 87);"></div>
        <div class="cells" style="top: 13.32%;left:53.32%;"></div>
        <div class="cells" style="top: 19.98%;left:53.32%;"></div>
        <div class="cells" style="top: 26.64%;left:53.32%;"></div>
        <div class="cells" style="top: 33.3%;left:53.32%;"></div>

        <div class="cells" style="top: 40%; right: 33.3%"></div>
        <div class="cells" style="top: 40%;right:26.64%;"></div>
        <div class="cells" style="top: 40%;right:19.98%;"></div>
        <div class="cells safe" style="top: 40%;right:13.32%;"></div>
        <div class="cells" style="top: 40%;right:6.66%;"></div>
        <div class="cells" style="top: 40%;right:0;"></div>

        <div class="cells blue" style="top: 46.66%; right: 33.3%"></div>
        <div class="cells blue" style="top: 46.66%;right:26.64%;"></div>
        <div class="cells blue" style="top: 46.66%;right:19.98%;"></div>
        <div class="cells blue" style="top: 46.66%;right:13.32%;"></div>
        <div class="cells blue" style="top: 46.66%;right:6.66%;"></div>
        <div class="cells" style="top: 46.66%;right:0;"></div>

        <div class="cells" style="top: 53.32%; right: 33.3%"></div>
        <div class="cells" style="top: 53.32%;right:26.64%;"></div>
        <div class="cells" style="top: 53.32%;right:19.98%;"></div>
        <div class="cells" style="top: 53.32%;right:13.32%;"></div>
        <div class="cells" style="top: 53.32%;right:6.66%; background: blue;"></div>
        <div class="cells" style="top: 53.32%;right:0;"></div>

        <div class="cells" style="bottom: 0;left:53.32%;"></div>
        <div class="cells" style="bottom: 6.66%;left:53.32%;"></div>
        <div class="cells safe" style="bottom: 13.32%;left:53.32%;"></div>
        <div class="cells" style="bottom: 19.98%;left:53.32%;"></div>
        <div class="cells" style="bottom: 26.64%;left:53.32%;"></div>
        <div class="cells" style="bottom: 33.3%;left:53.32%;"></div>

        <div class="cells" style="bottom: 0;left:46.66%;"></div>
        <div class="cells red " style="bottom: 6.66%;left:46.66%;"></div>
        <div class="cells red" style="bottom: 13.32%;left:46.66%;"></div>
        <div class="cells red" style="bottom: 19.98%;left:46.66%;"></div>
        <div class="cells red" style="bottom: 26.64%;left:46.66%;"></div>
        <div class="cells red" style="bottom: 33.3%;left:46.66%;"></div>

        <div class="cells" style="bottom: 0;left:40%;"></div>
        <div class="cells" style="bottom: 6.66%;left:40%; background: red;"></div>
        <div class="cells" style="bottom: 13.32%;left:40%;"></div>
        <div class="cells" style="bottom: 19.98%;left:40%;"></div>
        <div class="cells" style="bottom: 26.64%;left:40%;"></div>
        <div class="cells" style="bottom: 33.3%;left:40%;"></div>

        <div class="cells" style="top: 53.32%; left: 33.3%"></div>
        <div class="cells" style="top: 53.32%;left:26.64%;"></div>
        <div class="cells" style="top: 53.32%;left:19.98%;"></div>
        <div class="cells safe" style="top: 53.32%;left:13.32%;"></div>
        <div class="cells" style="top: 53.32%;left:6.66%;"></div>
        <div class="cells" style="top: 53.32%;left:0;"></div>

        <div class="cells green" style="top: 46.66%;left: 33.3%"></div>
        <div class="cells green" style="top: 46.66%;left:26.64%;"></div>
        <div class="cells green" style="top: 46.66%;left:19.98%;"></div>
        <div class="cells green" style="top: 46.66%;left:13.32%;"></div>
        <div class="cells green" style="top: 46.66%;left:6.66%;"></div>
        <div class="cells" style="top: 46.66%;left:0;"></div>


    </div>

    <a href="t4.1.html" download="tast ludo" style="margin: 40px 10px; "> download </a>

</body>

</html>

""")
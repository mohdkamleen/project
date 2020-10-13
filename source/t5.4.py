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
            height: 400px;
            background: linear-gradient(90deg, rgb(78, 67, 221), rgb(49, 240, 43));
            margin: 0 5%;
            min-width: 1000px;
            overflow: auto;
        }

        .text {
            color: #555555;
            font-size: 25px;
            color: rgb(226, 221, 221);
            font-family: Arial, Helvetica, sans-serif;
            padding: 10px;
        }

        span {
            font-weight: bolder;
            font-size: 30px;
            color: #dddddd;
        }

        .down {
            display: flex;
            justify-content: space-around;
            align-items: center;
        }

        iframe {
            height: 200px;
            width: 200px;
            border: 2px solid #555555;
            border-radius: 50%;
            margin: 20px;
        }

        .form {
            padding: 10px;
        }

        input,
        textarea {
            padding: 10px;
            margin: 8px;
            border-radius: 4px;
            border: 1px solid #999999;
        }

        textarea {
            width: 380px;
            height: 70px;
        }

        #send {
            background: red;
            border-radius: 50px;
            margin: 0px 300px 10px 10px;
        }
    </style>
</head>

<body>
    <h1> 4. Design a webpage for footer.</h1>

    <div class="container">
        <div class="text">Contact us <br> <span>.</span><span>.</span><span>.</span> </div>
        <div class="down">
            <div class="form">
                <form action="#">
                    <input type="text" required id="name" placeholder="Full Name">
                    <input type="text" required id="email" placeholder="Your Email"> <br>
                    <input type="text" required id="phone" placeholder="Your Phone">
                    <input type="text" required id="level" placeholder="Budget Level"> <br>
                    <textarea required id="message" placeholder="Your Requirements"></textarea> <br>
                    <input type="submit" onclick="send_data()" id="send" value="Send message">
                </form>
            </div>
            <div class="map">
                <iframe
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3558.9015068900007!2d80.93581361504417!3d26.874870183143937!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x399bfd90f852511b%3A0xea3004cdf494ecbb!2sDigiCoders%20Technologies%20Private%20Limited!5e0!3m2!1sen!2sin!4v1594887869365!5m2!1sen!2sin"></iframe>
            </div>
        </div>
    </div>
    <script>



        function send_data() {


            const name = document.getElementById("name").value;
            const phone = document.getElementById("phone").value;
            const message = document.getElementById("message").value;
            const level = document.getElementById("level").value;
            const email = document.getElementById("email").value;


            console.log({
                "name": name,
                "phone": phone,
                "message": message,
                "budget level": level,
                "email": email
            });

        }
    </script>


</body>

</html>

""")
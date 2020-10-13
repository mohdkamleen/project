#!C:\Users\Lenovo\AppData\Local\Programs\Python\Python38\python.exe 
print("Content-Type: text/html\r\n\r\n")

print("""


<html>

<head>
	<meta name="theme-color" content="#1cb2f3">
	<style>
		* {
			user-select: none;
			outline: none;
		}

		body {
			background: linear-gradient(-45deg, white, white, #00b3ff, white, #fff);
			min-height: 500px;
		}

		fieldset {
			background-image: linear-gradient(-45deg, white, white, #00b3ff 50%, white, #fff);
			position: absolute;
			top: 50%;
			left: 50%;
			transform: translate(-50%, -50%);
			padding: 10px 20px;
		}

		input,
		textarea {
			width: 60px;
			color: #000;
			height: 50px;
			width: 60px;
			border: 2px solid black;
			border-radius: 50px;
			font-size: 25px;
			background: white;
			margin: 5px;
		}

		textarea {
			font-size: 20px;
		}

		.text_area {
			padding: 10;
			background: linear-gradient(-42deg, white, white, #00b3ff, white, #fff);
			width: 230px;
			max-width: 230px;
			height: auto;
			min-height: 50px;
			overflow-x: hidden;
		}

		.da {
			width: 110px;
			color: 000;
			background-color: none;
		}


		input:focus {
			border: 2px solid black;
			border-radius: 50px;
			color: blue;
			background: linear-gradient(-45deg, white, white, #00b3ff, white, #fff);
		}

		.ta {
			width: 90px;
		}


		::-webkit-scrollbar {
			width: 0;
		}

		#form {
			text-align: center;
		}
	</style>
</head>

<body>
	<div>
		<fieldset>
			<form name=form id="form">
				<textarea class="text_area" placeholder="start calculations" name=answer disabled></textarea><br>

				<input type="button" value=" 1 " onclick="form.answer.value += 1 ">
				<input type="button" value=" 2 " onclick="form.answer.value += 2 ">
				<input type="button" value=" 3 " onclick="form.answer.value += 3 ">

				<br>

				<input type="button" value=" 4 " onclick="form.answer.value += '4' ">
				<input type="button" value=" 5 " onclick="form.answer.value += '5' ">
				<input type="button" value=" 6 " onclick="form.answer.value += '6' ">

				<br>

				<input type="button" value=" 7 " onclick="form.answer.value += '7' ">
				<input type="button" value=" 8 " onclick="form.answer.value += '8' ">
				<input type="button" value=" 9 " onclick="form.answer.value += '9' ">

				<br>

				<input type="button" value=" + " onclick="form.answer.value += '+' ">
				<input type="button" value=" - " onclick="form.answer.value += '-' ">
				<input type="button" value=" * " onclick="form.answer.value += '*' ">


				<br>

				<input type="button" value=" / " onclick="form.answer.value += '/' ">
				<input type="button" value=" 0 " onclick="form.answer.value += '0' ">
				<input type="button" value=" . " onclick="form.answer.value += '.' ">


				<br>

				<input type="button" class="da" value="clear all" onclick="form.answer.value= '' ">
				<input type="button" class="ta" value=" = " onclick="form.answer.value=eval(form.answer.value)">




			</form>
		</fieldset>

		<a href="t8.2.html" download="calculator"
			style=" color:rgb(42, 79, 243); position: absolute; bottom: 0; padding: 10px; font-size: 20px; text-decoration: none; font-family: monospace;">
			Download </a>
	</div>
</body>


</html>

""")
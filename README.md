# CMPE150-MIDTERM1-GLASS-OF-WATER
Problem solution of the glass of water question in the first midterm exam of cmpe150
<html>
<head>
<link href="css/question.css" type="text/css" rel="stylesheet" />
<title>Assignment (teaching.codes)</title>
</head>
<body>
	<div class="container">
		<div class="row">
			<div class="col-lg-12">
				<h1>
					Question 1: <br><br>
					<code>A Glass of Water</code>
				</h1>
				<div>
					Please read <a href="ReadMe.html">important information</a> first.
				</div>
				<div id="page1">
					<h2>Description</h2>
					<p>
						&#8195;Assume that you have an empty glass.<br>
						&#8195;You're given <font color = "red">width</font>, <font color = "red">height</font> and <font color = "red">n</font> as inputs.<br>
						
						&#8195;Your task is to take a user input each round to determine how much water to add/remove from the glass and draw the glass with water. Use <font color = "red">O</font> to represent 1 unit of water<br>

						&#8195;1 < width and width is an integer<br>
						&#8195;1 < height and height is an integer<br><br>
						
						<b>Note:</b> You don't need to check the edge cases. (more water than possible, negative water etc.)<br>
					</p>
					<p>
						<h2>User Inputs:</h2>
						&#8195;&#8195;• ONCE<br>
						&#8195;&#8195;&#8195;• width : width of the glass<br>
						&#8195;&#8195;&#8195;• height : height of the glass<br>
						&#8195;&#8195;&#8195;• n : number of times the user adds/removes water from the glass<br><br>
						
						&#8195;&#8195;• FOR n TIMES<br>
						&#8195;&#8195;&#8195;• change in the amount of water<br>
					</p>
					<p>
						<h2>Outputs:</h2>
						&#8195;&#8195;• Print the glass (with water) everytime after taking water input from the user<br>
						&#8195;&#8195;• Print the glass #<br>
						
						&#8195;&#8195;• Empty glass with height = 8, width = 10 should look like this : <br><br>
						
						&#8195;&#8195;&#8195;&#8195;<img src="empty_bottle.png"> <br>
						
					</p>
					<p>
						<b>Warning:</b> You are not allowed to use any imports.<br>
					</p><br>

					<h2>Examples:</h2>
					
					<b>Example Description:</b> glass height is 8, glass width is 10 and move_count is 5.<br>
					We start by adding 20 water and continue until we take 5 water inputs.<br><br>
					<table>
						<tr class="header">
							<td>INPUTS</td>
							<td>OUTPUTS</td>
						</tr>
						<tr>
							<td style = "white-space: nowrap">
							10<br>8<br>5<br>20<br>4<br>8<br>-5<br>-20
							</td>
							<td style = "white-space: nowrap">
							<img src="example.png">
							</td>
						</tr>
					</table>
					<br>
					<b>Note:</b> Green numbers in the output screenshot are inputs, you shouldn't print them again.<br>
				</div>
			</div>
		</div>
	</div>
</body>
</html>

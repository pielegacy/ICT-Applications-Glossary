<!DOCTYPE html>
<html>
	<head>
		<title>{{name}} Terms</title>
		<link type="text/css" href="/main.css" rel="stylesheet">
		<link rel="shortcut icon" href="/static/icon.ico">
	</head>
	<body>
		<div id="terms">
			<h1>{{name}}</h1>
			<a href="/">Return Home</a>
			%count = 0
			%for term in terms:
				<div class="define">
					<h3>{{term}}</h3>
					<div class="actdefinition">{{defins[count]}}</div>
				</div>
			%end
		</div>
	</body>
</html>
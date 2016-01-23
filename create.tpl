<!DOCTYPE html>
<html>
	<head>
		<title>Add Definition</title>
		<link type="text/css" href="/main.css" rel="stylesheet">
		<link rel="shortcut icon" href="/static/icon.ico">
	</head>
	<body>
		<div id="terms">
			<h1>Add Definition</h1>
			<form action="/create" method="post">
				<input name="term" type="text" placeholder="Term*"/><br>
				<textarea name="define" placeholder="Definition*"></textarea><br>
				<input name="category" type="text" class="cat" placeholder="Category"/><br>
				<input class="sub" value="Create Term" type="submit"/>
			</form>
		</div>
	</body>
</html>
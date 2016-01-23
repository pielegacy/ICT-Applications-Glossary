<!DOCTYPE html>
<html>
	<head>
		<title>Glossary Terms</title>
		<link type="text/css" href="main.css" rel="stylesheet">
		<link rel="shortcut icon" href="/static/icon.ico">
	</head>
	<body>
		<div id="terms">
			<h1>ICT Glossary</h1>
			View by :
			<a class="navlinks" href="concept">Concept</a>
			%count = 0
			%for term in terms:
				<div class="define">
					<h3>{{term}}</h3>
					<div class="actdefinition">{{defins[count]}}</div>
					<a href="category/{{cats[count]}}">Part of {{cats[count]}}</a>
					%count += 1
				</div>
			%end
		</div>
		<footer>
			Tools<br><a class="navlinks" href="create">Add Term</a>
		</footer>
	</body>
</html>
<!DOCTYPE html>
<html>
	<head>
		<title>ICT Concepts</title>
		<link type="text/css" href="/main.css" rel="stylesheet">
		<link rel="shortcut icon" href="/static/icon.ico">
	</head>
	<body>
		<div id="terms">
			<h1>ICT Concepts</h1>
			<a href="/">Return Home</a>
			<p class="concepts">The terms in this glossary can be sorted into these concepts : </p>
			%count = 0
			%for term in terms:
				<div class="define">
					<p class="concepts"><a href="category/{{term}}">{{term}}</a></p>
				</div>
			%end
		</div>
	</body>
</html>
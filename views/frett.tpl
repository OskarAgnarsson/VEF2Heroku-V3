<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Hasarfréttir</title>
	<link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
	% include("haus.tpl")
	<div class="row">
		<section><h3>{{frett[0]}}</h3></section>
		<section><h3></h3></section>
		<section><img src="/static/mynd{{nr}}.jpg"></section>
		<section class="pd2">
			<p>{{frett[1]}}</p>
			<p>{{frett[2]}}</p>
			<h6><a href="/b">Aftur á Hasarfréttir</a></h6>
		</section>
	</div>
	% include("footer.tpl")
</body>
</html>
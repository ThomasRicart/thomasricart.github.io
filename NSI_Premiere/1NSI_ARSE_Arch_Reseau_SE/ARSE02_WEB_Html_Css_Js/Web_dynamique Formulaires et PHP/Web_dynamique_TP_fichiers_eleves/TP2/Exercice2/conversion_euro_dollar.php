<!DOCTYPE html>
<html lang="fr">	

<head>
	<meta charset="UTF-8" />
	<link rel="stylesheet" type="text/css" href="style.css">
	<title>Conversion euro-dollar</title>
</head>

<body>

<?php
	$Val = $_GET['valeur'];
	$To = $_GET['taux'];
	$Dev = $_GET['devise'];
	
	date_default_timezone_set('Europe/Paris');
	$date = date("d/m/Y");
	$heure = date("G\hi");
	
	echo "<h3>Simulation effectuée le ... à ... :</h3><hr/>";

	if($Dev == ...)
	{
		$somme = round(...,2);
		echo "<p>Somme obtenue : $somme dollars.</p><hr/>";
	}
	else
	{
		$somme = round(...,2);
		echo "<p>Somme obtenue : ....</p><hr/>";
	}
?>

	<p><a href='index.html'>Recommencer une nouvelle simulation</a></p>
</body>
</html>
<!DOCTYPE html>
<html lang="fr">	

<head>
	<meta charset="UTF-8" />
	<title>Confirmation ajout rdv</title>
</head>


<?php
	require_once 'data_access.php';

	$jour = $_POST['dateJ'];
	$mois = $_POST['dateM'];
	$annee = $_POST['dateA'];
	$heure = $_POST['hour'];
	$agenda = $_POST['agenda'];
	$titre = (string) $_POST['titre'];

	$date = date_create_from_format('j/n/Y', $jour.'/'.$mois.'/'.$annee);
	$year = date_format($date, 'o'); // numéro de l'année au format ISO
	$week = (int)date_format($date, 'W'); //numéro de la semaine (démarre un lundi) au format ISO et sans 0
	$day = date_format($date, 'N'); // numéro du jour (1 pour lundi ; 7 pour dimanche) au format ISO

	append_creneau($year,$week,$day,$heure,$agenda,$titre);
?>
             

<body>
	<p>Le rendez-vous a bien été ajouté.</p>
	<br/>
	<p>Cliquez <a href="display.php?year=<?php echo $year?>&week=<?php echo $week?>">ici</a> pour vérifier le rendez-vous.</p>
	<br/><hr/>
	<p>
		<a href="agenda.html">Consulter l'agenda</a><br/>
		<a href="ajoutRDV.html">Ajouter un autre rendez-vous à l'agenda</a>
	</p>
</body>
</html>
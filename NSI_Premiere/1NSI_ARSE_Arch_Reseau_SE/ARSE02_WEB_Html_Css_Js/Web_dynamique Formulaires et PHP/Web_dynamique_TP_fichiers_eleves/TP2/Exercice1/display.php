<!DOCTYPE html>
<html lang="fr">	

<head>
	<meta charset="UTF-8" />
	<link rel="stylesheet" type="text/css" href="display_table.css">

<?php
require_once 'display_table.php';

$year = $_GET['year'];
$week = $_GET['week'];

$lundi = date_create();
date_isodate_set($lundi, $year, $week);

$jour_semaine = array($lundi);
for($i=1;$i<=6;$i++)
{
	$jour_semaine[] = clone $lundi;
	date_add($jour_semaine[$i], new DateInterval("P$i"."D"));
}


if($week>1){$year_prec=$year; $week_prec=$week-1;}else{$year_prec=$year-1; $week_prec=52;}
if($week<52){$year_next=$year; $week_next=$week+1;}else{$year_next=$year+1; $week_next=1;}

display($year,$week,$year_prec,$week_prec,$year_next,$week_next,$jour_semaine);
?>

	</div>
   	<div id="footer">
		<hr/>
		<p><a href="agenda.html">Consulter une autre semaine</a><br/>
		<a href="ajoutRDV.html">Ajouter un rendez-vous à l'agenda</a></p>
	</div>

</body>
</html>
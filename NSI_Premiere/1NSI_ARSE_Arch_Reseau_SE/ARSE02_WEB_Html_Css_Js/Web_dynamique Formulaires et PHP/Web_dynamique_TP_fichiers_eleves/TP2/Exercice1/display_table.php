<?php
	require_once 'data_access.php';
	
	
	// Affichage du début de la table
	function table_begin()
    {
		echo "<table>";
	}
	

	// Affichage de l'entête de la table
	function table_header($L)
    {
		$jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche'];
		echo "<tr><th></th>";
		for($i=0;$i<7;$i++)
        {
			echo "<th class='date'>$jours[$i]<br/>".date_format($L[$i],'d/m/Y')."</th>";
		}
		echo "</tr>";
	}
	
	
	// Affiche des lignes de la table
	function table_rows($L)
	{
		for($i=0;$i<24;$i++)
		{
			if($i<10)
			{
				echo "<tr><th class='horaire'>0$i:00</th>";
			}
			else
			{
				echo "<tr><th class='horaire'>$i:00</th>";
			}
			for($j=0;$j<7;$j++)
			{
				if($L[$i][$j] == 0)
				{
					echo "<td></td>";
				}
				else
				{
					echo "<td class=\"".$L[$i][$j][0]."\">".$L[$i][$j][1]."</td>";
				}
			}
			echo "</tr>";
		}
	}
	
	
	// Affichage de la fin de la table
	function table_end()
    {
		echo "</table><br/>";
	}
	
	
	// Affichage de la semaine de l'agenda
	function display($y,$w,$y_p,$w_p,$y_n,$w_n,$L)
    {	
		echo "<title>Consultation semaine $w</title>
			</head>

			<body>
				<div id='entete'>
					<h1>Semaine du ".date_format($L[0],'d/m/Y')." au ".date_format($L[6],'d/m/Y')." (sem. $w)</h1>
					<table id='nav'>
						<tr>
							<td id='pred'><a href=\"display.php?year=$y_p&week=$w_p\">Semaine précédente</a></td>
							<td id='succ'><a href=\"display.php?year=$y_n&week=$w_n\">Semaine suivante</a></td>
						</tr>
					</table>
					<hr/>
				</div>
				<div id='contents'>";

		$planning = load_week($y,$w);

		table_begin();
		table_header($L);
		table_rows($planning);
		table_end();
	}

?>
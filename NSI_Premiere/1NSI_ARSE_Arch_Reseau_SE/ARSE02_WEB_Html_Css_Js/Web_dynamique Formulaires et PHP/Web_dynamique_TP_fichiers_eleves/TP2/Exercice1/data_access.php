<?php
	function append_creneau($y,$w,$d,$H,$agenda,$titre)
	{
		$nom_fichier = "data/$y-$w.txt";
		$F = fopen($nom_fichier,'a');
		fwrite($F,"$d;$H;$agenda;$titre\n");
		fclose($F);
	}
	
	
	function initialisation_creneaux() // renvoie un tableau de 24 lignes et 7 colonnes
	{
		$tab = array();
		for($ligne=0;$ligne<24;$ligne++)
		{
			$tab[] = array();
			for($colonne=0;$colonne<7;$colonne++)
			{
				$tab[$ligne][] = 0;
			}
		}
		return $tab;
	}
	
	
	function load_week($y,$w)
	{
		$creneaux = initialisation_creneaux();
		
		$nom_fichier = "data/$y-$w.txt";
		if(file_exists($nom_fichier))
		{
			$F = fopen($nom_fichier,'r');
			while($ligne = fgets($F))
			{
				$L = explode(';',trim($ligne));
				$creneaux[(integer)$L[1]][(integer)$L[0]-1] = array($L[2],$L[3]);
			}
			fclose($F);
		}
		return $creneaux;
	}
?>
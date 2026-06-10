
( function ()
  {

      menu_gauche = document.createElement('aside');
      menu_gauche.id = "navparagraphe";
      menu_gauche.innerHTML = '	<ul id="menu_accordeon">\n	\n		</ul>\n';

      menu_droit = document.createElement('div');
      menu_droit.id = "menu_droit";
      menu_droit.innerHTML = '		<a href="#" title="Haut de page"><div id="haut"></div></a>\n		<a href="#" title="Page pr&eacute;c&eacute;dente"><div id="precedent"></div></a>\n		<a href="#" title="Page suivante"><div id="suivant"></div></a>\n		<a href="#" title="Accueil principal"><div id="retour_accueil"></div></a>\n';

      fil_dariane = document.createElement('ul');
      fil_dariane.id = "ariane";
      
      corps = document.getElementById('corps');
      
      corps.insertBefore(fil_dariane,corps.firstChild)

      document.body.insertBefore(menu_droit,document.body.firstChild)

      document.body.insertBefore(menu_gauche,document.body.firstChild)
  }) ();

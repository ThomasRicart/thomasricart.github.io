
/* appelé par RACINE/scripts/chargeur_capsule.js */

/* contient la liste des js propres au module, dont menu.js et icon.js 
   les variables à modifier sont scripts_du_module et css_du_module
*/

( function ()
  {

//      console.log("chargeur_dans_capsule")

/* chemins donnés à partir du dossier script_SUFFIXE de la capsule */

      let scripts_du_module = [
	  "menu.js",
//	  "icon.js", // charge l'icone du module dans chaque page
      ];

/* chemins donnés à partir de la racine de la capsule */

      let css_du_module = [
      ];


      /* question : a-t-on besoin de css spécifiques à la capsule, ou bien ceux-ci sont-ils plutôt sépcifiques à chaque page
	 et donc destinés à apparaître dans l'en-tête de la page ?*/

      /* Plus rien à modifier en dessous. */

      function conf_js(  modules)
      {
	  function ajoute_js ( url )
	  {
	      let objet_script = document.createElement("script");
	      objet_script.type = "text/javascript";
	      objet_script.src = url;
	      
	      document.head.appendChild(objet_script);   
	  }

	  chemin = document.currentScript.src.slice(0,document.currentScript.src.lastIndexOf("/")+1)

	  for (i=0; i < modules.length; i++)
	  {
	      ajoute_js(chemin+modules[i]);
	  }
	  
      }

      function conf_css( css_du_module)
      {
	  
	  function ajoute_css ( url )
	  {
	      let objet_link  = document.createElement('link');
	      
	      objet_link.rel  = 'stylesheet';
	      objet_link.type = 'text/css';
	      objet_link.href = url;
	      objet_link.media = 'all';
	      
	      document.head.appendChild( objet_link); // comment identifier une erreur de chargement ?
	  }
	  
	  chemin = document.currentScript.src.slice(0,document.currentScript.src.lastIndexOf("scripts"))
	  
//	  console.log(chemin)
  
	  for (i=0; i < css_du_module.length; i++)
	  {
	      ajoute_css(chemin+css_du_module[i]);
	  }
	  
      }
      
      conf_js(scripts_du_module)
      conf_css(css_du_module)
      
  })();

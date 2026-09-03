
/*

  Ce script charge (dynamiquement) des listes de feuilles de style css et de scripts javascript en détectant automatiquement le chemin où aller les chercher. Les hypothèses sur l'arborescence sont les suivantes :

  - dans les listes ci-dessous, les scripts et css d'environnements sont appelés à partir du répertoire 'RACINE/' de la formation (RACINE est détecté automatiquement)
  - ce script se trouve dans un sous dossier de l'arborescence de 'RACINE/'
  - chaque capsule est contenue dans un sous dossier du type 'RACINE/formation_SUFFIXE/' et les fichiers menu.js et icon.js se trouvent dans le dossier 'RACINE/formaton_SUFFIXE/scripts_SUFFIXE/' ( SUFFIXE est détecté automatiquement )

  - les listes de scripts sont arborescentes, de façon à gérer les dépendances entre scripts.

*/

(function ()
 {
     /* Les .css communs à toutes les pages, chemin donné à partir de la racine de la formation. */

      let css_d_environnement = [
	  "css/raz.css" ,
	  "css/prism.css",
	  "codemirror/lib/codemirror.css",
	  "codemirror/theme/rubyblue.css",
	  "css/Style_ISN_Terminale.css",
      ];

      /* Les .js communs à toutes les pages, chemin donné à partir de la racine de la formation. */
      
      let scripts_d_environnement = [
	  ["scripts/jquery.js",[
	      ["codemirror/lib/codemirror.js",[
		  ["codemirror/mode/python/python.js",[]],
		  ["codemirror/mode/xml/xml.js",[]],
		  ["codemirror/mode/javascript/javascript.js",[]],
		  ["codemirror/mode/css/css.js",[]],
		  ["codemirror/mode/htmlmixed/htmlmixed.js",[]],
		  ["codemirror/addon/edit/matchbrackets.js",[]],
		  ["scripts/prog_html.js",[]],               // dépend de jquery et codemirror
		  ["skulpt/skulpt.min.js",[
		      ["skulpt/skulpt-stdlib.js",[]],
		      ["scripts/prog_python.js",[]],         // dépend de jquery, codemirror et skulpt (?)
		      ["scripts/chargeur_capsule.js",[]],    // placé ici pour masquer le code codemirror dans les onglets après le rendu.
		                                             //Utiliser une fonction de rafraichissement de codemirror prévue pour à la place, de préférence.
		  ]],	  
	      ]],
	      ["scripts/jquery-iframe-auto-height-master/vendor/jquery.browser.js",[]],
	      ["scripts/jquery-iframe-auto-height-master/dist/jquery-iframe-auto-height.js",[]],
	  ]],
	  ["scripts/clipboard.min.js",[
	      ["scripts/prism.js",[]],
	  ]],
	  ["mathjax/MathJax.js?config=TeX-AMS_SVG-full&locale=fr",[]],
      ];

      /* la chaine de configuration de mathjax, 
         attention aux échappements imbriqués !
      */
      
      let chaine_config_mathjax = "MathJax.Hub.Config({showProcessingMessages: false,showMathMenu: false,showMathMenuMSIE: false,jax: ['input/TeX','output/SVG'],tex2jax: { inlineMath: [['$','$'],['\\\\(','\\\\)']] }});";

      /* ensuite les fonctions utilisées, plus rien n'est à modifier */
    
      function conf_mathjax ( )
      {
	  let objet_conf = document.createElement("script");
	  objet_conf.type = "text/x-mathjax-config";
	  
	  objet_conf.innerHTML = chaine_config_mathjax;
	  
	  document.head.appendChild(objet_conf);
      }
      
      function conf_css( chemin, css_d_environnement)
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
	  
	  chemin = trouve_les_chemins()
	  
	  for (i=0; i < css_d_environnement.length; i++)
	  {
	      ajoute_css(chemin+css_d_environnement[i]);
	  }
	  
      }
      
      function conf_js( chemin, modules)
      {
	  function ajoute_js ( url , deps)
	  {
	      let objet_script = document.createElement("script");
	      objet_script.type = "text/javascript";
	      objet_script.src = url;

//	      objet_script.onload= function() { console.log("load "+url); };

	      if (deps.length  > 0)
	      {
		  objet_script.onload= function() {
//		      console.log("dépendances de "+url);
		      conf_js(chemin, deps)
		  };
	      }
//	      console.log("chargement "+url)
	      document.head.appendChild(objet_script);   
	  }
	  

	  for (i=0; i < modules.length; i++)
	  {
	      ajoute_js(chemin+modules[i][0],modules[i][1]);
	  }
	  
      }
      
      function trouve_les_chemins()
      {
	  path1 = document.currentScript.src
	  path2 = document.currentScript.baseURI
	  
	  prefixe1 = ""
	  prefixe2 = ""
	  prefixecommun = ""
	  
	  start1 = 0
	  start2 = 0
	  
	  while (prefixe2.includes(prefixe1))
	  {
	      start1 = path1.indexOf("/",start1)+1
	      start2 = path2.indexOf("/",start2)+1
	      
	      prefixecommun = prefixe1
	      
	      prefixe1 = path1.slice(0,start1)
	      prefixe2 = path2.slice(0,start2)
	  }
	  
	  return ( prefixecommun )
      }

      chemin = trouve_les_chemins()
      
      conf_mathjax()
      
      conf_css( chemin, css_d_environnement)

      conf_js( chemin, scripts_d_environnement)

 }) ();

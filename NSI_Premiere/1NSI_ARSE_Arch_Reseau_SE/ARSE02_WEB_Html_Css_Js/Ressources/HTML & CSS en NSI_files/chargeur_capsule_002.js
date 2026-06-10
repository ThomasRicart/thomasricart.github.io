
/* 
   Appelle le script chargeur_capsule.js qui se trouvent dans le sous-dossier de la capsule en cours.
   Son rôle est de permettre d'insérer les scripts propres de la capsule après le chargement des dépendances par chareur.js 
  Il ne comporte aucune partie à modfier 
*/

( function ()
  {

      let scripts_communs = [
	      ["scripts/page.js",[
	          ["scripts/boite_onglet.js",[
		      ["scripts/accordeon.js",[]]
		  ]]
	      ]]];
      
      let scripts_du_module = [
	  ["chargeur_capsule.js",[]]
      ];


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
      
/*      
      function conf_js( chemin, modules)
      {
	  function ajoute_js ( url )
	  {
	      let objet_script = document.createElement("script");
	      objet_script.type = "text/javascript";
	      objet_script.src = url;
	      
	      document.head.appendChild(objet_script);   
	  }

	  for (i=0; i < modules.length; i++)
	  {
	      ajoute_js(chemin + modules[i]);
	  }	  
      }
  */    
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
	  
	  prefcomm = prefixecommun
	      
	  dossier_scripts = document.currentScript.src.slice(prefcomm.length,document.currentScript.src.lastIndexOf("/"))
	  
	  dossier_du_module = document.currentScript.baseURI.slice(prefcomm.length)

	  if (dossier_du_module.indexOf("/") != -1)
	  {
	  
	      dossier_du_module = dossier_du_module.slice(0,dossier_du_module.indexOf("/"))
	      
	      suffixe_du_module = dossier_du_module.slice("cours".length)
	      	
	      return ({'racine' : prefcomm,
		       'module' : dossier_du_module, 
		       'suffixe' : suffixe_du_module})
	      
	  }
	  else
	  {
	      return ({'racine' : prefcomm,
		       'module' : "", 
		       'suffixe' : ""})
	  }
      }

      chemin = trouve_les_chemins()
    
      if (chemin['module'].length > 0)  // on ne fait rien si on est dans l'index à la racine du squelette
      {
	  // scripts de la racine, communs à toutes les capsules
	  conf_js( chemin['racine'], scripts_communs)
	  // le chargeur de la capsule, dans son dossier scripts
	  conf_js( chemin['racine']+chemin['module']+"/scripts"+chemin['suffixe']+"/", scripts_du_module)
      }
      
  })();

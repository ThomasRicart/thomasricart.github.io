/* Nécessite JQuery et CodeMirror */

/* Script conçu par Nicolas Buyle-Bodin et amélioré par Jean-Manuel Meny sous licence Creative Commons BY-NC-SA */
/* Respect de la Paternité - Pas d'utilisation commerciale - Partage des conditions initiales à l'identique */

/* Préambule :
	Ces documents sont sous licence libre, modifiables et ré-utilisables à loisir.
	Ils ont demandé plusieurs centaines d'heures de travail et de conception.
	Merci de rappeler leur paternité originale si vous les ré-utilisez. */

$(function(){
	$(".contenu").hide();
	
	let boiteOnglets = document.getElementsByClassName("boite_onglets");
	
	for(let i = 0; i < boiteOnglets.length; i++)
	{
		let lesOnglets = boiteOnglets[i].getElementsByClassName("onglet");
		let lesContenus = boiteOnglets[i].getElementsByClassName("contenu");
	
		for(let j = 0; j < lesOnglets.length; j++)
		{
					let unOnglet = lesOnglets[j];
					let leContenu = lesContenus[j];
					
					$(unOnglet).click(
						function () {
							// Mettre tous les onglets non actifs
							$(".active").removeClass("active");
							
							// Mettre l'onglet cliqué actif
							$(this).addClass("active");
							
							// Cacher les boîtes de contenu
							for(let k = 0; k < lesContenus.length; k++) 
							{	
								let unContenu = lesContenus[k];
								if(k != j )
								{
									if($(unContenu).is(":visible")) {$(unContenu).hide();}
								}
							}
		 
							// Afficher la boîte de contenu associée
							$(leContenu).toggle();
							if (!($(leContenu).is(":visible")))
							{
								$(".active").removeClass("active");
							}
							
						});
		}
	};

	// Ajout section expérimentale : Bloquer les copier-coller de la correction pour forcer les
	// élèves à recopier à la main (c'est beaucoup plus formateur)
	// Actuellement valable pour les corrections HTML
	function alertCopy() {
		alert("Désolé, vous ne pouvez pas copier la correction. Essayez de la recopier à la main, c'est plus formateur ;)");
		return false;
	}
	$(".no-copy").bind('copy', alertCopy);
	$(".no-copy").bind('cut', alertCopy);

});

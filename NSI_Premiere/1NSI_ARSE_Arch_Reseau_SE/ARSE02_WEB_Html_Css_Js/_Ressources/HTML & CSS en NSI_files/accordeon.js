/* Nécessite JQuery et JQuery Auto Height Master */

/* Script conçu par Jean-Manuel Meny et Nicolas Buyle-Bodin sous licence Creative Commons BY-NC-SA */
/* Respect de la Paternité - Pas d'utilisation commerciale - Partage des conditions initiales à l'identique */

/* Préambule :
	Ces documents sont sous licence libre, modifiables et ré-utilisables à loisir.
	Ils ont demandé plusieurs centaines d'heures de travail et de conception.
	Merci de rappeler leur paternité originale si vous les ré-utilisez. */

$(function(){

	$('.titrePanneauHtml, .titrePanneauCss, .titrePanneauHtmlJS, .titrePanneauHtml_Non, .titrePanneauCss_Non').each(
		function(index){
 
			$('.titrePanneauHtml, .titrePanneauCss, .titrePanneauHtmlJS, .titrePanneauHtml_Non, .titrePanneauCss_Non').eq(index).click(function(){

					 $('.panneau').eq(index).toggle();
                         
			});	// fin fonction exécutée au clic
	});

});

$(function(){
	$('iframe').iframeAutoHeight({
					  debug: true,
					  /*minHeight: 200,*/
					  diagnostics: true,
					  animate: false,
					  heightOffset: 20
					 });

 
});


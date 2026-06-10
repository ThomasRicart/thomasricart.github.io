
function reponse_vocab_statistiques()
{
    let reponse_1 = document.getElementById("question_def1_1").value;
    let reponse_2 = document.getElementById("question_def1_2").value;
    let reponse_3 = document.getElementById("question_def1_3").value;
    let reponse_4 = document.getElementById("question_def1_4").value;

    if ((reponse_1 == "le caractère")&(reponse_2 == "un individu")&(reponse_3 == "la population")&(reponse_4 == "un échantillon")) {
        alert("Bonne réponse, bravo ! Tu as compris le vocabulaire précédent.");
    } else {
        alert("Essaie encore, attention à respecter l'orthographe et l'article attendu : \nN'hésite pas à copier-coller les mots écrits de l'énoncé. \nAttention à ne pas m'être d'espace final inutile !");
    } 
}

function reponse_frequence()
{
    let reponse = document.getElementById("question_def2").value;

    if ((reponse == "21491/153207")) {
        alert("Bonne réponse, bravo ! Tu as compris le calcul attendu pour une fréquence.");
    } else {
        if ((reponse == "0.14")||(reponse == "0.1403")||(reponse == "0.14027")) {
            alert("La valeur exacte est attendue :\nécrire la fraction avec le symbole /");
        } 
        else {
        alert("Essaie encore. \nAttention à écrire le calcul permettant d'obtenir la fréquence avec le symbole / \nN'hésite pas à copier-coller les valeurs écrits de l'énoncé. \nAttention à ne pas m'être d'espace inutile !");
            }
    } 
}

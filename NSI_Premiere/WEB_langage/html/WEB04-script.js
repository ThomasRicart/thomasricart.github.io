/**
 * Fonction de mise à jour du Dashboard
 * Cette fonction lit les inputs et modifie le DOM
 */
function mettreAJourDashboard() {
    // 1. Sélection des éléments sources (le formulaire)
    const inputPiece = document.getElementById("nom_piece");
    const curseurTemp = document.getElementById("consigne");

    // 2. Sélection de l'élément à modifier (le statut des capteurs)
    const affichageTemp = document.getElementById("valeur-temp");
    const titreHeader = document.querySelector("h1");

    // 3. Récupération des valeurs
    let nouvellePiece = inputPiece.value;
    let nouvelleTemp = curseurTemp.value;

    // 4. Application des modifications au DOM
    if (nouvellePiece !== "") {
        titreHeader.textContent = "Dashboard : " + nouvellePiece;
    }
    
    affichageTemp.textContent = nouvelleTemp;

    // 5. Modification du style selon la température (Bonus S40)
    if (nouvelleTemp > 25) {
        affichageTemp.style.color = "red";
        affichageTemp.style.fontWeight = "bold";
    } else {
        affichageTemp.style.color = "black";
        affichageTemp.style.fontWeight = "normal";
    }

    console.log("Mise à jour effectuée : " + nouvellePiece + " à " + nouvelleTemp + "°C");
}
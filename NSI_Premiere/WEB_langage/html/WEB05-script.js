/**
 * S41 - Dashboard Intelligent
 */
function mettreAJourDashboard() {
    // 1. Sélection des éléments
    const inputPiece = document.getElementById("nom_piece");
    const curseurTemp = document.getElementById("consigne");
    const affichageTemp = document.getElementById("valeur-temp");
    const titreHeader = document.querySelector("h1");
    
    // Nouveaux éléments S41
    const zoneCard = document.getElementById("card-temp");
    const iconeStatus = document.getElementById("icon-status");

    // 2. Récupération des valeurs
    let nouvellePiece = inputPiece.value;
    let nouvelleTemp = parseFloat(curseurTemp.value); // On s'assure que c'est un nombre

    // 3. Mise à jour des textes
    if (nouvellePiece !== "") {
        titreHeader.textContent = "Dashboard : " + nouvellePiece;
    }
    affichageTemp.textContent = nouvelleTemp;

    // 4. LOGIQUE CONDITIONNELLE (S41)
    
    // On retire d'abord les anciennes classes pour "nettoyer" la carte
    zoneCard.classList.remove("chaud", "froid");

    if (nouvelleTemp >= 26) {
        // État chaud
        zoneCard.classList.add("chaud");
        iconeStatus.textContent = "🔥";
    } 
    else if (nouvelleTemp <= 17) {
        // État froid
        zoneCard.classList.add("froid");
        iconeStatus.textContent = "❄️";
    } 
    else {
        // État normal
        iconeStatus.textContent = "✅";
    }

    console.log("Mise à jour effectuée à " + nouvelleTemp + "°C");
}

/**
 * Gère l'allumage et l'extinction visuelle du dashboard
 * @param {string} action - Reçoit 'allumer' ou 'eteindre'
 */
function gererLumiere(action) {
    const corpsPage = document.body;

    if (action === 'eteindre') {
        corpsPage.classList.add("mode-nuit");
        console.log("Lumières éteintes");
    } else {
        corpsPage.classList.remove("mode-nuit");
        console.log("Lumières allumées");
    }
}
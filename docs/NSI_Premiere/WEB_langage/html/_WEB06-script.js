/**
 * S42 - Logique Capteurs / Traitement / Actionneurs
 */

function mettreAJourDashboard() {
    // 1. CAPTEURS (Entrées)
    const inputPiece = document.getElementById("nom_piece");
    const curseur = document.getElementById("consigne");
    
    // 2. IHM & ACTIONNEURS (Sorties)
    const affichageTemp = document.getElementById("valeur-temp");
    const titre = document.getElementById("titre-principal");
    const zoneCard = document.getElementById("card-temp");
    const icone = document.getElementById("icon-status");
    const affichageVentilo = document.getElementById("etat-ventilo");

    const t = parseFloat(curseur.value);
    affichageTemp.textContent = t;

    // Mise à jour du titre
    if (inputPiece.value !== "") {
        titre.textContent = "Système : " + inputPiece.value;
    }

    // 3. TRAITEMENT (Boucle de décision)
    zoneCard.classList.remove("chaud", "froid");
    affichageVentilo.classList.remove("ventilo-on");

    if (t >= 26) {
        // Condition CHAUD -> Actionneur Ventilation ON
        zoneCard.classList.add("chaud");
        icone.textContent = "🔥";
        affichageVentilo.textContent = "EN MARCHE (Extraction air chaud)";
        affichageVentilo.classList.add("ventilo-on");
    } 
    else if (t <= 17) {
        // Condition FROID -> Actionneur Ventilation OFF
        zoneCard.classList.add("froid");
        icone.textContent = "❄️";
        affichageVentilo.textContent = "ARRÊT (Conservation chaleur)";
    } 
    else {
        // Condition NORMALE
        icone.textContent = "✅";
        affichageVentilo.textContent = "ARRÊT";
    }
}

/**
 * Commande Actionneur Lumière
 */
function gererLumiere(action) {
    if (action === 'eteindre') {
        document.body.classList.add("mode-nuit");
    } else {
        document.body.classList.remove("mode-nuit");
    }
}

/**
 * DÉFI S42 : Mode automatique (IHM pilotant les capteurs)
 */
function modeAutoConfort() {
    const curseur = document.getElementById("consigne");
    // On force la valeur du capteur à 21°C
    curseur.value = 21;
    // On déclenche manuellement la mise à jour du système
    mettreAJourDashboard();
    console.log("Mode Auto-Confort activé : cible 21°C");
}
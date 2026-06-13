#############################################################################
# Jeux de données fournis                                                   #
#############################################################################
from plantes import Plante, plantes
from mesures import mesures

#############################################################################
# Écrire le code de la fonction croissance_moyenne de la question 1         #
#############################################################################


def croissance_moyenne(plantes):
    if plantes == []:
        return None
    else:
        somme = 0
        for plante in plantes:
            somme = somme + plante.croissance
        return somme / len(plantes)

# Tests
assert croissance_moyenne([]) == None
assert croissance_moyenne([
    Plante("Basilic", "Ocimum basilicum", 60, 40, "plein soleil"),
    Plante("Tomate", "Solanum lycopersicum", 80, 100, "plein soleil")]) == 70


#############################################################################
# Écrire le code de la fonction dictionnaire_mesure de la question 2      #
#############################################################################

def dictionnaire_mesure(plantes, mesures):
    # Création du dictionnaire
    dico = {}
    for plante in plantes:
        dico[plante.nom] = []
    for mesure in mesures:
        dico[mesure["plante"]].append(mesure)
    return dico

# Test
assert dictionnaire_mesure([
    Plante("Basilic", "Ocimum basilicum", 60, 40, "plein soleil"),
    Plante("Tomate", "Solanum lycopersicum", 80, 100, "plein soleil")],
       [{'jour': 1, 'plante': 'Basilic', 'hauteur': 0.85, 'temperature': 29.3, 'humidite': 50.89},
         {'jour': 2, 'plante': 'Basilic', 'hauteur': 1.7, 'temperature': 17.44, 'humidite': 78.99}]) == {
             "Basilic":[{'jour': 1, 'plante': 'Basilic', 'hauteur': 0.85, 'temperature': 29.3, 'humidite': 50.89},
               {'jour': 2, 'plante': 'Basilic', 'hauteur': 1.7, 'temperature': 17.44, 'humidite': 78.99}],
     "Tomate":[]}


#############################################################################
# Fonction défaillante à analyser et corriger pour les questions 3 et 4     #
#############################################################################

def purger_mesures_extremes(liste_mesures):
    """
    Supprime de la liste toutes les mesures dont la température 
    n'est pas comprise entre 20 et 25°C inclus.
    """
    mesure_a_supp = []
    for mesure in liste_mesures:
        if mesure['temperature'] < 20 or mesure['temperature'] > 25:
            mesure_a_supp.append(mesure)
    for mesure in mesure_a_supp:
        liste_mesures.remove(mesure)


def test_purger():
    mesures_test = [
        {'jour': 1, 'plante': 'Basilic', 'temperature': 18.0},
        {'jour': 2, 'plante': 'Basilic', 'temperature': 19.0},
        {'jour': 3, 'plante': 'Basilic', 'temperature': 22.0},
        {'jour': 4, 'plante': 'Basilic', 'temperature': 28.0},
        {'jour': 5, 'plante': 'Basilic', 'temperature': 29.0}
    ]

    purger_mesures_extremes(mesures_test)

    print("Résultat après la purge :")
    for m in mesures_test:
        print(f"Jour {m['jour']} : {m['temperature']}°C")

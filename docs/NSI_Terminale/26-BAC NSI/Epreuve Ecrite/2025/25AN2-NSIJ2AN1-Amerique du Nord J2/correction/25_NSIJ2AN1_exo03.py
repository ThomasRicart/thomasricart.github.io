# Créé par thoma, le 23/05/2025 en Python 3.7

graphe_airinfo = {
    'W': {'P': 6},
    'P': {'W': 6, 'T': 10, 'S': 17},
    'B': {'T': 9},
    'T': {'B': 9, 'P': 10, 'S': 8},
    'S': {'P': 17, 'T': 8}
     }

def vol_direct(graphe, ville1, ville2):
    if ville1 not in graphe.keys() or ville2 not in graphe.keys():
        return False
    return ville2 in graphe[ville1].keys()


def liste_villes_proches(graphe, ville, d_max):
    villes_proches = []
    for voisine, distance in graphe[ville].items():
        if distance <= d_max:
            villes_proches.append(voisine)
    return villes_proches

graphe_droidevant = {
    'W': {'P': 6, 'B': 7},
    'P': {'W': 6, 'B': 1},
    'B': {'W': 7, 'P': 1},
    'T': {'S': 8},
    'S': {'T': 8}
    }


def parcours(graphe, visitees, ville):
    """Parcours d'un graphe à partir d'une ville non visitée,
    en ayant déjà visité un certain nombre de villes. """
    # Marque la ville comme visitée
    visitees.append(ville)
    # Parcourt les voisines de la ville
    for voisine in graphe[ville]:
        if voisine not in visitees:
            # Explore depuis les voisines non visitées
            parcours(graphe, visitees, voisine)

visitees1 = []
parcours(graphe_airinfo, visitees1, 'W')

visitees2 = []
parcours(graphe_droidevant, visitees2, 'W')

from random import randint

def ville_arbitraire(graphe):
    liste_sommets = [cle for cle in graphe.keys()]
    n = len(liste_sommets)
    choix = randint(0, n-1)
    return liste_sommets[choix]

for i in range(20):
    print(ville_arbitraire(graphe_airinfo))
def est_connexe(graphe):
    depart = ville_arbitraire(graphe)
    visitees = []                              # Ligne 4
    parcours(graphe, visitees, depart)
    return len(visitees) == len(graphe)        # Ligne 6


def mystere(graphe, ville, chemin, cout, arrivee):
    # ajoute la ville actuelle au chemin
    chemin = chemin + [ville]
    # si la ville courante est l'arrivée
    if ville == arrivee:
        # Affichage du chemin
        print(chemin, cout)
    # On scrute les choisins de la ville courante
    for voisins, poids in graphe[ville].items():
        # si ce voisin n'est déjà dans le chemin
        if voisins not in chemin:
            # appel récursif en ajoutant le poids de cette arete
            mystere(graphe, voisins, chemin, cout + poids, arrivee)
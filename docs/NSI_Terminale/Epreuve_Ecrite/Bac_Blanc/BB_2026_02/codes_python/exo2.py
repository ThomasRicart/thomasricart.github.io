from random import choice

graphe_airinfo = {
    'W': {'P': 6},
    'P': {'W': 6, 'T': 10, 'S': 17},
    'B': {'T': 9},
    'T': {'B': 9, 'P': 10, 'S': 8},
    'S': {'P': 17, 'T': 8}     }

# Question 18
assert graphe_airinfo['T']['P'] == 10

graphe_droidevant = {
    'W': {'P': 6, 'B': 7},
    'P': {'W': 6, 'B': 1},
    'B': {'W': 7, 'P': 1},
    'T': {'S': 8},
    'S': {'T': 8} }

# Question 19
def vol_direct(graphe, ville1, ville2):
    return ville2 in graphe[ville1].keys()
assert vol_direct(graphe_airinfo, 'T', 'B') == True
assert vol_direct(graphe_airinfo, 'W', 'B') == False

# Question 20
def liste_villes_proches(graphe, ville, d_max):
    liste = []
    for ville_voisine, distance in graphe[ville].items():
        if distance <= d_max:
            liste.append(ville_voisine)
    return liste
assert liste_villes_proches(graphe_airinfo, 'T', 7) == []
assert liste_villes_proches(graphe_airinfo, 'T', 9) == ['B', 'S']

def parcours(graphe, visitees, ville):
    """Parcours d'un graphe à partir d'une ville non visitée,
    en ayant déjà visité un certain nombre de villes."""
    visitees.append(ville)              # Marque la ville comme visitée
    for voisine in graphe[ville].keys():       # Parcourt les voisines de la ville
        if voisine not in visitees:
            # Explore depuis les voisines non visitées
            parcours(graphe, visitees, voisine)

# Question 23
visitees1 = []
parcours(graphe_airinfo, visitees1, 'W')
assert visitees1 == ['W', 'P', 'T', 'B', 'S']
visitees2 = []
parcours(graphe_droidevant, visitees2, 'W')
assert visitees2 == ['W', 'P', 'B']

def ville_arbitraire(graphe):
    return choice(list(graphe.keys()))

# Question 25
def est_connexe(graphe):
    depart = ville_arbitraire(graphe)
    visitees = []
    parcours(graphe, visitees, depart)
    return len(visitees) == len(graphe)

assert est_connexe(graphe_airinfo) == True
assert est_connexe(graphe_droidevant) == False

def mystere(graphe, ville, chemin, cout, arrivee):
    # Ajoute la ville actuelle au chemin
    chemin = chemin + [ville]
    if ville == arrivee:
        # Affiche le chemin et son coût total
        print(chemin, cout)
    # Parcourt les villes voisines et leurs poids
    for voisine, poids in graphe[ville].items():
        # Vérifie que la ville n'est pas déjà visitée
        if voisine not in chemin:
            mystere(graphe, voisine, chemin, cout + poids, arrivee)

# Question 26 à décommenter
#mystere(graphe_airinfo, 'W', [], 0, 'B')
    # ['W', 'P', 'T', 'B'] 25
    # ['W', 'P', 'S', 'T', 'B'] 40



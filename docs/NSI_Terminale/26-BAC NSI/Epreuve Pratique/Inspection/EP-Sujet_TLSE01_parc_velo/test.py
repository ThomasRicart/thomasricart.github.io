def somme_distances_trajets(trajets):
    ''' Renvoie la somme des distances parcourues '''
    if trajets == []:
        return 0
    trajet = trajets.pop()
    return 1 + somme_distances_trajets(trajets[1:])

trajets = [
    {'depart': 'Mairie', 'arrivee': 'Gare', 'distance': 2.8},
    {'depart': 'Gare', 'arrivee': 'Stade', 'distance': 1.6},
    {'depart': 'Mairie', 'arrivee': 'Stade', 'distance': 3.5},
    {'depart': 'Gare', 'arrivee': 'Université', 'distance': 2.2},
    {'depart': 'Parc', 'arrivee': 'Mairie', 'distance': 4.0},
    {'depart': 'Université', 'arrivee': 'Gare', 'distance': 2.0}
]

print(somme_distances_trajets(trajets))
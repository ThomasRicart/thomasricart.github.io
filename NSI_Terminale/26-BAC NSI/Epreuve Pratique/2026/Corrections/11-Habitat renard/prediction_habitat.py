from math import sqrt
from donnees_habitats import zones_connues

nouveau = {'vegetation': 5, 'proximite_eau': 2,
           'densite_urbaine': 4, 'disponibilite_proies': 6}


def distance(hab_1, hab_2):
    '''
    Calcule la distance euclidienne entre deux habitats.
    entrée : 
        - habitat_1 : dictionnaire représentant un habitat.
        - habitat_2 : dictionnaire représentant un autre habitat.
    sortie : 
        - float : distance euclidienne entre habitat_1 et habitat_2.
    '''
    # On calcule d'abord les carrés
    v = (hab_1['vegetation'] - hab_2['vegetation'])**2
    p = (hab_1['proximite_eau'] - hab_2['proximite_eau'])**2
    u = (hab_1['densite_urbaine'] - hab_2['densite_urbaine'])**2
    d = (hab_1['disponibilite_proies'] - hab_2['disponibilite_proies'])**2
    return sqrt(v + p + u + d)


def distance_d_un_habitat(habitat, habitats):
    '''
    Calcule la distance entre un habitat et chaque habitat de la liste.
    entrée : 
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) où distance est la distance entre habitat et chaque habitat de la liste.
    '''
    liste = []
    for habitat_2 in habitats:
        liste.append((distance(habitat, habitat_2), habitat_2))
    return liste


def premiere_composante(c):
    '''Fonction utilitaire renvoyant la première composante d'un tuple'''
    return c[0]


def k_plus_proches(k, habitat, habitats):
    '''
    Calcule les k habitats les plus proches de l'habitat donné.
    entrée : 
        - k : entier représentant le nombre d'habitats à retourner.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - list[tuple] : liste de tuples (distance, habitat) l'élément à l'indice 0 est la distance euclidienne entre habitat 
                        et chaque habitat de la liste et l'élément à l'indice 1 est le dictionnaire correspondant à l'habitat correspondant.
    '''
    # On calcule les distances
    distances = distance_d_un_habitat(habitat, habitats)
    # On cherche à trier les distances en fonction de la distance euclidienne.
    distances.sort(key=premiere_composante)
    # renvoie les distances jusque la borne k non comprise
    return distances[:k]


def presence_renard(k, habitat, habitats):
    '''
    Vérifie si l'habitat donné a plus de k/2 voisins avec des renards.
    entrée : 
        - k : entier représentant le nombre d'habitats à considérer.
        - habitat : dictionnaire représentant un habitat.
        - habitats : liste de dictionnaires représentant des habitats.
    sortie : 
        - bool : True si l'habitat a plus de k/2 voisins avec des renards, False sinon.
    '''
    habitats = k_plus_proches(k, habitat, habitats)
    n_renards = 0
    for habitat in habitats:
        distance = habitat[0]
        caracteristiques = habitat[1]
        if caracteristiques['presence_renard']:
            n_renards += 1
    return n_renards > k/2

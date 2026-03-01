def compter_elements(liste: list, valeur_cherchee) -> int:
    """
    Compte le nombre d'apparitions d'une valeur dans une liste.
    Itération sur les éléments.
    """
    compteur = 0
    for elt in liste:
        if elt == valeur_cherchee:
            compteur += 1
    return compteur

def compter_indices(liste: list, valeur_cherchee) -> int:
    """
    Compte le nombre d'apparitions d'une valeur dans une liste.
    Itération sur les indices.
    """
    compteur = 0
    for i in range(len(liste)):
        if liste[i] == valeur_cherchee:
            compteur += 1
    return compteur

# --- TESTS UNITAIRES ---
""" Fonction de test pour le comptage """
# Test 1 : Valeur présente plusieurs fois
assert compter_elements([1, 2, 1, 3, 1], 1) == 3
# Test 2 : Valeur absente
assert compter_elements([1, 2, 3], 5) == 0
# Test 3 : Liste vide
assert compter_elements([], 1) == 0

# Test version indices
assert compter_indices([1, 2, 1, 3, 1], 1) == 3
assert compter_indices([1, 2, 3], 5) == 0
assert compter_indices([], 1) == 0
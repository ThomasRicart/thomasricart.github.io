def somme_elements(liste: list)->int:
    """
    Calcule la somme des nombres d'une liste.
    Itération sur les elements.
    """
    total = 0
    # On parcourt la liste avec elt
    for elt in liste:
        # On ajoute l'élément elt
        total += elt
    return total

def somme_indices(liste: list)->int:
    """
    Calcule la somme des nombres d'une liste.
    Itération sur les indices (index).
    """
    total = 0
    # On parcourt de 0 à la longueur de la liste
    for i in range(len(liste)):
        # On ajoute l'élément situé à l'index i
        total += liste[i]
    return total

# --- TESTS UNITAIRES ---
""" Fonction de test de la fonction somme_indices """
assert somme_indices([1, 2, 3, 4]) == 10
assert somme_indices([100, 200]) == 300
assert somme_indices([]) == 0


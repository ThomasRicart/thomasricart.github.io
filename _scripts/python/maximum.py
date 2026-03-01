def maximum_elements(liste: list) -> int:
    """
    Recherche la valeur maximale d'une liste.
    Itération sur les éléments.
    """
    if not liste:
        return None

    # On initialise le maximum avec le premier élément
    max_val = liste[0]
    
    # On parcourt la liste avec elt
    for elt in liste:
        # Si l'élément est plus grand que le maximum actuel
        if elt > max_val:
            max_val = elt
    return max_val

def maximum_indices(liste: list) -> int:
    """
    Recherche la valeur maximale d'une liste.
    Itération sur les indices (index).
    """
    if not liste:
        return None

    max_val = liste[0]
    
    # On parcourt de 0 à la longueur de la liste
    for i in range(len(liste)):
        # On compare l'élément situé à l'index i
        if liste[i] > max_val:
            max_val = liste[i]
    return max_val

# --- TESTS UNITAIRES ---
""" Fonction de test pour la recherche de maximum """
assert maximum_elements([1, 5, 3, 2]) == 5
assert maximum_elements([-10, -2, -5]) == -2
assert maximum_elements([]) is None

assert maximum_indices([1, 5, 3, 2]) == 5
assert maximum_indices([-10, -2, -5]) == -2
assert maximum_indices([]) is None
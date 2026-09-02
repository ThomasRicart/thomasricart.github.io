def somme_indices(liste):
    """
    Calcule la somme des nombres d'une liste.
    Itération sur les indices (index).

    Args:
        liste (list): Une liste de nombres.

    Returns:
        number: La somme totale des éléments.
    """
    total = 0
    # On parcourt de 0 à la longueur de la liste
    for i in range(len(liste)):
        # On ajoute l'élément situé à l'index i
        total += liste[i]
    return total

# --- TESTS UNITAIRES ---
def test_somme_indices():
    assert somme_indices([1, 2, 3, 4]) == 10
    assert somme_indices([100, 200]) == 300
    assert somme_indices([]) == 0

# test_somme_indices()
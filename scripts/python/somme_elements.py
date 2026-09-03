def somme_elements(liste):
    """
    Calcule la somme des nombres d'une liste.
    Itération directe sur les éléments.

    Args:
        liste (list): Une liste de nombres (int ou float).

    Returns:
        number: La somme totale des éléments.
    """
    total = 0
    for nombre in liste:
        total += nombre
    return total

# --- TESTS UNITAIRES ---
def test_somme_elements():
    assert somme_elements([1, 2, 3, 4]) == 10
    assert somme_elements([10.5, 0.5, 2]) == 13.0
    assert somme_elements([-5, 5, 10]) == 10
    assert somme_elements([]) == 0  # Cas limite : liste vide

# test_somme_elements()
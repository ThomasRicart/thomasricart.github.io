def est_present_indices(liste, valeur_cherchee):
    """
    Vérifie si une valeur est présente dans une liste donnée.
    Itération sur les indices (index)

    Args:
        liste (list): La liste d'éléments dans laquelle effectuer la recherche.
        valeur_cherchee: La valeur (nombre, chaîne, etc.) à trouver.

    Returns:
        bool: True si la valeur est trouvée, False sinon.
    """
    # On parcourt les indices de 0 à la taille de la liste - 1
    for i in range(len(liste)):
        # On accède à l'élément via son index [i]
        if liste[i] == valeur_cherchee:
            return True
    return False

# --- TESTS UNITAIRES (Asserts) ---
def test_est_present_indices():
    """ Fonction de test de la fonction est_present_indices """
    # Test 1 : Valeur présente au milieu
    assert est_present_indices([10, 20, 30, 40], 30) == True
    # Test 2 : Valeur absente
    assert est_present_indices([10, 20, 30, 40], 50) == False
    # Test 3 : Valeur présente au tout début (cas limite)
    assert est_present_indices(["BTS", "CIEL", "Maths"], "BTS") == True
    # Test 4 : Liste vide (cas limite)
    assert est_present_indices([], 1) == False
    # Test 5 : Recherche dans une chaîne
    assert est_present_indices("Automatisme", "a") == True

# à décommenter pour tester la fonction
# test_est_present_indices()

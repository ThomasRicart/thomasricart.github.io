def est_present_elements(liste, valeur_cherchee):
    """
    Vérifie si une valeur est présente dans une liste donnée.
    Itération sur les éléments

    Args:
        liste (list): La liste d'éléments dans laquelle effectuer la recherche.
        valeur_cherchee: La valeur (nombre, chaîne, etc.) à trouver.

    Returns:
        bool: True si la valeur est trouvée, False sinon.
    """
    for element in liste:
        if element == valeur_cherchee:
            return True
    return False

# --- TESTS UNITAIRES (Asserts) ---
def test_est_present_elements():
    """ Fonction de test de la fonction est_prensent """
    # Test 1 : Valeur présente au milieu
    assert est_present_elements([10, 20, 30, 40], 30) == True
    # Test 2 : Valeur absente
    assert est_present_elements([10, 20, 30, 40], 50) == False
    # Test 3 : Valeur présente au tout début (cas limite)
    assert est_present_elements(["BTS", "CIEL", "Maths"], "BTS") == True
    # Test 4 : Liste vide (cas limite)
    assert est_present_elements([], 1) == False
    # Test 5 : Recherche d'un caractère dans une chaîne (Python traite les chaînes comme des listes)
    assert est_present_elements("Automatisme", "a") == True

# à décommenter pour tester la fonction
# test_est_present_elements()
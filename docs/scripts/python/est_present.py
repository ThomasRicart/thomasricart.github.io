def est_present_elements(liste: list, valeur_cherchee: int)->bool:
    """
    Vérifie si une valeur est présente dans une liste donnée.
    Itération sur les éléments
    """
    for element in liste:
        if element == valeur_cherchee:
            return True
    return False

def est_present_indices(liste: list, valeur_cherchee: int)->bool:
    """
    Vérifie si une valeur est présente dans une liste donnée.
    Itération sur les indices (index)
    """
    # On parcourt les indices de 0 à la taille de la liste - 1
    for i in range(len(liste)):
        # On accède à l'élément via son index [i]
        if liste[i] == valeur_cherchee:
            return True
    return False


# --- TESTS UNITAIRES (Asserts) ---
""" Fonction de test de la fonction est_present_elements """
# Test 1 : Valeur présente au milieu
assert est_present_elements([10, 20, 30, 40], 30) == True
# Test 2 : Liste vide (cas limite)
assert est_present_elements([], 1) == False
# Test 3 : Recherche d'un caractère dans une chaîne (Python traite les chaînes comme des listes)
assert est_present_elements("Automatisme", "a") == True

# --- TESTS UNITAIRES (Asserts) ---
""" Fonction de test de la fonction est_present_indices """
# Test 4 : Valeur présente au milieu
assert est_present_indices([10, 20, 30, 40], 30) == True
# Test 5 : Liste vide (cas limite)
assert est_present_indices([], 1) == False
# Test 6 : Recherche dans une chaîne
assert est_present_indices("Automatisme", "a") == True


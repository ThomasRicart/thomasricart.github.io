def recherche_dichotomique(liste: list, valeur_cherchee: int) -> int:
    """
    Recherche une valeur dans une liste TRIÉE par dichotomie.
    Renvoie l'indice de la valeur si trouvée, sinon None.
    Complexité : O(log n)
    """
    debut = 0
    fin = len(liste) - 1
    
    while debut <= fin:
        # Calcul de l'indice du milieu (division entière)
        milieu = (debut + fin) // 2
        
        if liste[milieu] == valeur_cherchee:
            return milieu  # Valeur trouvée
        elif liste[milieu] < valeur_cherchee:
            # La valeur est dans la partie droite
            debut = milieu + 1
        else:
            # La valeur est dans la partie gauche
            fin = milieu - 1
            
    return None  # Valeur non trouvée

# --- TESTS UNITAIRES ---
""" Fonction de test pour la recherche dichotomique """
liste_triee = [1, 3, 5, 7, 9, 11, 13]

assert recherche_dichotomique(liste_triee, 7) == 3   # Indice de 7 est 3
assert recherche_dichotomique(liste_triee, 1) == 0   # Début
assert recherche_dichotomique(liste_triee, 13) == 6  # Fin
assert recherche_dichotomique(liste_triee, 4) is None # Absent
assert recherche_dichotomique([], 1) is None         # Liste vide

def tri_selection(liste: list) -> list:
    """
    Trie une liste en place selon l'algorithme du tri par sélection.
    """
    n = len(liste)
    
    for i in range(n):
        # On suppose que le minimum est à l'indice i
        min_idx = i
        
        # On cherche le vrai minimum dans le reste de la liste
        for j in range(i + 1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        
        # Si on a trouvé un élément plus petit, on échange
        if min_idx != i:
            liste[i], liste[min_idx] = liste[min_idx], liste[i]
            
    return liste

# --- TESTS UNITAIRES ---
""" Fonction de test pour le tri par sélection """
l1 = [64, 25, 12, 22, 11]
tri_selection(l1)
assert l1 == [11, 12, 22, 25, 64]

assert tri_selection([]) == []

def tri_bulle(liste: list) -> list:
    """
    Trie une liste en place selon l'algorithme du tri à bulles.
    """
    n = len(liste)
    
    # On parcourt la liste n fois
    for i in range(n):
        # Optimisation : on vérifie si un échange a eu lieu
        echange_effectue = False
        
        # Les i derniers éléments sont déjà en place
        for j in range(0, n - i - 1):
            # Si l'élément est plus grand que le suivant, on échange
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                echange_effectue = True
        
        # Si aucun échange n'a été fait, la liste est déjà triée
        if not echange_effectue:
            break
            
    return liste

# --- TESTS UNITAIRES ---
""" Fonction de test pour le tri à bulles """
l1 = [5, 1, 4, 2, 8]
tri_bulle(l1)
assert l1 == [1, 2, 4, 5, 8]

assert tri_bulle([3, 2, 1]) == [1, 2, 3]

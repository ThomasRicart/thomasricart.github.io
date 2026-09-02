def tri_insertion(liste: list) -> list:
    """
    Trie une liste en place selon l'algorithme du tri par insertion.
    """
    # On commence à l'indice 1 car l'élément 0 est considéré comme déjà trié
    for i in range(1, len(liste)):
        cle = liste[i]
        j = i - 1
        
        # Décalage des éléments plus grands que la clé vers la droite
        while j >= 0 and liste[j] > cle:
            liste[j + 1] = liste[j]
            j -= 1
        
        # Insertion de la clé à sa place
        liste[j + 1] = cle
        
    return liste

# --- TESTS UNITAIRES ---
""" Fonction de test pour le tri par insertion """
l1 = [5, 2, 4, 6, 1, 3]
tri_insertion(l1)
assert l1 == [1, 2, 3, 4, 5, 6]

l2 = [10, -2, 0]
tri_insertion(l2)
assert l2 == [-2, 0, 10]

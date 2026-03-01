def fusion(gauche: list, droite: list) -> list:
    """
    Fusionne deux listes triées en une seule liste triée.
    """
    resultat = []
    i, j = 0, 0
    
    # Tant que les deux listes contiennent des éléments
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    
    # On ajoute les éléments restants (s'il y en a)
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    
    return resultat

def tri_fusion(liste: list) -> list:
    """
    Trie une liste selon l'algorithme du tri fusion (récursif).
    Renvoie une NOUVELLE liste triée (ne modifie pas l'originale en place).
    """
    # Cas de base : liste vide ou à 1 élément est déjà triée
    if len(liste) <= 1:
        return liste
    
    # Division
    milieu = len(liste) // 2
    partie_gauche = liste[:milieu]
    partie_droite = liste[milieu:]
    
    # Appels récursifs
    gauche_triee = tri_fusion(partie_gauche)
    droite_triee = tri_fusion(partie_droite)
    
    # Fusion
    return fusion(gauche_triee, droite_triee)

# --- TESTS UNITAIRES ---
""" Fonction de test pour le tri fusion """
assert tri_fusion([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
assert tri_fusion([]) == []
assert tri_fusion([1]) == [1]

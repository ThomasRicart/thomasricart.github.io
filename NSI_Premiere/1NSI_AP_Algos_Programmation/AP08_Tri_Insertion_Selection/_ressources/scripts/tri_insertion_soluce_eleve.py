def tri_insertion(liste):
    for i in range(len(liste)-1):
        k = i + 1           # indice de la clé
        cle = liste[k]      # récuperation de la clé
        while cle < liste[k-1] and k > 0:   # verif position de la clé
            decalage_valeurs(liste,k)
            k = k - 1                       # Décalage suivant
        liste[k] = cle      # placement de la clé au bon endroit
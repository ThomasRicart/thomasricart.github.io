def tri_insertion(liste):
    for i in range(len(liste)-1):
        k = i + 1           # indice de la clé
        cle = liste[k]      # récuperation de la clé
        while cle < liste[k-1] and k > 0:   # vérif position de la clé
            liste[k] = liste[k-1]           # décalage a droite
            k = k - 1                       # Décalage suivant
        liste[k] = cle      # placement de la clé au bon endroit

liste = [3,8,1,13,4,21,5,2]
tri_insertion(liste)
assert liste == [1, 2, 3, 4, 5, 8, 13, 21]
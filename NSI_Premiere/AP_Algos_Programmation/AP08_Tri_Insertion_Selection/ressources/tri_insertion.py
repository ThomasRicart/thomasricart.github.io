# Créé par Thomas, le 01/06/2024 en Python 3.7
def tri_insertion(L):
    n = len(L)
    for i in range(1, n):
        k = i                               # Indice de la clé
        # Tant que le bord de la liste n'est pas atteint
        # ET que le suivant est plus petit que le précédent
        while k > 0 and L[k] < L[k-1]:
            L[k-1], L[k] = L[k], L[k-1]     # Echange des deux éléments
            k = k - 1                       # La clé se déplace vers la gauche

L = [6, 5, 4, 3, 2, 1]
tri_insertion(L)
print(L)


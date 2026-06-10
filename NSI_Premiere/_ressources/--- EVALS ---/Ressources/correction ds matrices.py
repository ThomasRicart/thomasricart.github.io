L = [[1,4,5,3],[-6,3,2,1],[6,4,8,9]]
### Question 1 et 2
n = len(L)          # Nombre de lignes
m = len(L[0])       # Nombre de colonnes (matrice rectangulaire)

### Question 3
L[2][3] = 3
assert L == [[1, 4, 5, 3], [-6, 3, 2, 1], [6, 4, 8, 3]]

L.append([1,5,6,8])
assert L == [[1, 4, 5, 3], [-6, 3, 2, 1], [6, 4, 8, 3], [1, 5, 6, 8]]

L[1].append(5)
assert L == [[1, 4, 5, 3], [-6, 3, 2, 1, 5], [6, 4, 8, 3], [1, 5, 6, 8]]

### Question 4
L = [[1,4,5,3],[-6,3,2,1],[6,4,8,9]]
print(L[2][0])

### Question 5
def affiche_valeur(L):
    for SL in L:
        for elt in SL:
            print(elt,end=" ")

### Question 6
def recherche_minimum(L):
    minimum = [0,0,L[0][0]]
    n = len(L)
    for i in range(n):
        m = len(L[i])
        for j in range(m):
            if L[i][j] < minimum[2]:
                minimum[2] = L[i][j]
                minimum[0] = i
                minimum[1] = j
    return minimum

assert recherche_minimum(L) == [1,0,-6]

### Question 7
L2 = [[5,8,9],[2,4,3],[1,6,7]]
def addition_colonne(L):
    liste_sommes = []
    for j in range(3):
        somme = 0
        for i in range(3):
            somme = somme + L2[i][j]
        liste_sommes.append(somme)
    return liste_sommes

assert addition_colonne(L2) == [8,18,19]



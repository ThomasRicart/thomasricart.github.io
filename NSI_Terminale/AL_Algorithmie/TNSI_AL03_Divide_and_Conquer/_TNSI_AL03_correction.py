### Exercice 1 - Recherche dichotomique - version impérative
def recherche_dicho_imperative(tab: list, val: int) -> bool:
    ''' Renvoie True si val est dans tab
    tab est une liste triee
    recherche dichotomique
    version imperative '''
    i_deb = 0
    i_fin = len(tab) - 1
    while i_deb < i_fin:
        i_mil = (i_fin + i_deb)//2
        if tab[i_mil] == val:
            return True
        if tab[i_mil] > val:
            i_fin = i_mil - 1
        else:
            i_deb = i_mil + 1
    return False

def verif_exo1():
    tab = [2, 3, 4, 6, 7, 8]
    print(recherche_dicho_imperative(tab, 4), 'attendu: True')
    print(recherche_dicho_imperative(tab, 5), 'attendu: False')

### Exercice 2 - Recherche dichotomique - version récursive
def recherche_dicho_rec(L: list, val: int) -> bool:
    ''' Renvoie True si val est dans tab
    tab est une liste triee
    recherche dichotomique
    version recursive '''
    if len(L) == 0:
        return False
    return L.pop() == val or recherche_dicho_rec(L, val)

def verif_exo2():
    tab = [2, 3, 4, 6, 7, 8]
    print(recherche_dicho_rec(tab, 4), 'attendu: True')
    print(recherche_dicho_rec(tab, 5), 'attendu: False')

### Exercice 3 - Recherche dans une liste non triee
def recherche(L: list, val: int) -> bool:
    ''' Renvoie True si val est dans tab
    tab est une liste
    version recursive '''
    pass

def verif_exo3():
    tab = [2, 3, 4, 6, 7, 8]
    print(recherche_dicho_rec(tab, 4), 'attendu: True')
    print(recherche_dicho_rec(tab, 5), 'attendu: False')

### Exercice 4 - Division
def division(L: list) -> tuple:
    ''' Renvoie la liste coupée en deux en deux sous listes
    sortie: tuple de listes '''

def verif_exo4():
    L1 = [1, 4, 6, 15]
    L2 = [3, 9, 10]
    print(division(L1), 'attendu: ([1, 4], [6, 15])')
    print(division(L2), 'attendu: ([3], [9, 10])')
    print(division([1]), 'attendu: ([] , [1])')

### Exercice 5 - Fusion
def fusion(L1, L2, L = None):
    ''' Fusionne deux listes L1 et L2 triées
    version récursive '''
    if L == None:
        L = []
    return fusion_rec(L1, L2, L)
def fusion_rec(L1, L2, L):
    if L1 == [] or L2 == []:
        return L + L1 + L2
    if L1[0] < L2[0]:
        e = L1.pop(0)
    else:
        e = L2.pop(0)
    L = L + [e]
    return fusion_rec(L1, L2, L)

def verif_exo5():
    L1 = [1, 3, 4]
    L2 = [0, 2, 5, 6]
    print(fusion(L1, L2))


### Exercice 6 - Tri fusion
def tri_fusion(L):
    ''' Renvoie la liste L triée '''
    n = len(L)
    if n < 2:
        return L
    else:
        L1, L2 = division(L)
        L1 = tri_fusion(L1)
        L2 = tri_fusion(L2)
        return fusion(L1, L2)

### Exercice 9 - rechercher de maximum
def maximum(L):
    if len(L) == 1:
        return L[0]
    return max(maximum(L[:len(L)//2]), maximum(L[len(L)//2:]))
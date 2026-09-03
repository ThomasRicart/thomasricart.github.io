# Exercice 1
def fonc1(a,b):
    if a < b:
        return b - a
    else:
        return a * b
assert fonc1(4,3) == 12     # Sujet A
assert fonc1(3,4) == 1      # Sujet A
assert fonc1(2,3) == 1      # Sujet B
assert fonc1(3,2) == 6      # Sujet B

# Exercice 2
def fonc2(n):
    a = 1
    for i in range(n):
        a = a * 2
    return a
assert fonc2(4) == 16     # Sujet A
assert fonc2(3) == 8      # Sujet B

# Exercice 3
def fonc3(une_liste):
    a = 0
    for elt in une_liste:
        a = a + elt
    return a
assert fonc3([1,3,4,6]) == 14     # Sujet A
assert fonc3([1,2,4,6]) == 13     # Sujet B

# Exercice 4
def fonc4(une_liste):
    n = len(une_liste)
    sortie = []
    for i in range(n):
        if une_liste[i] % 2 == 0:
            sortie.append(i)
    return sortie
assert fonc4([1,3,4,6]) == [2,3]     # Sujet A
assert fonc4([1,2,4,6]) == [1,2,3]   # Sujet B

# Exercice 5
def fonc5(n):
    a = 10
    while n > 0:
        a = a + 1
        n = n - 1
    return a
assert fonc5(6) == 16     # Sujet A
assert fonc5(5) == 15     # Sujet B

# Exercice 6 - SUJET A
def recherche_maximum(une_liste):
    maximum = une_liste[0]
    for elt in une_liste:
        if elt > maximum:
            maximum = elt
    return maximum
ma_liste= [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert recherche_maximum(ma_liste) == 9

# Exercice 6 - SUJET B
def recherche_minimum(une_liste):
    minimum = une_liste[0]
    for elt in une_liste:
        if elt < minimum:
            minimum = elt
    return minimum
ma_liste= [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert recherche_minimum(ma_liste) == 1

# Exercice 7 - SUJET A
def somme_liste_pairs(une_liste):
    somme_pairs = 0
    for elt in une_liste:
        if elt % 2 == 0:
            somme_pairs= somme_pairs + elt
    return somme_pairs
ma_liste = [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert somme_liste_pairs(ma_liste) == 18

# Exercice 7 - SUJET B
def somme_liste_impairs(une_liste):
    somme_impairs = 0
    for elt in une_liste:
        if elt % 2 != 0:
            somme_impairs= somme_impairs + elt
    return somme_impairs
ma_liste = [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert somme_liste_impairs(ma_liste) == 20


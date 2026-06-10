### DS02A - CORRECTION
# Exercice 1
def f(a,b):
    if a < b:
        return a
    else :
        return b
assert f(7,3) == 3

# Exercice 2
def f(x):
    for i in range(6):
        x = x + i
    return x
assert f(2) == 17

# Exercice 3
mon_tuple = (1 ,6 ,7 ,3 ,2)
def f(un_tuple : tuple ):
    a = 0
    for elt in un_tuple :
        a = a + elt
    return a
assert f(mon_tuple) == 19

# Exercice 4
def f(x):
    i = 0
    a = 0
    while i < x:
        a = a + 2
        i = i + 1
    return a
assert f(3) == 6

# Exercice 5
def f(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i , end = " ")
f(7)    # 0 2 4 6

# Exercice 6
def recherche_minimum_I(une_liste):
    n = len(une_liste)
    minimum = une_liste[0]
    for i in range(1,n):
        if une_liste[i] < minimum:
            minimum = une_liste[i]
    return minimum
ma_liste = [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert recherche_minimum_I(ma_liste) == 1

def recherche_minimum_E(une_liste):
    minimum = une_liste[0]
    for elt in une_liste:
        if elt < minimum:
            minimum = elt
    return minimum
ma_liste = [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert recherche_minimum_E(ma_liste) == 1

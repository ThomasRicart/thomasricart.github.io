### DS02A - CORRECTION
# Exercice 1
def f(a,b):
    if a < b:
        return a
    else :
        return b
assert f(3,7) == 3

# Exercice 2
def f(x):
    for i in range(6):
        x = x + i
    return x
assert f(1) == 16

# Exercice 3
mon_tuple = (1 ,6 ,8 ,3 ,2)
def f(un_tuple : tuple ):
    a = 0
    for elt in un_tuple :
        a = a + elt
    return a
assert f(mon_tuple) == 20

# Exercice 4
def f(x):
    i = 0
    a = 0
    while i < x:
        a = a + 3
        i = i + 1
    return a
assert f(3) == 9

# Exercice 5
def f(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i , end = " ")
f(9)    # 0 2 4 6 8

# Exercice 6
def recherche_maximum_I(une_liste):
    n = len(une_liste)
    maximum = une_liste[0]
    for i in range(1,n):
        if une_liste[i] > maximum:
            maximum = une_liste[i]
    return maximum
ma_liste = [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert recherche_maximum_I(ma_liste) == 9

def recherche_maximum_E(une_liste):
    maximum = une_liste[0]
    for elt in une_liste:
        if elt > maximum:
            maximum = elt
    return maximum
ma_liste = [3 ,6 ,8 ,1 ,9 ,4 ,7]
assert recherche_maximum_E(ma_liste) == 9

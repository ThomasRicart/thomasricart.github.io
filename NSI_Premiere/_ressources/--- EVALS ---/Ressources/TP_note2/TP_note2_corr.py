from random import *

### Exercice 2
def plus_petit(k,T):
    '''
    Renvoie une liste, dans l'ordre des k plus petits éléments de T
    '''
    liste_plus_petits = []
    for i in range(k):
        n = len(T)
        mini = T[0]
        for j in range(n):
            if T[j] < mini:
                mini = T[j]
        liste_plus_petits.append(mini)
        T.remove(mini)
    return liste_plus_petits

T = [5,7,1,4,3,9,0,-2]
liste_plus_petits = plus_petit(3,T)
#assert liste_plus_petits == [-2,0,1,3]

### Exercice 3
def bulle(tab,i):
    '''
    Cette fonction ne renvoie rien
    Modifie la liste en place et
    fait remonter le plus grand élément de tab jusqu'à l'indice i
    '''
    j = 0
    while j < i:
        if tab[j] > tab[j+1]:
            tab[j] , tab[j+1] = tab[j+1] , tab[j]
        j = j + 1
liste = [4,8,15,7,3]
'''
bulle(liste,4)
assert liste == [4,8,7,3,15]
La plus grande valeur est remontée jusqu'à l'indice 4]
'''

def rand_list(n):
    '''
    Renvoie une liste de n entiers aléatoires entre
    1 et 100 inclus
    '''
    liste_aleatoire = [randint(1,100) for i in range(n)]
    return liste_aleatoire

def tri2(tab):
    '''
    Cette fonction ne renvoie rien
    Fonction de tri suivant la méthode citée au début de l'exo 3
    '''

    #pass    # à commenter
    n = len(tab)
    for i in range(len(tab)):
        bulle(tab[0:n-i],n-i-1)
    return tab
tab = [4,2,6,1,-3,9,0]
'''
tri2(tab)
assert tab == [-3,0,1,2,4,6,9]
'''


### TP NOTE 1
### Exercice 1
### Complexité linéaire O(n)
t = [4,3,2,1]
for i in range(len(t)-1):
    if t[i] > t[i+1]:
        t[i] , t[i+1] = t[i+1] , t[i]

assert t == [3, 2, 1, 4]

### Exercice 2
### Complexité quadratique O(n**2)
t = [1,4,2,3]
for i in range(len(t)):
    for j in range(i):
        print(t[j],end=" ")
''' Affichage 1 1 4 1 4 2 '''

### Exercice 3
### Complexité lineaire O(n)
### Au début de la liste
def recherche_lineaire(liste,valeur):
    n = len(liste)
    for i in range(n):
        if liste[i] == valeur:
            return i
    return False

### Exercice 4
def recherche_dichotomique(L:list,valeur:int)->bool:
    ''' Algorithme de recherche dichotomique '''
    i_deb = 0                           #3
    i_fin = len(L) - 1                  #4
    while i_fin - i_deb >= 0:           #5
        i_cen = (i_deb + i_fin) // 2    #6
        if L[i_cen] == valeur:          #7
            return True                 #8
        elif valeur > L[i_cen]:         #9
            i_deb = i_cen + 1           #10
        else:                           #11
            i_fin = i_cen - 1           #12
    return False                        #13





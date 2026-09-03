def recherche_dichotomique(L:list,valeur:int)->bool:
    i_deb = 0
    i_fin = len(L) - 1
    while i_fin - i_deb >= 0:
        i_cen = (i_deb + i_fin) // 2
        if L[i_cen] == valeur:
            # return True
            return i_cen
        elif valeur > L[i_cen]:
            i_deb = i_cen + 1
        else:
            i_fin = i_cen - 1
    return False

def f(x)->int:
    y = x**3 - x**2 - x - 2
    return y
def g(x):
    y = 3*x**3 - x**2 - x - 2
    return y

##########################################################
##### Zone à compléter en enlevant les commentaires ######
##########################################################

### Question 1

def creation_abscisses(a:int,b:int)->list:
    liste_abscisses = [i for i in range(a,b+1)]
    return liste_abscisses

assert creation_abscisses(-3,3) == [-3, -2, -1, 0, 1, 2, 3]

### Question 2

def creation_ordonnees(abscisses:list,fonction):
    liste_ordonnees = [fonction(abs) for abs in abscisses]
    return liste_ordonnees

assert creation_ordonnees([-3,-2,-1,0,1,2,3],f) == [-35,-12,-3,-2,-3,0,13]
assert creation_ordonnees([-3,-2,-1,0,1,2,3],g) == [-89,-28,-5,-2,-1,16,67]


### Question 4

def recherche_zero(a:int,b:int,fonction)->int:
    abscisses = creation_abscisses(a,b)
    ordonnees = creation_ordonnees(abscisses,fonction)
    indice_zero = recherche_dichotomique(ordonnees,0)
    return indice_zero

assert recherche_zero(-3,3,f) == 5

### Question 5
def recherche_valeur(a:int,b:int,fonction,valeur):
    abscisses = creation_abscisses(a,b)
    ordonnees = creation_ordonnees(abscisses,fonction)
    indice_zero = recherche_dichotomique(ordonnees,valeur)
    return indice_zero

def recherche_dichotomique2(L:list,valeur:int)->int:
    i_deb = 0
    i_fin = len(L) - 1
    while i_fin - i_deb >= 0:
        i_cen = (i_deb + i_fin) // 2
        if L[i_cen] == valeur:
            # return True
            return i_cen
        elif valeur > L[i_cen]:
            i_deb = i_cen + 1
        else:
            i_fin = i_cen - 1
    return i_fin





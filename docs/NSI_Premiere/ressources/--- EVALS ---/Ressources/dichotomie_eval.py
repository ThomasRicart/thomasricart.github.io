def recherche_dichotomique(L:list,valeur:int)->bool:
    i_deb = 0
    i_fin = len(L) - 1
    while i_fin - i_deb >= 0:
        i_cen = (i_deb + i_fin) // 2
        if L[i_cen] == valeur:
            return True
        elif valeur > L[i_cen]:
            i_deb = i_cen + 1
        else:
            i_fin = i_cen - 1
    return False

def recherche_dichotomique_bis(L:list,valeur:int)->bool:
    i_deb = 0
    i_fin = len(L) - 1
    while i_fin - i_deb >= 0:
        i_cen = (i_deb + i_fin) // 2
        if L[i_cen] == valeur:
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

def creation_abscisses(a,b):
    liste_abscisses = []
    for i in range(a,b+1):
        liste_abscisses.append(a)
        a = a + 1
    return liste_abscisses

assert creation_abscisses(-3,3) == [-3, -2, -1, 0, 1, 2, 3]

def creation_ordonnees(abscisses,fonction):
    liste_ordonnees = []
    for elt in abscisses:
        liste_ordonnees.append(fonction(elt))
    return liste_ordonnees

assert creation_ordonnees([-3,-2,-1,0,1,2,3],f) == [-35,-12,-3,-2,-3,0,13]
assert creation_ordonnees([-3,-2,-1,0,1,2,3],g) == [-89,-28,-5,-2,-1,16,67]

def recherche_zero(a:int,b:int,fonction)->list:
    abscisses = creation_abscisses(a,b)
    ordonnees = creation_ordonnees(abscisses,fonction)
    recherche = recherche_dichotomique_bis(ordonnees,0)
    return recherche

assert recherche_zero(-3,3,f) == 5
abscisses = creation_abscisses(-5,5)
ordonnees = creation_ordonnees(abscisses,f)
print(ordonnees)
ordonnees = creation_ordonnees(abscisses,g)
print(ordonnees)





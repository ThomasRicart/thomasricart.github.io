def f(h):
    ''' Fonction renvoyant la flottabilité en fonction de h
    In:
        h --> float
    Out:
        flottabilite --> float '''
    flottabilite = -h**3 + 6.3*h**2 - 25.93
    return flottabilite

def make_abs(a,b,p):
    ''' Fonction renvoyant une liste de valeurs comprises entre
    a et b inclus par pas de 10**(-p)
    In:
        a,b: float
        p: int précision (nombre de chiffres après le virgule
    Out:
        liste_abs --> list'''
    liste_abs = []
    while a <= b:
        liste_abs.append(a)
        a = round(a + 10**(-p),p)
    return liste_abs

def make_ord(f,liste_abs,p):
    ''' Fonction renvoyant une liste de valeurs correspondant à f(h)
    In:
        f: fonction
        liste_abs: list contenant les abscisses des points
        p: int précision
    Out:
        liste_ord --> list'''
    liste_ord = []
    for elt in liste_abs:
        liste_ord.append(round(f(elt),p))
    return liste_ord

def recherche_h0(liste_ord,p):
    i_deb = 0
    i_fin = len(liste_ord) - 1
    while liste_ord[i_deb] * liste_ord[i_fin] < 0:

    return i_deb,i_fin

a = 0
b = 4.2
p = 2
liste_abs = make_abs(a,b,p)
liste_ord = make_ord(f,liste_abs,p)
#print(liste_abs)
#print(liste_ord)
val = recherche_h0(liste_ord,p)
print(val)
print(f(val[0]),f(val[1]))

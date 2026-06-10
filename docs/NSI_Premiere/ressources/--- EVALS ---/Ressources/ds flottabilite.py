def f(h,p):
    flottabilite = -h**3 + 6.3*h**2 - 25.93
    return round(flottabilite,p)

def creation_abscisses(a,b,p):
    ''' creation d'une liste de valeurs comprises entre a et b inclus
    par pas de 10^(-p)'''
    liste_absc = []
    while a <= b:
        liste_absc.append(a)
        a = round(a + 10**(-p),p)
    return liste_absc

def creation_ordonnees(abscisses,f,p):
    '''
    abscisses: liste contenant les abscisses h
    f: fonction utilisée dans notre exercice
    '''
    liste_ord = []
    for elt in abscisses:
        liste_ord.append(f(elt,p))
    return liste_ord

a = 0
b = 4.2
p = 4
abs = creation_abscisses(a,b,p)
ord = creation_ordonnees(abs,f,p)

def recherche_equilibre(f,p):
    ''' Fonction recherchant la valeur h_0
    correspondant à l'équilibre du navire
    0 <= h <= 4.2
    Renvoie un encadrement de h_0 par deux valeurs
    a et b telles que b-a=precision
    '''

    a = 0
    b = 4.2
    liste_abs = creation_abscisses(a,b,p)


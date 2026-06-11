def dernier(n):
    collier = [True for i in range(n)]        # Ligne 2
    indice = 0
    collier[indice] = False
    for etape in range(n-1):
        nb_bonbons_vus = 0
        while nb_bonbons_vus < 3:             # Ligne 7
            indice += 1
            if indice >= n:                   # Ligne 9
                indice = 0
            if collier[indice]:               # Ligne 11
                nb_bonbons_vus += 1
        collier[indice] = False               # Ligne 13
    return indice

class File:
    def __init__(self):
        self.file = []

    def est_vide(self):
        return len(self.file) == 0

    def enfile(self, x):
        self.file.append(x)

    def defile(self):
        return self.file.pop(0)

    def affiche(self):
        sortie = ''
        for elt in self.file:
            sortie += str(elt) + ' '
        sortie = '(Tête) ' + sortie + '(Queue)'
        print(sortie)

f = File()
f.enfile(0)
f.enfile(1)
#print(f.affiche())

f = File()
for x in [0, 1, 2, 3, 4]:
    f.enfile(x)
f.defile()
f.enfile(f.defile())
f.enfile(f.defile())
#print(f.affiche())

def dernier_file(n):
    f = File()
    for i in range(n):
        f.enfile(i)
    f.defile()
    while not f.est_vide():
        # Défiler 2 bonbons et les remettre
        for _ in range(2):
            if not f.est_vide():
                bonbon_defile = f.defile()
                f.enfile(bonbon_defile)
        # Manger le 3ème bonbon
        if not f.est_vide():
            dernier = f.defile()
            if f.est_vide():
                return dernier
    return dernier

print(dernier_file(8))


class Bonbon:
    def __init__(self, valeur):
        self.pred = None
        self.valeur = valeur
        self.succ = None

zero = Bonbon(0)
un = Bonbon(1)
deux = Bonbon(2)

zero.succ = un
un.pred = zero

un.succ = zero
deux.pred = un

deux.succ = zero
zero.pred = deux

a = zero.succ.valeur
b = un.succ.succ.pred.valeur

def creer_collier(n):
    # Création du premier bonbon
    premier = Bonbon(0)
    actuel = premier
    for i in range(1, n):
        # création du nouveau bobon
        nouveau = Bonbon(i)           # Ligne 5
        # on accroche les successeurs et predecesseurs
        actuel.succ = nouveau         # Ligne 6
        nouveau.pred = actuel         # Ligne 7
        # on se déplace dans le collier
        actuel = nouveau
    # on referme le collier
    actuel.succ = premier             # Ligne 9
    premier.pred = actuel             # Ligne 10
    return premier

bonbon = Bonbon(3)
bonbon.pred = bonbon
bonbon.succ = bonbon


premier = creer_collier(4)
premier.pred.succ = premier.succ
premier.succ.pred = premier.pred
bonbon = premier.succ

def dernier_chaine(n):
    bonbon = creer_collier(n)
    while bonbon.succ != bonbon:              # Ligne 3
        bonbon.pred.succ = bonbon.succ        # Ligne 4
        bonbon.succ.pred = bonbon.pred        # Ligne 5
        bonbon = bonbon.succ.succ.succ        # Ligne 6
    return bonbon.valeur
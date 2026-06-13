import random

class Salle:
    def __init__(self, nom):
        ''' Constructeur de la classe Salle
        nom (str)
        '''
        self.nom = nom
        self.tresor = random.randint(1, 20)
        self.pieces_suivantes = []

    def ajouter_porte(self, autre_salle):
        ''' Ajoute une porte à une salle
        self et autre_salle sont liées '''
        ### A compléter ###############
        ### Supprimer la ligne pass
        pass
        #####################

    def __repr__(self):
        return f'Salle {self.nom}: trésor = {self.tresor}'

def test_classe_salle():
    A = Salle('A')
    B = Salle('B')
    C = Salle('C')
    D = Salle('D')
    A.ajouter_porte(B)

class Donjon:
    ''' Constructeur de la classe Donjon
    salles (dict) clé: nom, valeur : Salle(nom) '''
    def __init__(self):
        self.salles = {}
        self.entree = None

    def ajouter_salle(self, nom):
        # A Ecrire
        salle_a_ajouter = Salle(nom)
        self.salles[nom] = salle_a_ajouter
        if self.entree is None:
            self.entree = salle_a_ajouter
        return salle_a_ajouter

    def relier(self, nom1, nom2):
        self.salles[nom1].ajouter_porte(self.salles[nom2])

    def parcourir_largeur(self):
        # A compléter
        visites = []
        file = [self.entre]
        total = 0

        while file:
            salle = file.pop(0)             # dépile le premier élément
            if salle not in visites:        # si la salle est non visitée
                visites.append(salle)       # ajouter la salle aux salles visitées
                total += salle.tresor       # ajout du trésor trouvé
                # for voisin in .................
                # ................................
                for voisin in salle.pieces_suivantes:
                    file.append(voisine)    # ajout des voisins non visités dans la file
        return total

    def parcourir_largeur_init(self):
        ''' Parcours du donjon en largeur d'abord '''
        file = [self.entree]        # File des salles à visiter
        visites = []                # Liste des salles visitées
        total = 0                   # Trésor total
        return self.parcourir_largeur_rec(file, visites, total)

    def parcourir_largeur_rec(self, file = None, visites = None, total = 0):
        if not file:                # Plus de salles à visiter
            return total
        salle = file.pop(0)         # Observation de la prochaine salle à visiter
        if salle not in visites:    # Si la salle n'est pas encore visitée
            visites.append(salle)   # Ajout de la salle dans les salles visitées
            total += salle.tresor   # Ajout du trésor de la salle

            for v in salle.pieces_suivantes:    # pour chaque voisin de la salle
                if v not in visites:            # si elle n'est pas encore visitée
                    file.append(v)              # l'ajouter à la file à visiter

        return self.parcourir_largeur_rec(file, visites, total) # Appel récursif

##    def parcourir_largeur_rec(self, file=None, visites=None, total=0):
##        if not file:                # Plus de salles à visiter
##            return total
##
##        salle = file.pop(0)         # Observation de la prochaine salle à visiter
##
##        # ⚠️ Erreur subtile : la salle est ajoutée aux visites APRÈS avoir ajouté ses voisines
##        total += salle.tresor       # Ajout du trésor de la salle
##
##        for v in salle.pieces_suivantes:    # Pour chaque voisin de la salle
##            if v not in visites:            # Si elle n'est pas encore visitée
##                file.append(v)              # L'ajouter à la file à visiter
##
##        visites.append(salle)               # <-- Mauvais ordre : trop tard
##
##        return self.parcourir_largeur_rec(file, visites, total)

    def max_or_methode(self, n):
        visites = []
        salle = self.entree
        return self.max_or_methode_rec(n, salle, visites)
    def max_or_methode_rec(self, n, salle, visites):
        if n == 1:
            return salle.tresor
        visites.append(salle)
        meilleur = salle.tresor

        for voisine in salle.pieces_suivantes:
            if voisine not in visites:
                total = salle.tresor + self.max_or_methode_rec(n-1, voisine, visites[:])
                if total > meilleur:
                    meilleur = total
        return meilleur


def max_or(donjon, n):
        visites = []
        salle = donjon.entree
        return max_or_rec(donjon, n, salle, visites)
def max_or_rec(donjon, n, salle, visites):

        if n == 1:
            return salle.tresor

        visites.append(salle)
        meilleur = salle.tresor

        for voisine in salle.pieces_suivantes:
            if voisine not in visites:
                total = salle.tresor + max_or_rec(donjon, n-1, voisine, visites[:])
                if total > meilleur:
                    meilleur = total
        return meilleur

def generer_donjon(nb_salles = 6):
    d = Donjon()
    noms = [chr(65+i) for i in range(nb_salles)]
    for nom in noms:
        d.ajouter_salle(nom)

    for _ in range(nb_salles * 2):
        a, b = random.sample(noms, 2)
        d.relier(a, b)
    return d

D1 = generer_donjon()

class Route:
    def __init__(self, nom, nb_vehicules = 0):
        ''' Contructeur de la classe Route '''
        self.nom = nom
        self.nb_vehicules = nb_vehicules
        self.feu = Feu('Vert')

    def ajouter_vehicules(self, n):
        ''' Ajoute un nombre n (int) de vehicules à la route
        n peut être négatif
        le nombre de véhicule ne peut jamais etre strictement négatif
        '''
        self.nb_vehicules = self.nb_vehicules + n
        if self.nb_vehicules < 0:
            self.nb_vehicules = 0

    def ajouter_feu(self, couleur):
        ''' Ajoute un feu à la route '''
        self.feu = Feu(couleur)

class Feu:
    def __init__(self, couleur):
        ''' Contructeur de la classe Feu '''
        self.couleur = couleur
        self.couleur_suivante = {'Rouge': 'Vert', 'Vert': 'Orange', 'Orange': 'Rouge'}

# ----------------------------------------------------------
# Question 1 : méthode passer_suivant
# ----------------------------------------------------------
    def passer_suivant(self):
        ''' Méthode permettant de faire passer le feu à la couleur suivante '''
        ### PARTIE A COMPLETER ###

        ###########################


class Carrefour:
    def __init__(self, routes):
        ''' Contructeur de classe Carrefour '''
        self.routes = routes    # liste de routes (de classe Route)

# ----------------------------------------------------------
# Question 2 : méthode route_max
# ----------------------------------------------------------
    def route_max(self):
        ''' Renvoie la route (de type Route) dont le nombre de véhicules est maximal '''
        ### PARTIE A COMPLETER ###

        ###########################

# ----------------------------------------------------------
# Question 3 : méthode adapter_circulation
# ----------------------------------------------------------
    def adapter_circulation(self):
        ''' permet d'adapter la circulation:
        - détermination de la route prioritaire
        - passage au vert de la route prioritaire
        - passage d'un véhicule sur cette route
        - passage au rouge des autres routes
        '''
        route_prioritaire = self.route_max()
        for r in self.routes:
            if route_prioritaire == r.nom:
                r.feu.couleur = "Vert"
                r.ajouter_vehicules(-1)
            else:
                r.feu.couleur = 'Rouge'

# ----------------------------------------------------------
# Question 4 : méthode récursive
# ----------------------------------------------------------
    def passage_voitures(self):
        nb_voitures_total = 0
        ### PARTIE A COMPLETER ###

        ###########################

        if self.routes == [] or nb_voitures_total == 0:
            return None
        return self.passage_voitures_rec(nb_voitures_total)

    def passage_voitures_rec(self, nb_vehicules_total):
        if nb_vehicules_total == 0:
            return None

        ### PARTIE A COMPLETER ###
        ### Adaptation de la circulation

        ###########################

        print('route prioritaire: ', r_max.nom, 'voitures restantes: ', nb_vehicules_total)

        ### PARTIE A COMPLETER ###
        ### Appel récursif

        ###########################


# Création des routes
R1 = Route('R1')
R2 = Route('R2')
R3 = Route('R3')

# Création des feux sur les routes
R1.ajouter_feu('Rouge')
R2.ajouter_feu('Vert')
R3.ajouter_feu('Rouge')

# Ajout des vehicules sur les routes
R1.ajouter_vehicules(4)
R2.ajouter_vehicules(2)
R3.ajouter_vehicules(6)

# Création du carrefour
C = Carrefour([R1, R2, R3])

def test_classe_feu():
    F1 = Feu('Vert')
    print(F1.couleur)   # Vert
    F1.passer_suivant()
    print(F1.couleur)   # Orange
    F1.passer_suivant()
    print(F1.couleur)   # Rouge
    F1.passer_suivant()
    print(F1.couleur)   # Vert
# test_classe_feu()

def test_methode_route_max():
    R1 = Route('R1', 7)
    R2 = Route('R2', 10)
    R3 = Route('R3', 6)
    C = Carrefour([R1, R2, R3])
    route_prio = C.route_max()
    print(route_prio.nom)       # R2
# test_methode_route_max()

def test_adapter_circulation():
    R1 = Route('R1', 7)
    R2 = Route('R2', 10)
    R3 = Route('R3', 6)
    C = Carrefour([R1, R2, R3])
    C.adapter_circulation()
    print(f'R1: {R1.nb_vehicules} véhicules. Feu: {R1.feu.couleur}')
    # Attendu: 7 véhicules, feu Rouge
    print(f'R2: {R2.nb_vehicules} véhicules. Feu: {R2.feu.couleur}')
    # Attendu: 9 véhicules, feu Vert
    print(f'R3: {R3.nb_vehicules} véhicules. Feu: {R3.feu.couleur}')
    # Attendu: 6 véhicules, feu Rouge

def test_methode_passage_voiture():
    R1 = Route('R1', 7)
    R2 = Route('R2', 10)
    R3 = Route('R3', 6)
    C = Carrefour([R1, R2, R3])
    C.passage_voitures()
#test_methode_passage_voiture()

# ----------------------------------------------------------
# Classe Route
# ----------------------------------------------------------
class Route:
    def __init__(self, nom, couleur, nb_vehicules):
        ''' Contructeur de la classe Route
        nom (str)
        nb_vehicules (int)
        '''
        self.nom = nom
        self.nb_vehicules = nb_vehicules
        self.feu = Feu(couleur)

    def ajouter_vehicules(self, n):
        ''' Ajoute un nombre n (int) de vehicules à la route
        n peut être négatif
        le nombre de véhicule ne peut jamais etre strictement négatif
        '''
        self.nb_vehicules = self.nb_vehicules + n
        if self.nb_vehicules < 0:
            self.nb_vehicules = 0

# ----------------------------------------------------------
# Classe Feu
# ----------------------------------------------------------
class Feu:
    def __init__(self, couleur):
        ''' Contructeur de la classe Feu
        couleur (str)
        '''
        self.couleur = couleur
        self.couleur_suivante = {'Rouge': 'Vert', 'Vert': 'Orange', 'Orange': 'Rouge'}

    def passer_suivant(self):
        ''' Méthode permettant de faire passer le feu à la couleur suivante '''
        # -------------------------------------------------------
        # Question 1
        # -------------------------------------------------------
        ### PARTIE A COMPLETER ###
        self.couleur = self.couleur_suivante[self.couleur]
        ###########################

# ----------------------------------------------------------
# Classe Carrefour
# ----------------------------------------------------------
class Carrefour:
    def __init__(self, routes):
        ''' Contructeur de classe Carrefour
        routes: liste (list) de Route
        '''
        self.routes = routes

    def route_max(self):
        ''' Renvoie la route (de type Route) dont le nombre de véhicules est maximal '''
        # -------------------------------------------------------
        # Question 2
        # -------------------------------------------------------
        ### PARTIE A COMPLETER ###
        r_max = self.routes[0]
        for route in self.routes:
            if route.nb_vehicules > r_max.nb_vehicules:
                r_max = route
        return r_max
        ###########################

    def adapter_circulation(self):
        ''' permet d'adapter la circulation:
        - détermination de la route prioritaire
        - passage au vert de la route prioritaire
        - passage d'un véhicule sur cette route
        - passage au rouge des autres routes
        '''
        # -------------------------------------------------------
        # Question 3
        # -------------------------------------------------------
        ### PARTIE A CORRIGER ###
        route_prioritaire = self.route_max()
        for r in self.routes:
            #if route_prioritaire == r.nom:
            if route_prioritaire.nom == r.nom:
                r.feu.couleur = "Vert"
                r.ajouter_vehicules(-1)
            else:
                r.feu.couleur = 'Rouge'
        ###########################

    def passage_voitures(self):
        # Calcule le nombre de voitures total sur toutes les routes du carrefour
        nb_voitures_total = 0
        for r in self.routes:
            nb_voitures_total = nb_voitures_total + r.nb_vehicules
        if self.routes == [] or nb_voitures_total == 0:
            return None
        return self.passage_voitures_rec(nb_voitures_total)

    def passage_voitures_rec(self, nb_vehicules_total):
        # A compléter
        if nb_vehicules_total == 0:
            return None
        # -------------------------------------------------------
        # Question 4
        # -------------------------------------------------------
        ### PARTIE A COMPLETER ###
        ### Zone 1
        nb_vehicules_total -= 1
        r_max = self.route_max()
        self.adapter_circulation()
        ###
        print('route prioritaire: ', r_max.nom, 'voitures restantes: ', nb_vehicules_total)
        ### Zone 2
        return self.passage_voitures_rec(nb_vehicules_total)
        ###
        ###########################




# -------------------------------------------------------
# Zone de test
# -------------------------------------------------------

# Création des routes
R1 = Route('R1', 'Rouge', 4)
R2 = Route('R2', 'Vert', 2)
R3 = Route('R3', 'Rouge', 6)

# Création du carrefour
C = Carrefour([R1, R2, R3])

def test_classe_feu():
    R1.feu.passer_suivant()
    print(f'Couleur du feu de R1 {R1.feu.couleur}')
    print('Couleur attendue: Vert')
    R1.feu.passer_suivant()
    print(f'Couleur du feu de R1 {R1.feu.couleur}')
    print('Couleur attendue: Orange')
    R1.feu.passer_suivant()
    print(f'Couleur du feu de R1 {R1.feu.couleur}')
    print('Couleur attendue: Rouge')
#test_classe_feu()

def test_methode_route_max():
    route_prioritaire = C.route_max()
    print(f'La route prioritaire est la route {route_prioritaire.nom}')
    print('Route attendue: R3')
#test_methode_route_max()

def test_methode_adapter_circulation():
    C.adapter_circulation()
    print('----------- Adaptation de la circulation --------------')
    print(f'{R1.nom} est la route avec {R1.nb_vehicules} véhicules dont le feu est {R1.feu.couleur}')
    print('Résultat attendu: 4 véhicules / Feu Rouge')
    print('-------------------------------------------------------')
    print(f'{R2.nom} est la route avec {R2.nb_vehicules} véhicules dont le feu est {R2.feu.couleur}')
    print('Résultat attendu: 2 véhicules / Feu Rouge')
    print('-------------------------------------------------------')
    print(f'{R3.nom} est la route avec {R3.nb_vehicules} véhicules dont le feu est {R3.feu.couleur}')
    print('Résultat attendu: 5 véhicules / Feu Vert')
    print('-------------------------------------------------------')
#test_methode_adapter_circulation()

def test_passage_voitures():
    R1 = Route('R1', 'Rouge', 4)
    R2 = Route('R2', 'Vert', 2)
    R3 = Route('R3', 'Rouge', 6)
    C = Carrefour([R1, R2, R3])

    C.passage_voitures()

#test_passage_voitures()
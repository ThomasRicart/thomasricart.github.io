import csv

# ----------------------------------------------------------
# Question 1 : Lecture du fichier CSV
# ----------------------------------------------------------
def lire_trajets(nom_fichier):
    """
    Lit le fichier CSV et renvoie une liste de dictionnaires.
    Chaque dictionnaire contient :
    'depart', 'arrivee', 'duree', 'date', 'dist'
    """
    trajets = []
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        lecteur = csv.reader(f)
        for ligne in lecteur:
            trajet = {}
            trajet['depart'] = ligne[0]
            ### PARTIE A COMPLETER ###



            ###########################
    return trajets

# ----------------------------------------------------------
# Question 2 : Trajet le plus long
# ----------------------------------------------------------
def trajet_le_plus_long(liste_trajets):
    """
    Renvoie a date du trajet le plus long en km
    """
    ### PARTIE A MODIFIER ET COMPLETER ###
    date_trajet_plus_long = None



    ###########################

    return date_trajet_plus_long

# ----------------------------------------------------------
# Question 3 : Somme des distances
# ----------------------------------------------------------
def somme_distances_trajets(trajets):
    ''' Renvoie la somme des distances parcourues '''
    ### PARTIE A MODIFIER ###
    if trajets == []:
        return 0
    trajet = trajets.pop()
    return 1 + somme_distances_trajets(trajets[1:])
    ###########################

# ----------------------------------------------------------
# Question 4 : Classe Trajet
# ----------------------------------------------------------

class Trajet:
    def __init__(self, depart, arrivee, duree, date, distance):
        ''' Contructeur de la classe Trajet '''
        self.depart = depart
        self.arrivee = arrivee
        self.duree = duree
        self.date = date
        self.distance = distance
        self.suivant = None

    def set_suivant(self, trajet_suivant):
        ''' affecte à l'attribut suivant
        le trajet 'trajet_suivant'  de type Trajet       '''
        self.suivant = trajet_suivant

#--- Réponse Question 4.1.
### Les trois trajets sont T1, T2 et T3
liste_trajets = [
    {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 12, 'date': '2025-10-01', 'dist': 2.8},
    {'depart': 'Gare', 'arrivee': 'Stade', 'duree': 8, 'date': '2025-10-01', 'dist': 1.6},
    {'depart': 'Stade', 'arrivee': 'Lac', 'duree': 10, 'date': '2025-10-01', 'dist': 2.3}
    ]

### PARTIE A MODIFIER et COMPLETER ###
T1 = None
T2 = None
T3 = None

#--- Réponse Question 4.2.
### PARTIE A COMPLETER ###


#--- Réponse Question 4.3.
def distance_totale(T):
    ''' Renvoie la distance totale parcourue par un vélo à partir du trajet T '''
    ### PARTIE A MODIFIER et COMPLETER ###
    pass
    ######################################


# ----------------------------------------------------------
# Listes de trajets de test --- Ne pas modifier
# ----------------------------------------------------------

trajets_test = [
    {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 12, 'date': '2025-10-01', 'dist': 2.8},
    {'depart': 'Gare', 'arrivee': 'Stade', 'duree': 8, 'date': '2025-10-01', 'dist': 1.6},
    {'depart': 'Université', 'arrivee': 'Gare', 'duree': 10, 'date': '2025-10-02', 'dist': 2.3},
    {'depart': 'Mairie', 'arrivee': 'Stade', 'duree': 15, 'date': '2025-10-02', 'dist': 3.5},
    {'depart': 'Gare', 'arrivee': 'Parc', 'duree': 9, 'date': '2025-10-03', 'dist': 4.2},
    {'depart': 'Parc', 'arrivee': 'Mairie', 'duree': 7, 'date': '2025-10-03', 'dist': 1.3},
    {'depart': 'Mairie', 'arrivee': 'Université', 'duree': 14, 'date': '2025-10-04', 'dist': 3.1},
    {'depart': 'Stade', 'arrivee': 'Gare', 'duree': 11, 'date': '2025-10-04', 'dist': 2.5},
    {'depart': 'Gare', 'arrivee': 'Musée', 'duree': 13, 'date': '2025-10-05', 'dist': 3.0},
    {'depart': 'Marché', 'arrivee': 'Mairie', 'duree': 9, 'date': '2025-10-05', 'dist': 2.0}
    ]

trajets_test2 = [
    {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 12, 'date': '2025-10-01', 'dist': 2.8},
    {'depart': 'Gare', 'arrivee': 'Stade', 'duree': 8, 'date': '2025-10-01', 'dist': 1.6},
    {'depart': 'Stade', 'arrivee': 'Lac', 'duree': 10, 'date': '2025-10-01', 'dist': 2.3}
    ]

# ----------------------------------------------------------
# Protocoles de tests --- Décommenter les tests
# ----------------------------------------------------------

def test_question1():
    trajets_importes = lire_trajets('trajets.csv')
    print('-------- Test nombre de trajets présents --------')
    print(f'nombre de trajets dans le fichier: {len(trajets_importes)}')
    print(f'valeur attendue: 40')
    print('-------- Test première valeur importée --------')
    print(f'premier trajet dans le fichier: {trajets_importes[0]}')
    print("valeur attendue: {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 12, 'date': '2025-10-01', 'dist': 2.8}")

#test_question1()

def test_question2():
    trajets = trajets_test
    print('-------- Test date du trajet le plus long --------')
    print(f'Trajet le plus long de trajets_test: {trajet_le_plus_long(trajets)}')
    print("valeur attendue: 2025-10-03")
#test_question2()

def test_question3():
    trajets = trajets_test
    print('-------- Test somme des distances parcourues --------')
    print(f'Somme des distances de trajets_tests: {somme_distances_trajets(trajets)}')
    print("valeur attendue: 26.3")

#test_question3()

def test_question41(T1, T2, T3):
    print('-------- Test Création de trajets --------')
    print(f'départ de T1: {T1.depart} -- valeur attendue: Mairie')
    print(f'départ de T2: {T2.depart} -- valeur attendue: Gare')
    print(f'date de T3: {T3.date} -- valeur attendue: 2025-10-01')
    print(f'arrivée de T2: {T2.arrivee} -- valeur attendue: Stade')
    print(f'durée de T1: {T1.duree} -- valeur attendue: 12')
#test_question41(T1, T2, T3)

def test_question42(T):
    print('-------- Test Enchainement des trajets --------')
    print(f'{T.depart} -- valeur attendue: Mairie')
    print(f'{T.suivant.depart} -- valeur attendue: Gare')
    print(f'{T.suivant.suivant.depart} -- valeur attendue: Stade')
    print(f'{T.suivant.suivant.suivant} -- valeur attendue: None')

#test_question42(T1)

def test_question43(T):
    print('-------- Test distance totale à partir du trajet T --------')
    print(f'{distance_totale(T)} -- valeur attendue: 6.7')

#test_question43(T1)


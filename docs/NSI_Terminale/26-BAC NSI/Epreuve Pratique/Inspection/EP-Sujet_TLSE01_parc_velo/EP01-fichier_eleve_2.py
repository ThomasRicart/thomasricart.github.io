import csv

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

trajets_anomalie = [{'depart':'Mairie','arrivee':'Gare','duree':10,'date':'2025-10-01','dist':1.5},
                    {'depart':'Stade','arrivee':'Université','duree':8,'date':'2025-10-01','dist':1.0},
                    {'depart':'Gare','arrivee':'Stade','duree':12,'date':'2025-10-02','dist':3.5}]

trajets_test2 = [
    {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 12, 'date': '2025-10-01', 'dist': 2.8},
    {'depart': 'Gare', 'arrivee': 'Stade', 'duree': 8, 'date': '2025-10-01', 'dist': 1.6},
    {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 10, 'date': '2025-10-02', 'dist': 2.3}
    ]
trajets_test3 = [
    {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 12, 'date': '2025-10-01', 'dist': 2.3},
    {'depart': 'Gare', 'arrivee': 'Stade', 'duree': 8, 'date': '2025-10-01', 'dist': 1.6},
    {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 10, 'date': '2025-10-02', 'dist': 2.3}
    ]

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
            ### PARTIE A COMPLETER ###
            ### Supprimer la ligne pass
            pass
            ###########################
    return trajets

def test_lire_trajets():
    trajets_importes = lire_trajets('trajets.csv')
    print('-------- Test nombre de trajets présents --------')
    print(f'nombre de trajets dans le fichier: {len(trajets_importes)}')
    print(f'valeur attendue: 40')
    print('-------- Test première valeur importée --------')
    print(f'premier trajet dans le fichier: {trajets_importes[0]}')
    print("valeur attendue: {'depart': 'Mairie', 'arrivee': 'Gare', 'duree': 12, 'date': '2025-10-01', 'dist': 2.8}")
#test_lire_trajets()

# ----------------------------------------------------------
# Question 2 : Station la plus fréquentée
# ----------------------------------------------------------
def station_plus_frequentee(liste_trajets):
    """
    Renvoie le nom de la station la plus utilisée
    (départ ou arrivée confondus).
    """
    ### PARTIE A COMPLETER ###
    ### Supprimer la ligne pass
    pass
    ###########################

def test_station_plus_frequentee():
    print('-------- Test Station la plus fréquentée --------')
    print(f'station la plus fréquentée:  {station_plus_frequentee(trajets_test)}')
    print('valeur attendue: Gare')

#test_station_plus_frequentee()

# ----------------------------------------------------------
# Question 3 : Moyenne de distance par jour + anomalies
# ----------------------------------------------------------
def analyse_par_jour(liste_trajets):
    """
    Calcule la distance moyenne parcourue par jour
    et affiche un avertissement si la moyenne du jour < 2 km.
    """

    # Étape 1 : regroupement des distances par jour
    distances_par_jour = {}
    for trajet in liste_trajets:
        jour = trajet['date']
        if jour not in distances_par_jour.keys():
            distances_par_jour[jour] = [trajet['dist']]
        else:
            distances_par_jour[jour].append(trajet['dist'])

    # Étape 2 : calcul des moyennes par jour
    moyennes = {}
    for jour in distances_par_jour.keys():
        moyenne = sum(distances_par_jour[jour]) / len(distances_par_jour[jour])
        moyennes[jour]= moyenne

    # Étape 3 : détection d’activité anormale
    ### PARTIE A COMPLETER ###

    ###########################
    return moyennes

def test_analyse_par_jour():
    print('-------- Test sur liste trajet_test --------')
    print(f'analyse par jour: {analyse_par_jour(trajets_test)}')
    print("valeur attendue: {'2025-10-01': 2.2, '2025-10-02': 2.9, '2025-10-03': 2.75, '2025-10-04': 2.8, '2025-10-05': 2.5}")
    print('-------- Test sur liste trajet_anomalie --------')
    print(f'analyse par jour: {analyse_par_jour(trajets_anomalie)}')
    print('valeur attendue: Activité anormale le 2025-10-01')
#test_analyse_par_jour()

# ----------------------------------------------------------
# Question 4 : Somme des distances des trajets
# ----------------------------------------------------------
def somme_distances_trajets(trajets):
    """
    Renvoie la somme des distances parcourues
    """
    if trajets == []:
        return 0
    trajet = trajets.pop()
    return 1 + somme_distances_trajets(trajets[1:])

def test_somme_distances_trajets():
    print('-------- Test sur la somme des distances des trajets --------')
    print(f'somme des distances des différents trajets: {somme_distances_trajets(trajets_test)}')
    print('valeur attendue: 26.3')
#test_somme_distances_trajets()

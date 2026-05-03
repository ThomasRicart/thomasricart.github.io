import datetime

def date_future(nb_jours):
    """Renvoie la date située nb_jours après aujourd'hui"""
    return datetime.date.today() + datetime.timedelta(days=nb_jours)

# Variable contenant les délais en jours pour chaque niveau (index 0 à 4)
DELAIS = [1, 3, 7, 15, 30]

class Carte:
    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse
        self.niveau = 0
        # À la création, la carte est à réviser le jour même
        self.date_prochaine = datetime.date.today()

    def __repr__(self):
        return f"<Carte: {self.question} (Niveau {self.niveau})>"

    #############################################################################
    # Écrire la méthode traiter_reponse(self, succes) de la question 1          #
    #############################################################################
    def traiter_reponse(self, succes):
        if succes:
            if self.niveau < 4:
                self.niveau += 1
        else:
            self.niveau = 0

        delaisProchain = DELAIS[self.niveau]
        self.date_prochaine = date_future(delaisProchain)


# Des cartes et un paquet de cartes pour réaliser des tests
c1 = Carte("Capitale de l'Italie ?", "Rome")
c1.niveau = 2
c1.date_prochaine = date_future(4)
c2 = Carte("7 x 8 ?", "56")
c2.date_prochaine = date_future(1)
c3 = Carte("Symbole du Fer ?", "Fe")
c3.date_prochaine = date_future(7)

paquet = [c1, c2, c3]

def test_q1():

    # exemples de tests possibles:
    print("=== TESTS traiter_reponse ===")

    # Test 1 : succès → niveau augmente
    print("\nTest 1 : succès")
    print("Avant :", c1)
    c1.traiter_reponse(True)
    print("Après :", c1)
    print("Date prochaine :", c1.date_prochaine)

    # Test 2 : échec → retour à 0
    print("\nTest 2 : échec")
    print("Avant :", c1)
    c1.traiter_reponse(False)
    print("Après :", c1)
    print("Date prochaine :", c1.date_prochaine)

    # Test 3 : plafond niveau 4
    print("\nTest 3 : plafond niveau 4")
    c1.niveau = 4
    print("Avant :", c1)
    c1.traiter_reponse(True)
    print("Après :", c1)  # doit rester à 4

    # Test 4 : vérification délai
    print("\nTest 4 : délai cohérent")
    c2.niveau = 1
    print("Avant :", c2)
    c2.traiter_reponse(True)  # passe à 2 → délai 7 jours
    print("Après :", c2)
    print("Date prochaine :", c2.date_prochaine)

#############################################################################
# Écrire la fonction extraire_cartes_du_jour de la question 2               #
#############################################################################

def extraire_cartes_du_jour(paquet, date_jour):
    """
    renvoie une nouvelle liste contenant uniquement les cartes
    dont la date_prochaine est inférieure ou égale à date_jour
    parametre en entrée:
        paquet: list de Carte
        date_jour: date
    parametre en sortie:
        list
    """
    # Creation de la liste vide qui va recevoir les cartes du jour
    cartesDuJour = []
    # Pour chaque carte du paquet
    for carte in paquet:
        # si la date de la carte est inférieure ou égal à date_jour
        if carte.date_prochaine <= date_jour:
            # On ajoute la carte à cartesDuJour
            cartesDuJour.append(carte)
    # à la fin de la boucle, on renvoie la liste
    return cartesDuJour

# des tests pour la fonction extraire_cartes_du_jour
def test_q2():
    for nb_jours in range(10):
        print(extraire_cartes_du_jour(paquet,date_future(nb_jours)))


#############################################################################
# Fonction défaillante à analyser et corriger pour la question 3            #
#############################################################################

def extraire_cartes_a_renforcer(paquet):
    """
    Parcourt le paquet et renvoie la liste des cartes ayant le
    niveau d'avancement le plus faible.
    """
    if len(paquet) == 0:
        return []
    # On recupere le niveau minimal
    niveau_min = paquet[0].niveau
    # initialisation de la liste de cartes à renforcer
    a_renforcer = []
    # Pour chaque carte du paquet
    for carte in paquet:
        # si la carte a un niveau inférieur à niveau_min
        if carte.niveau < niveau_min:
            # nouveau niveau_min
            niveau_min = carte.niveau
            # creation de nouveau a_renforcer
            a_renforcer = [carte]
        # si la carte a un niveau egal à niveau_min
        elif carte.niveau == niveau_min:
            # ajout de la carte à a_renforcer
            a_renforcer.append(carte)
    return a_renforcer




def test_renforcement():
    # Création d'un paquet de test
    c1 = Carte("Capitale de l'Italie ?", "Rome")
    c1.niveau = 2

    c2 = Carte("7 x 8 ?", "56")
    c2.niveau = 1

    c3 = Carte("Symbole du Fer ?", "Fe")
    c3.niveau = 2

    mon_paquet = [c1, c2, c3]

    # Appel de la fonction défaillante
    resultat = extraire_cartes_a_renforcer(mon_paquet)

    print("Cartes à renforcer (niveau le plus bas attendu : 1) :")
    print(resultat)

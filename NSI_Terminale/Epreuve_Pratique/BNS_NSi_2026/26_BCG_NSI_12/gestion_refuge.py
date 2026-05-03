import csv

class Renard:
    """
    Classe représentant un renard dans le refuge.
    Attributs : identifiant, nom, poids, date_arrivee.
    """
    def __init__(self, identifiant, nom, poids, date_arrivee):
        self.identifiant = identifiant #int
        self.nom = nom  #str
        self.poids = poids  #float
        self.date_arrivee = date_arrivee    # str AAAA-MM-JJ


        pass # Question 1 à compléter

    def __str__(self):
        sortie = f'Renard ID {self.identifiant} - {self.nom} (Arrivé le {self.date_arrivee})'
        return sortie
        pass # Question 2 à compléter
renard1 = Renard(200, 'Oscar', 5.1, '2026-01-01')


class Refuge:
    """
    Classe représentant le refuge contenant la liste des renards.
    """
    def __init__(self, nom, adresse):
        self.nom = nom
        self.adresse = adresse
        self.liste_renards = []

    def recueillir(self, un_renard):
        """
        Méthode d'ajout d'un renard au refuge.
        """
        self.liste_renards.append(un_renard)

    def lister_peu_corpulents(self):
        """
        Méthode qui renvoie une liste des Renards dont le poids est < 6.0 kg.
        """
        return [renard for renard in self.liste_renards if renard.poids < 6.0]

    def pourcentage_peu_corpulents(self):
        """
        Méthode qui renvoie le pourcentage des renards peu corpulents.
        """
        if len(self.liste_renards) == 0:
            return 0.0
        return len(self.lister_peu_corpulents()) / len(self.liste_renards) * 100

    def importer_donnees(self, nom_fichier):
        """
        Fonction qui importe les données des renards à partir d'un fichier CSV.
        """
        print(f"Tentative d'importation depuis {nom_fichier}...")
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            lignes = csv.DictReader(f, delimiter=';')
            for ligne in lignes:
                # Chaque donnée est lue comme un str !for
                renard = Renard(
                            int(ligne['id']),
                            ligne['nom'],
                            float(ligne['poids']),
                            ligne['date_arrivee'])
                self.recueillir(renard)

refuge = Refuge("SOS Goupil", "123 rue de la forêt")
refuge.importer_donnees("donnees_renards.csv")
def test_q3():
    for renard in refuge.liste_renards:
        print(renard)


# Q4

##Un renard est peu corpulent si sa masse est inférieure à 6.0kg
##
##On compte :
##- nombre de renards < 6.0 kg
renards_peu_corpulents = refuge.lister_peu_corpulents()
nb_renards_peu_corpulents = len(renards_peu_corpulents)

##- nombre total de renards
nb_total_renards = len(refuge.liste_renards)
##
##Exemple avec les données fournies
##Total : 30 renards
##Peu corpulents : 15
##
##Pourcentage = (15 / 30) × 100 = 50 %

print(100*nb_renards_peu_corpulents/nb_total_renards)

print(refuge.pourcentage_peu_corpulents())
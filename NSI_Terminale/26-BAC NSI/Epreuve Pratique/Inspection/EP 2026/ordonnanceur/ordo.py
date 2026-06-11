# Créé par thoma, le 10/10/2025 en Python 3.7
class Processus:
    def __init__(self, nom:str, duree:int):
        self.nom = nom
        self.duree_totale = duree
        self.duree_restante = duree
        self.temps_attente = 0
        self.temps_execution = 0

    def __str__(self):
        return f'{self.nom}:  restant = {self.duree_restante}'

class OrdonnanceurRR:
    def __init__(self, quantum:int):
        self.quantum = quantum
        self.file = []
        self.temps_courant = 0
        self.historique = []

    def est_vide(self):
        return self.file == []

    def ajouter_processus(self, processus):
        self.file.append(processus)
        print(f'{processus.nom) a été ajouté à la file')


    def executer(self):
        print('Début de l\'ordonnancement Round Robin')

        while not self.est_vide():
            processus_en_cours = self.file.pop(0)


P1 = Processus('P1', 8)

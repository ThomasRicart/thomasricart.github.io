import random

tab = [5, 3, 8, 0, 1, 2, 7, 6, 4]

# Q3
tab_gagnant = [0, 1, 2, 3, 4, 5, 6, 7, 8]
assert tab_gagnant == [i for i in range(0, 9)]

class Taquin:
    def __init__(self):
        self.tab = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.pile = Pile()
        self.mode_resolution = False
    # Q4
    def est_gagnant (self):
        return self.tab == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # Q5
    def indice(self, numero):
        assert type(numero) == int
        assert 0 <= numero <= 8
        while self.tab[i] != numero:
            i = i + 1
        return i

    # Q6
    def est_possible(self, numero):
        ''' Renvoie True si le déplacement de numéro est possible '''
        pass
    def jouer(self, numero):
        if self.est_possible(numero):
            i = self.indice(numero)
            j = self.indice(0)
            self.tab[j] = numero
            self.tab[i] = 0
        if not self.mode_resolution:
            self.pile.empiler(numero)

    # Q7
    def coups_possibles(self):
        ''' Renvoie une liste des numeros possibles à déplacer '''
        pass
    def melanger(self, n):
        precedent = None
        i = 0
        while i < n:
            possibilites = self.coups_possibles()
            choix = random.choice(possibilites)
            if choix != precedent:
                self.jouer(choix)
                precedent = choix
                i = i + 1

# Q8
# [0, 1, 2] [1, 0, 2]   [1, 4, 2]   [1, 4, 2]   [1, 4, 0]
# [3, 4, 5] [3, 4, 5]   [3, 0, 5]   [3, 5, 0]   [3, 5, 2]
# [6, 7, 8] [6, 7, 8]   [6, 7, 8]   [6, 7, 8]   [6, 7, 8]
# PILE s <- 2, 5, 4, 1
# Coups résolution automatique: 2 - 5 - 4 - 1
    def resoudre(self):
        self.mode_resolution = True
        while not self.est_gagnant():
            coup_a_jouer = self.pile.depile()
            print("coup joué: ", coup_a_jouer)
            self.jouer(coup_a_jouer)
# Q10:
# LE même numero serait dépiler puis re empilé immédiatement ensuite

# Q11
    def jouer2(self, numero):
        if self.est_possible(numero):
            i = self.indice(numero)
            j = self.indice(0)
            self.tab[j] = numero
            self.tab[i] = 0
        if not self.mode_resolution:
            if not self.pile.est_vide():
                numero_sommet_pile = self.pile.depile()
                if numero == numero_sommet_pile:
                    self.pile.empiler(numero_sommet_pile)
                    self.pile.empiler(numero)
            else:
                self.pile.empiler(numero)






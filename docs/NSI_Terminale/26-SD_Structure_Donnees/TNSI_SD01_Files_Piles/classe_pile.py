# Créé par thoma, le 16/03/2025 en Python 3.7
class Pile:
    def __init__(self, taille = None):
        ''' Si taille est None, la pile n'a pas de taille maximum '''
        self.pile = []
        self.nb_elements = 0
        if taille:
            self.taille = taille

    def est_vide(self):
        ''' Renvoie True si la pile est vide '''
        return self.nb_elements == 0
    def est_pleine(self):
        ''' Renvoie True si la pile est pleine '''
        if taille:
            return (self.nb_elements == self.taille)
        return False
    def empiler(self, element):
        ''' Empile element si non pleine '''
        if not self.est_pleine():
            self.pile.append(element)
    def depiler(self):
        ''' Renvoie l'élément dépilé si non vide '''
        if not self.est_vide():
            return self.pile.pop()


P = Pile()          # Pas de taille maximum
assert P.est_vide()
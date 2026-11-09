class Maillon:
    def __init__(self, nom, suivant = None):
        self.nom = nom
        self.suivant = suivant
    def __str__(self):
        return f'{self.nom}<-{self.suivant}'
    def get_suivant(self):
        return self.suivant
    def get_nom(self):
        return self.nom
    def set_suivant(self, maillon):
        self.suivant = maillon

A = Maillon(1)
B = Maillon(2)
A.suivant = B

class File_chainee:
    def __init__(self, maillon = None):
        self.premier_element = maillon
    def est_vide(self):
        return self.premier_element == None
    def enfiler(self, valeur):
        nouveau_maillon = Maillon(valeur)
        if self.est_vide():
            self.premier_element = nouveau_maillon
        else:
            courant = self.premier_element
            while courant.suivant:
                courant = courant.suivant
            courant.suivant = nouveau_maillon
    def defiler(self):
        if not self.est_vide():
            elt_a_renvoyer = self.premier_element
            self.premier_element = self.premier_element.suivant
            return elt_a_renvoyer

    def __str__(self):
        if self.est_vide():
            return f'[]'
        else:
            liste = []
            courant = self.premier_element
            while courant:
                liste.append(str(courant.nom))
                courant = courant.suivant
            elements = "<-".join(liste)
            return elements
F = File_chainee()
assert F.est_vide()
F.enfiler(1)
F.enfiler(2)
F.enfiler(3)
print(F)

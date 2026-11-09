class Maillon:
    def __init__(self, valeur, suivant = None):
        self.valeur = valeur
        self.suivant = suivant          # de type Maillon

    def __str__(self):
        ''' Surcharge de l'opérateur print '''
        return f'{self.valeur}'

A = Maillon(1)
B = Maillon(2)
assert A.valeur == 1
assert B.valeur == 2
assert A.suivant == None
A.suivant = B
assert A.suivant == B
#print(A)
#print(B)


class File_chainee:
    def __init__(self, tete = None):
        self.tete = tete                # de type Maillon
    def est_vide(self):
        return self.tete == None
    def enfiler(self, valeur):
        maillon_a_inserer = Maillon(valeur)
        if self.est_vide():
            self.tete = maillon_a_inserer
        else:
            maillon_courant = self.tete
            while maillon_courant.suivant:
                maillon_courant = maillon_courant.suivant
            maillon_courant.suivant = maillon_a_inserer
    def defiler(self):
        if not self.est_vide():
            maillon_a_renvoyer = self.tete
            self.tete = self.tete.suivant
            return maillon_a_renvoyer
    def __str__(self):
        if not self.tete:
            return f'None'
        liste = []
        courant = self.tete
        while courant:
            liste.append(str(courant.valeur))
            courant = courant.suivant
        elements = "<-".join(liste)
        return elements


F = File_chainee()
assert F.est_vide()
F.enfiler(1)
assert F.tete.valeur == 1
F.enfiler(2)
F.enfiler(3)
F.enfiler(4)

print(F)
print(F.defiler())
print(F)
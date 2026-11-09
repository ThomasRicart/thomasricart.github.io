

class File_circulaire:
    def __init__(self, taille, tete = None):
        self.taille = taille
        self.file = [None]*self.taille
        self.debut = 0      # indice debut
        self.fin = 0        # indice fin
        self.nb_elements = 0
    def est_vide(self):
        return self.nb_elements == 0
    def est_plein(self):
        return self.nb_elements == self.taille
    def enfiler(self, valeur):
        if not self.est_plein():
            self.nb_elements += 1
            self.file[self.fin] = valeur
            self.fin = (self.fin + 1) % self.taille
    def defiler(self):
        if not self.est_vide():
            self.nb_elements -= 1
            element_a_defiler = self.file[self.debut]
            self.debut = (self.debut + 1) % self.taille
            return element_a_defiler


FC = File_circulaire(4)
FC.enfiler(1)
print(FC.file, FC.nb_elements)
FC.enfiler(6)
FC.enfiler(7)
FC.enfiler(8)
print(FC.file, FC.nb_elements)
FC.defiler()
print(FC.file, FC.nb_elements)
FC.enfiler(9)
print(FC.file, FC.nb_elements)
print(FC.defiler())
print(FC.file, FC.nb_elements)
FC.enfiler(4)
print(FC.file, FC.nb_elements)



FC = File_circulaire(5)
FC.enfiler(1)
print(FC.est_vide())
print(FC.est_plein())
print(FC.debut)
print(FC.fin)
FC.enfiler(2)
print(FC.est_vide())
print(FC.est_plein())
print(FC.debut)
print(FC.fin)

FC.enfiler(3)

FC.enfiler(4)
FC.enfiler(5)
FC.enfiler(6)
print(FC.est_vide())
print(FC.est_plein())
print(FC.debut)
print(FC.fin)



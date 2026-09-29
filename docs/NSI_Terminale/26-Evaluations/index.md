# Evaluations

1. [Évaluation 01]() : Révisions classe première/ [Correction]()


Code de l'exercice 8:
```python
class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur
    def get_couleur(self):
        return self.couleur
    
class Paquet:
    def __init__(self):
        self.cartes = []
    def ajouter_carte(self, carte):
        self.cartes.append(carte)
    def get_cartes(self):
        return self.cartes
```
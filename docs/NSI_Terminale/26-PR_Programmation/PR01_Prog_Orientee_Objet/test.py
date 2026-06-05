NOM = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
VALEURS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
COULEURS = ['Pique', 'Coeur', 'Carreau', 'Trefle']

def make_dico_carte(NOM:list, VALEURS:list) -> dict:
    ''' Crée un dictionnaire associant à chaque nom de carte sa valeur 
    sortie (dict) : un dictionnaire associant à chaque nom de carte sa valeur 
    exemple : make_dico_carte(NOM, VALEURS) -> {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
    '''
    sortie = {}
    # A compléter
    for i in range(len(NOM)):
        sortie[NOM[i]] = VALEURS[i]

    return sortie

DICO_CARTE = make_dico_carte(NOM, VALEURS)
# Résultat attendu : {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}


class Carte:
    def __init__(self, nom:str, couleur:str)-> None:
        ''' Initialise une carte avec un nom et une couleur'''
        self.nom = nom
        self.couleur = couleur

    def get_valeur(self)-> int:
        ''' Renvoie la valeur de la carte '''
        return DICO_CARTE[self.nom]


    def get_couleur(self)-> str:
        ''' Renvoie la couleur de la carte '''
        return self.couleur

    def __str__(self)-> str:
        ''' Renvoie une chaîne de caractères représentant la carte (ex: `10 de Pique`) '''
        return f"{self.nom} de {self.couleur}"

    def __eq__(self, other)-> bool:
        ''' Renvoie `True` si deux cartes sont de même valeur et `False` sinon 
        other (Carte) : la carte à comparer ''' 
        return self.get_valeur() == other.get_valeur()        
    def __lt__(self, other)-> bool:
        ''' Renvoie `True` si la carte est de valeur inférieure à l'autre et `False` sinon 
        other (Carte) : la carte à comparer '''
        return self.get_valeur() < other.get_valeur()


    def __gt__(self, other)-> bool:
        ''' Renvoie `True` si la carte est de valeur supérieure à l'autre et `False` sinon 
        other (Carte) : la carte à comparer ''' 
        return self.get_valeur() > other.get_valeur()

# Protocoles de test
def test_carte():
    ''' Teste la classe Carte '''
    carte1 = Carte('10', 'Pique')
    carte2 = Carte('Valet', 'Coeur')
    print(carte1) # Résultat attendu : 10 de Pique
    print(carte2) # Résultat attendu : Valet de Coeur
    print(carte1.get_valeur()) # Résultat attendu : 10
    print(carte1.get_couleur()) # Résultat attendu : Pique
    print(carte2.get_valeur()) # Résultat attendu : 11
    print(carte2.get_couleur()) # Résultat attendu : Coeur
    print(carte1 == carte2) # Résultat attendu : False
    print(carte1 < carte2) # Résultat attendu : True
    print(carte1 > carte2) # Résultat attendu : False
test_carte()

import random

NOM = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
VALEURS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
COULEURS = ['Pique', 'Coeur', 'Carreau', 'Trefle']
DICO_CARTE = make_dico_carte(NOM, VALEURS)
print(DICO_CARTE) # Résultat attendu : {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}
class Deck:
    def __init__(self, DICO_CARTE)-> None:
        ''' Initialise un paquet de cartes (une carte de chaque couleur et de chaque valeur) 
        Les cartes sont stockées dans une liste d'attribut `cartes`'''
        self.cartes = []
        self.reset()
    
    def __str__(self)-> str:
        ''' Renvoie une chaîne de caractères représentant le paquet de cartes (ex: `2 de Pique, 3 de Pique, ..., As de Trefle`) '''
        return ', '.join(str(carte) for carte in self.cartes)

    def melanger(self)-> None:
        ''' Mélange le paquet de cartes '''
        random.shuffle(self.cartes)

    def tirer_carte(self)-> Carte:
        ''' Tire une carte du paquet et la renvoie. La carte tirée est retirée du paquet.
        Si le paquet est vide, renvoie `None`'''
        if len(self.cartes) == 0:
            return None
        else:
            return self.cartes.pop()

    def cartes_restantes(self)-> int:
        ''' Renvoie le nombre de cartes restantes dans le paquet '''
        return len(self.cartes)

    def reset(self)-> None:
        ''' Réinitialise le paquet de cartes (remet toutes les cartes dans le paquet) '''
        self.cartes = []
        for n in DICO_CARTE.keys():
            for c in COULEURS:
                self.cartes.append(Carte(n, c))

    def distribuer(self, n:int)-> list:
        ''' Distribue n cartes du paquet et les renvoie sous forme de liste. Les cartes distribuées sont retirées du paquet.
        Si le paquet contient moins de n cartes, distribue toutes les cartes restantes et renvoie la liste des cartes distribuées.'''
        cartes_distribuees = []
        if len(self.cartes) < n:
            n = len(self.cartes)
        for i in range(n):
            cartes_distribuees.append(self.tirer_carte())
        return cartes_distribuees

    def cartes_couleur(self, couleur:str)-> list:
        ''' Renvoie une liste de toutes les cartes du paquet de la couleur donnée en argument. 
        Si aucune carte de cette couleur n'est présente dans le paquet, renvoie une liste vide.'''
        cartes_meme_couleur = []
        for carte in self.cartes:
            if carte.get_couleur() == couleur:
                cartes_meme_couleur.append(carte)
        return cartes_meme_couleur


    def cartes_valeur(self, valeur:int)-> list:
        ''' Renvoie une liste de toutes les cartes du paquet de la valeur donnée en argument. 
        Si aucune carte de cette valeur n'est présente dans le paquet, renvoie une liste vide.'''   
        cartes_meme_valeur = []
        for carte in self.cartes:
            if carte.get_valeur() == valeur:
                cartes_meme_valeur.append(carte)
        return cartes_meme_valeur


    def cartes_sup_valeur(self, valeur:int)-> list:
        ''' Renvoie une liste de toutes les cartes du paquet de valeur supérieure à la valeur donnée en argument. 
        Si aucune carte de valeur supérieure n'est présente dans le paquet, renvoie une liste vide.'''
        cartes_sup_valeur = []
        for carte in self.cartes:
            if carte.get_valeur() > valeur:
                cartes_sup_valeur.append(carte)
        return cartes_sup_valeur


    def cartes_inf_valeur(self, valeur:int)-> list:
        ''' Renvoie une liste de toutes les cartes du paquet de valeur inférieure à la valeur donnée en argument.   
        Si aucune carte de valeur inférieure n'est présente dans le paquet, renvoie une liste vide.'''
        cartes_inf_valeur = []
        for carte in self.cartes:
            if carte.get_valeur() < valeur:
                cartes_inf_valeur.append(carte)
        return cartes_inf_valeur

      

D = Deck(DICO_CARTE)
print(D) # Résultat attendu : 2 de Pique, 3 de Pique
A=D.distribuer(5)
print(A) # Résultat attendu : 7 cartes restantes dans le paquet (ex:

class Main:
    def __init__(self, deck:Deck, nb_cartes:int)-> None:
        ''' Initialise une main de cartes (une liste de cartes)'''
        self.main = []
        for i in range(nb_cartes):
            self.main.append(deck.tirer_carte())

    
    def __str__(self)-> str:
        ''' Renvoie une chaîne de caractères représentant la main de cartes (ex: `10 de Pique, Valet de Coeur, ...`) '''
        return ', '.join(str(carte) for carte in self.main)
    def melange_main(self)-> None:
        ''' Mélange la main de cartes '''
        random.shuffle(self.main)
        
    def ajouter_carte(self, carte:Carte)-> None:
        ''' Ajoute une carte à la main '''
        self.main.append(carte)

    def jouer_carte(self)-> None:
        ''' Joue une carte de la main (retire une carte de la main et la renvoie). Si la main est vide, renvoie `None`'''
        if len(self.main) == 0:
            return None
        else:
            return self.main.pop()
        
    def retirer_carte(self, carte:Carte)-> None:
        ''' Retire une carte de la main. Si la carte n'est pas présente dans la main, ne fait rien.'''
        if carte in self.main:
            self.main.remove(carte)

    def valeur_main(self)-> int:
        ''' Renvoie la valeur totale de la main (la somme des valeurs des cartes présentes dans la main) '''
        return sum(carte.get_valeur() for carte in self.main)
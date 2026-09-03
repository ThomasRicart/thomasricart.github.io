# Spécialité NSI — Terminale
## TP Orienté Objet : Simulation d'un jeu de cartes (La Bataille)

**Durée estimée :** 1h30  
**Notions abordées :** Classes, encapsulations, méthodes spéciales (`__repr__`, `__len__`), composition, algorithme de mélange, manipulation de listes.

---

### Objectif
Construire pas à pas la structure d'un jeu de la Bataille en appliquant les principes de la **Programmation Orientée Objet**.

Le TP s'articule autour de 4 classes complémentaires :
1. **`Carte`** : Représente une carte unique définie par sa valeur et sa couleur.
2. **`Deck`** : Représente le paquet initial complet (52 cartes) capable de se mélanger et de distribuer.
3. **`Main`** : Représente le jeu de cartes en main d'un joueur.
4. **`Jeu`** : Orchestre le déroulement de la partie entre deux joueurs.

---

### Étape 1 : La classe `Carte`

Une carte possède une **valeur** (de 2 à 14, où 11=Valet, 12=Dame, 13=Roi, 14=As) et une **couleur** (`'Pique'`, `'Cœur'`, `'Carreau'`, `'Trèfle'`).

#### Code à compléter :

```python
class Carte:
    NOMS_VALEURS = {11: 'Valet', 12: 'Dame', 13: 'Roi', 14: 'As'}

    def __init__(self, valeur, couleur):
        """
        Initialise la carte avec une valeur (int) et une couleur (str).
        """
        self.valeur = valeur
        self.couleur = couleur

    def __repr__(self):
        """
        Renvoie une représentation sous forme de texte de la carte.
        Exemples : "8 de Pique", "As de Cœur"
        """
        if self.valeur in Carte.NOMS_VALEURS:
            nom = ......
        else:
            nom = str(self.valeur)
        return f"{nom} de {self.couleur}"

    def est_plus_forte_que(self, autre_carte):
        """
        Renvoie True si la valeur de self est strictement supérieure 
        à celle de autre_carte, False sinon.
        """
        return ......
```

---

### Étape 2 : La classe `Deck` (Le paquet de cartes)

Un `Deck` contient les 52 cartes du jeu au départ.

#### Code à compléter :

```python
import random

class Deck:
    COULEURS = ['Pique', 'Cœur', 'Carreau', 'Trèfle']
    VALEURS = list(range(2, 15))  # de 2 à 14

    def __init__(self):
        """
        Génère un paquet complet de 52 cartes (combinaisons de valeurs et couleurs).
        """
        self.cartes = []
        for c in Deck.COULEURS:
            for v in Deck.VALEURS:
                # Ajouter une nouvelle instance de Carte à self.cartes
                self.cartes.append(......)

    def melanger(self):
        """Mélange aléatoirement la liste des cartes."""
        random.shuffle(......)

    def distribuer(self, main1, main2):
        """
        Distribue alternativement une carte à main1 et une carte à main2
        jusqu'à ce que le paquet soit vide.
        """
        tour_main1 = True
        while len(self.cartes) > 0:
            carte = self.cartes.pop()  # Extrait la dernière carte
            if tour_main1:
                main1.ajouter_carte(......)
            else:
                main2.ajouter_carte(......)
            tour_main1 = not tour_main1
```

---

### Étape 3 : La classe `Main` (Le jeu d'un joueur)

La classe `Main` gère la file des cartes détenues par un joueur. Quand un joueur gagne un pli, les cartes sont remises sous son paquet.

#### Code à compléter :

```python
class Main:
    def __init__(self, nom_joueur):
        self.nom = nom_joueur
        self.cartes = []

    def ajouter_carte(self, carte):
        """Ajoute une carte sous la pile du joueur (en fin de liste)."""
        self.cartes.append(carte)

    def tirer_carte(self):
        """
        Extrait et renvoie la première carte au-dessus de la pile (début de liste).
        Renvoie None si le joueur n'a plus de cartes.
        """
        if len(self.cartes) == 0:
            return None
        return self.cartes.pop(......)  # Quel indice permet de retirer le premier élément ?

    def est_vide(self):
        """Renvoie True si la main est vide."""
        return ......

    def __len__(self):
        """Permet d'utiliser len(main) pour connaître le nombre de cartes restantes."""
        return len(self.cartes)
```

---

### Étape 4 : La classe `Jeu` (Moteur de simulation)

La classe `Jeu` va assembler les éléments et simuler une partie de bataille classique (simplifiée sans gestion des égalités/bataille complexe, ou avec re-mélange des cartes gagnées).

#### Code à compléter :

```python
class Jeu:
    def __init__(self, nom_j1="Joueur 1", nom_j2="Joueur 2"):
        self.main1 = Main(nom_j1)
        self.main2 = Main(nom_j2)
        
        # 1. Création et préparation du paquet
        deck = Deck()
        deck.melanger()
        
        # 2. Distribution aux deux joueurs
        deck.distribuer(self.main1, self.main2)

    def jouer_un_tour(self):
        """
        Simule un tour de jeu :
        - Chaque joueur tire une carte.
        - On compare les cartes.
        - Le gagnant récupère les deux cartes.
        - En cas d'égalité (Bataille), chaque joueur reprend sa propre carte.
        """
        carte1 = self.main1.tirer_carte()
        carte2 = self.main2.tirer_carte()

        if carte1 is None or carte2 is None:
            return False  # Partie terminée

        print(f"{self.main1.nom} joue {carte1} | {self.main2.nom} joue {carte2}")

        if carte1.est_plus_forte_que(carte2):
            print(f"-> {self.main1.nom} remporte le pli !\n")
            self.main1.ajouter_carte(carte1)
            self.main1.ajouter_carte(carte2)

        elif carte2.est_plus_forte_que(carte1):
            print(f"-> {self.main2.nom} remporte le pli !\n")
            self.main2.ajouter_carte(carte1)
            self.main2.ajouter_carte(carte2)

        else:
            print("-> Égalité ! Chacun reprend sa carte.\n")
            self.main1.ajouter_carte(carte1)
            self.main2.ajouter_carte(carte2)

        return True

    def lancer_partie(self, max_tours=500):
        """
        Lance la simulation sur un nombre maximum de tours
        pour éviter les boucles infinies.
        """
        tour = 1
        en_cours = True
        
        while en_cours and tour <= max_t
# Créé par thoma, le 21/10/2025 en Python 3.7
class Jeton:
    def __init__(self, couleur, x, y):
        self.couleur = couleur  # 'R' ou 'J'
        self.x = x
        self.y = y

    def __repr__(self):
        return self.couleur


class Grille:
    def __init__(self, lignes=6, colonnes=7):
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[None for _ in range(colonnes)] for _ in range(lignes)]

    def afficher(self):
        print("\n  " + " ".join(str(i) for i in range(self.colonnes)))
        for ligne in self.grille:
            print(" |" + "|".join(j.couleur if j else " " for j in ligne) + "|")
        print("  " + "--" * self.colonnes)

    def placer_jeton(self, colonne, couleur):
        """Place un jeton dans la colonne si possible.
           Retourne le jeton placé ou None si impossible."""
        y = self.lignes - 1
        jeton_place = None

        while y >= 0 and jeton_place is None:
            if self.grille[y][colonne] is None:
                self.grille[y][colonne] = Jeton(couleur, colonne, y)
                jeton_place = self.grille[y][colonne]
            y = y - 1
        return jeton_place

    def verifier_victoire(self, x, y):
        """Teste si le jeton (x,y) forme un alignement de 4."""
        jeton = self.grille[y][x]
        if jeton is None:
            return False

        couleur = jeton.couleur
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        index = 0
        victoire = False

        while index < len(directions) and not victoire:
            dx, dy = directions[index]
            compteur = 1
            compteur = compteur + self._compter(jeton, dx, dy, couleur)
            compteur = compteur + self._compter(jeton, -dx, -dy, couleur)
            if compteur >= 4:
                victoire = True
            index = index + 1

        return victoire

    def _compter(self, jeton, dx, dy, couleur):
        """Compte les jetons de même couleur dans une direction donnée."""
        x = jeton.x + dx
        y = jeton.y + dy
        compteur = 0
        fini = False

        while not fini:
            if 0 <= x < self.colonnes and 0 <= y < self.lignes:
                j = self.grille[y][x]
                if j is not None and j.couleur == couleur:
                    compteur = compteur + 1
                    x = x + dx
                    y = y + dy
                else:
                    fini = True
            else:
                fini = True
        return compteur

    def est_pleine(self):
        x = 0
        pleine = True
        while x < self.colonnes and pleine:
            if self.grille[0][x] is None:
                pleine = False
            x = x + 1
        return pleine


class Jeu:
    def __init__(self):
        self.grille = Grille()
        self.joueurs = ['R', 'J']
        self.tour = 0

    def demander_colonne(self):
        print(f"Joueur {self.joueurs[self.tour % 2]}, choisissez une colonne (0-{self.grille.colonnes - 1}) : ", end="")
        entree = input()
        if entree.isdigit():
            col = int(entree)
            if 0 <= col < self.grille.colonnes:
                return col
        return None

    def jouer(self):
        print("=== Puissance 4 ===")
        gagnant = None

        while gagnant is None and not self.grille.est_pleine():
            self.grille.afficher()
            joueur = self.joueurs[self.tour % 2]

            col = None
            while col is None:
                col = self.demander_colonne()
                if col is None:
                    print("Entrée invalide. Recommencez.")

            jeton = self.grille.placer_jeton(col, joueur)
            if jeton is None:
                print("Colonne pleine, choisissez-en une autre.")
            else:
                if self.grille.verifier_victoire(jeton.x, jeton.y):
                    gagnant = joueur
                else:
                    self.tour = self.tour + 1

        self.grille.afficher()
        if gagnant is not None:
            print("🎉 Joueur", gagnant, "a gagné !")
        else:
            print("Match nul.")


if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()


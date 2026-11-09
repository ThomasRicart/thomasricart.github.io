# 🐍 SD01 : Files et Piles


---

## 📂 Ressources du Chapitre

Accédez ici à l'ensemble des documents de cours et aux outils de révision interactive.

| Support | Description | Corrections |
| :--- | :--- | :--- |
| [📕 **Cours**](./TNSI_SD02_Piles_files.pdf) | Le support de cours complet en version PDF. | |

<details>
<summary><b>Voir la correction Pile</b></summary>
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
</details>

---
---

### 🧩 Concepts illustrés
```python
```
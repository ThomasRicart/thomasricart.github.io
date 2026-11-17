# 🐍 AP05 : Les Listes et Tuples

<div class="subtitle" style="font-size: 1.2em; color: #546e7a; margin-bottom: 25px; font-style: italic;">
</div>

---

## 📂 Ressources du Chapitre

Accédez ici à l'ensemble des documents de cours et aux outils de révision interactive.

| Support | Description | Corrections |
| :--- | :--- | :--- |
| [📕 **Cours**](./AP05_Listes_Tuples.pdf) | Le support de cours complet en version PDF. | |
| [💡 **Synthèse**](./AP05_Listes_Tuples-synth.pdf) | Fiche récapitulative des concepts clés (HTML). | |
| [🎴 **Flashcards**](./flashcards/AP05_flashcards.html) | Cartes de mémorisation pour réviser les notions. ||
| [📝 **Quiz**](./quiz/AP05_quiz.html)| Auto-évaluation rapide sur le chapitre. ||
| [✏️ **Exercices 01**](./exercices/AP05_EXO1_Sujet.pdf) | Exercices d'application Listes et tuples |[Correction](./exercices/AP05_EXO1_Correction.pdf) |
| [✏️ **Exercices 02**](https://raisintine.fr/chocolatine/question.php?idc=66) | Exercices interactifs listes, tuples | |
| [✏️ **Exercices 03**](https://raisintine.fr/chocolatine/question.php?idc=61) | Exercices interactifs tableaux | |
| [📚 **Activité Capytale 1 - Listes**](https://capytale2.ac-paris.fr/web/c/3339-10504443) | **3339-10504443** | [Correction]()|
| [📚 **Activité Capytale 2 - Projet**](https://capytale2.ac-paris.fr/web/c/75a9-10504452) | **75a9-10504452** | [Correction]()|

---
Une liste est une structure de données qui permet de stocker plusieurs valeurs dans une seule variable. Les éléments d'une liste peuvent être de types différents (entiers, chaînes de caractères, etc.) et sont accessibles par leur position (indice) dans la liste.

```python
# Exemple de liste
ma_liste = ["Alice", "Bob", "Charlie", "David"]
```

| Indice | 0 | 1 | 2 | 3 |
| :---: | :--- | :--- | :--- | :--- |
| Élément | "Alice" | "Bob" | "Charlie" | "David" |

```python
# Exemple de liste
ma_liste = [3, 5, 7, 9, 12, 15]
```

| Indice | 0 | 1 | 2 | 3 | 4 | 5 |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| Élément | 3 | 5 | 7 | 9 | 12 | 15 |

Les différents algorithmes à connaitre:

```python 
# Algorithme 1 : Afficher les éléments d'une liste
# Itération sur les éléments d'une liste et affichage de chacun d'eux
def afficher_liste_element(liste):
    for element in liste:
        print(element)

# Itération sur les indices d'une liste et affichage de chacun des éléments
def afficher_liste_indices(liste):
    for i in range(len(liste)):
        print(liste[i])
```

```python
# Algorithme 2 : Effectuer la somme des éléments d'une liste
def somme_liste_elements(liste):
    somme = 0                   # Initialisation de la somme à 0
    for element in liste:       # Parcours de chaque élément de la liste
        somme = somme + element # Ajout de l'élément courant à la somme
    return somme                # Retourne la somme totale des éléments de la liste

def somme_liste_indices(liste):
    somme = 0
    for i in range(len(liste)):
        somme = somme + liste[i]
    return somme
```

```python
# Algorithme 3 : Trouver le maximum d'une liste
def maximum_liste_elements(liste):
    max_value = liste[0]
    for element in liste:
        if element > max_value:
            max_value = element
    return max_value

def maximum_liste_indices(liste):
    max_value = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > max_value:
            max_value = liste[i]
    return max_value
```

```python
# Algorithme 4 : Détecter si un élément est présent dans une liste
def est_present_element(liste, valeur):
    for element in liste:
        if element == valeur:
            return True
    return False

def est_present_indices(liste, valeur):
    for i in range(len(liste)):
        if liste[i] == valeur:
            return True
    return False
```
---

### 🧩 Concepts illustrés
```python
```
<!-- ===================== SUJET 2 : DÉBUT ===================== -->

# <span style="color:red">MÉTROPOLE J1 2025</span> — Exercice 2 : liste de tâches et file de priorité

**Notions :** POO, structure de file (interface `File`), insertion dans une file de priorité, coût d'un algorithme.
**Difficulté :** accessible et très proche du cours.

## Question 1

```python
tache1 = Tache(1, "Répondre aux e-mails", 45)
tache2 = Tache(2, "Ranger ma chambre", 60)
```

## Question 2

```python
    def avancer(self, n):
        """Fait avancer la tâche de n minutes."""
        self.duree_restante = self.duree_restante - n
```

## Question 3

```python
    def est_terminee(self):
        """Renvoie True si la tâche est terminée (durée restante négative ou nulle)."""
        return self.duree_restante <= 0
```

## Question 4

File de départ :

```text
[début] (<t3>, 4) (<t1>, 3) (<t2>, 3) (<t4>, 1) (<t5>, 1) [fin]
```

Après ajout de la tâche 6 avec la priorité 2. Elle se place après les priorités 3 et avant les priorités 1 :

```text
[début] (<t3>, 4) (<t1>, 3) (<t2>, 3) (<t6>, 2) (<t4>, 1) (<t5>, 1) [fin]
```

Après ajout de la tâche 7 avec la priorité 4. Elle se place **après** `t3` (même priorité, insérée plus tard) et avant `t1` :

```text
[début] (<t3>, 4) (<t7>, 4) (<t1>, 3) (<t2>, 3) (<t6>, 2) (<t4>, 1) (<t5>, 1) [fin]
```

## Question 5

`f.defiler()` renvoie le tuple `(<t3>, 4)`, donc `f.defiler()[0]` vaut **`<t3>`**.

```text
[début] (<t1>, 3) (<t2>, 3) (<t4>, 1) (<t5>, 1) [fin]
```

## Question 6

`f.examiner()` renvoie le tuple `(<t3>, 4)` sans le retirer, donc `f.examiner()[1]` vaut **`4`**. La file est **inchangée** :

```text
[début] (<t3>, 4) (<t1>, 3) (<t2>, 3) (<t4>, 1) (<t5>, 1) [fin]
```

## Question 7

```python
def ajouter_file_prio(f, t, p):
    """Ajoute le tuple (t, p) dans la file de priorité f en respectant
    l'ordre décroissant des priorités puis l'ordre d'insertion."""
    f_aux = File()
    while not f.est_vide() and f.examiner()[1] >= p:
        f_aux.enfiler(f.defiler())      # éléments au moins aussi prioritaires
    f_aux.enfiler((t, p))               # insertion de la nouvelle tâche
    while not f.est_vide():
        f_aux.enfiler(f.defiler())      # éléments moins prioritaires
    while not f_aux.est_vide():
        f.enfiler(f_aux.defiler())      # on reconstitue f
```

## Question 8

Dans le pire des cas, chacun des `m` éléments de `f` est défilé de `f` puis enfilé dans `f_aux`, puis défilé de `f_aux` pour être remis dans `f`. Cela représente environ `2m + 1` opérations élémentaires : le coût est **linéaire**, en **O(m)**.

## Question 9

Durées restantes initiales : t3 = 90, t7 = 20, t1 = 45, t2 = 60, t6 = 60, t4 = 30, t5 = 30.

| Bloc | Créneau | Tâche qui avance | Durée restante après | File ensuite (de la tête à la fin) |
|:---:|:---:|:---:|:---:|---|
| 1 | 0–25 | t3 | 65 | t7, t3, t1, t2, t6, t4, t5 |
| 2 | 25–50 | t7 | terminée | t3, t1, t2, t6, t4, t5 |
| 3 | 50–75 | t3 | 40 | t3, t1, t2, t6, t4, t5 |
| 4 | 75–100 | t3 | 15 | t3, t1, t2, t6, t4, t5 |
| 5 | 100–125 | t3 | terminée | t1, t2, t6, t4, t5 |
| 6 | 125–150 | t1 | 20 | t2, t1, t6, t4, t5 |
| 7 | 150–175 | t2 | 35 | t1, t2, t6, t4, t5 |
| 8 | 175–200 | t1 | terminée | t2, t6, t4, t5 |
| 9 | 200–225 | t2 | 10 | t2, t6, t4, t5 |
| 10 | 225–250 | t2 | terminée | t6, t4, t5 |
| 11 | 250–275 | t6 | 35 | t6, t4, t5 |
| 12 | 275–300 | t6 | 10 | t6, t4, t5 |
| 13 | 300–325 | t6 | terminée | t4, t5 |
| 14 | 325–350 | t4 | 5 | t5, t4 |
| 15 | 350–375 | t5 | 5 | t4, t5 |
| 16 | 375–400 | t4 | terminée | t5 |
| 17 | 400–425 | t5 | terminée | (vide) |

Suite des tâches par blocs de 25 minutes :

```text
t3, t7, t3, t3, t3, t1, t2, t1, t2, t2, t6, t6, t6, t4, t5, t4, t5
```

Points d'attention :

- Quand une tâche est réinsérée avec la **même priorité**, elle passe **derrière** les tâches de même priorité déjà présentes (condition 2). C'est pourquoi `t3` est derrière `t7` au bloc 1, et `t1` derrière `t2` au bloc 6.
- Les priorités ne changent jamais.

## Question 10

```python
def planning(f):
    """Renvoie la liste des tâches dans l'ordre où elles sont traitées
    par tranches de 25 minutes (méthode Pomodoro). f est vidée par l'appel."""
    resultat = []
    while not f.est_vide():
        t, p = f.defiler()                 # tâche en tête de file
        resultat.append(t)
        t.avancer(25)
        if not t.est_terminee():
            ajouter_file_prio(f, t, p)     # on la remet avec la même priorité
    return resultat
```

<!-- ===================== SUJET 2 : FIN ===================== -->
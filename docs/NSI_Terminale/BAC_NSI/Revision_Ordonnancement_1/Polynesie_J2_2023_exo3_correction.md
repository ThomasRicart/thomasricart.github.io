<!-- ===================== SUJET 4 : DÉBUT ===================== -->

# <span style="color:red">POLYNESIE J2 2023</span> — Exercice 3 : processus et ordonnancement (plus court temps restant)

**Notions :** commande `ps`, PID/PPID, états d'un processus, ordonnancement « plus court temps restant d'abord », moyenne des temps d'exécution, programmation Python.
**Prérequis :** si la lecture de `ps -aef` ou l'ordonnancement SRT n'ont pas été traités en classe, les questions 1 et 2 peuvent être données comme exercices de découverte (l'énoncé fournit toutes les règles).

## Question 1

**a)** La colonne PPID donne le processus parent. Les processus liés à `firefox` sont :

- 9617, lancé depuis `bash` (PID 8887) ;
- 9657, 9697, 9750 et 9794, dont le parent est 9617 ;
- 9795, dont le parent est 9794.

```text
8887 (bash)
 └── 9617  (/usr/lib/firefox/firefox)
      ├── 9657
      ├── 9697
      ├── 9750
      └── 9794
           └── 9795
```

**b)** Le premier processus de Firefox est le PID 9617, le seul dont le parent n'est pas un processus Firefox (son parent est `bash`). Il a été lancé par la commande :

```text
/usr/lib/firefox/firefox
```

**c)** La commande `kill` accepte plusieurs PID. On supprime tous les processus de Firefox, et uniquement eux (pas `bash` 8887, ni `ps` 9802) :

```text
kill 9617 9657 9697 9750 9794 9795
```

## Question 2

**a)** Diagramme des états :

| Transition | Étiquette |
|---|---|
| Nouveau → **Prêt** | (création) |
| **Prêt** → **Élu** | **Mise en exécution** |
| **Élu** → **En attente** | **Blocage** |
| **En attente** → **Prêt** | **Déblocage** |
| **Élu** → Terminé | (fin du processus) |

Sur le schéma de l'énoncé :

- l'ovale de gauche est **Prêt**, celui de droite **Élu**, celui du bas **En attente** ;
- la flèche du haut est **Mise en exécution** ;
- la flèche qui descend vers l'ovale du bas est **Blocage** ;
- la flèche qui remonte vers l'ovale de gauche est **Déblocage**.

**b)** Chronogramme donné dans l'énoncé (algorithme « plus court temps restant », une unité à la fois). Les fins d'exécution se lisent sur le schéma ; le temps d'exécution vaut fin − arrivée :

| Processus | Arrivée | Fin | Temps d'exécution |
|:---:|:---:|:---:|:---:|
| P1 | 0 | 12 | 12 |
| P2 | 2 | 18 | 16 |
| P3 | 3 | 5 | 2 |
| P4 | 7 | 9 | 2 |

Moyenne = (12 + 16 + 2 + 2) / 4 = 32 / 4 = **8 cycles**.

**c)** On choisit le processus de plus court temps restant (en cas d'égalité, le plus ancien), puis on l'exécute **2 cycles** :

| Instant | Processus présents (temps restant) | Choix |
|:---:|---|:---:|
| 0 | P1 (8) | P1 |
| 2 | P1 (6), P2 (6) : égalité, P1 est le plus ancien | P1 |
| 4 | P1 (4), P2 (6), P3 (2) | P3 |
| 6 | P1 (4), P2 (6) (P4 n'arrive qu'à 7) | P1 |
| 8 | P1 (2), P2 (6), P4 (2) : égalité, P1 est le plus ancien | P1 |
| 10 | P2 (6), P4 (2) | P4 |
| 12, 14, 16 | P2 seul | P2 |

```text
Temps : 0  2  4  6  8  10 12 14 16 18
        |P1|P1|P3|P1|P1|P4|P2|P2|P2|
```

Soit, case par case (18 cases) :

```text
P1 P1 P1 P1 P3 P3 P1 P1 P1 P1 P4 P4 P2 P2 P2 P2 P2 P2
```

**d)** Fins d'exécution : P1 en 10, P2 en 18, P3 en 6, P4 en 12.

| Processus | Temps d'exécution |
|:---:|:---:|
| P1 | 10 − 0 = 10 |
| P2 | 18 − 2 = 16 |
| P3 | 6 − 3 = 3 |
| P4 | 12 − 7 = 5 |

Moyenne = (10 + 16 + 3 + 5) / 4 = 34 / 4 = **8,5 cycles**.

Cet ordonnancement est **moins performant** que le précédent (8,5 > 8). Comme on ne peut changer de processus que tous les 2 cycles, les processus courts P3 et P4 attendent plus longtemps avant de démarrer : P4 arrive à l'instant 7 mais ne démarre qu'à l'instant 10.

## Question 3

**a)**

```python
def choix_processus(liste_attente):
    """Renvoie l'indice du processus le plus court parmi
    ceux présents en liste d'attente liste_attente."""
    if liste_attente != []:
        mini = len(liste_attente[0])
        indice = 0
        for i in range(1, len(liste_attente)):
            if len(liste_attente[i]) < mini:
                mini = len(liste_attente[i])
                indice = i
        return indice
```

- Pour un processus présent, `len` donne son **temps restant**, car il n'y a plus de chaînes vides en fin de liste.
- La liste d'attente est rangée par ordre d'arrivée, et la comparaison **stricte** `<` garde le premier minimum rencontré. En cas d'égalité, c'est donc le plus ancien qui est choisi.

**b)**

```python
def ordonancement(liste_proc):
    """Exécute l'algorithme d'ordonnancement
    liste_proc -- liste des processus
    Renvoie la liste d'exécution des processus"""
    execution = []
    attente = scrutation(liste_proc, [])
    while attente != []:
        indice = choix_processus(attente)
        execution.append(attente[indice].pop(0))   # exécute un cycle du processus choisi
        if attente[indice] == []:                  # processus terminé : on le retire de la file d'attente
            attente.pop(indice)
        attente = scrutation(liste_proc, attente)
    return execution
```

Résultat attendu avec `p1`, `p2`, `p3`, `p4` de l'énoncé (on retrouve le chronogramme de la question 2) :

```text
['1.8', '1.7', '1.6', '3.2', '3.1', '1.5', '1.4', '4.2', '4.1',
 '1.3', '1.2', '1.1', '2.6', '2.5', '2.4', '2.3', '2.2', '2.1']
```

### Pour vérifier avec Python (facultatif)

La fonction `scrutation` n'est pas fournie dans l'énoncé. En voici une écriture possible, pour tester :

```python
def scrutation(liste_proc, attente):
    """Fait avancer d'un cycle la date d'arrivée des processus non encore présents
    et ajoute à la liste d'attente ceux qui viennent d'arriver."""
    for p in liste_proc:
        if len(p) > 0 and p[-1] == '':
            p.pop()                                   # pas encore arrivé : une chaîne vide en moins
        elif len(p) > 0 and not any(p is q for q in attente):
            attente.append(p)                         # vient d'arriver
    return attente
```

<!-- ===================== SUJET 4 : FIN ===================== -->
<!-- ===================== ÉNONCÉ : DÉBUT ===================== -->

# <span style="color:red">RÉVISION NSI — Round Robin</span> : énoncé

**Exercice (20 points)** — Cet exercice porte sur la gestion des processus, la programmation orientée objet et les structures de données (files).

Un système d'exploitation possède un **ordonnanceur** : il décide quel processus utilise le processeur. On étudie ici un ordonnanceur de type **tourniquet** (*round robin*) sur un processeur à un seul cœur.

---

## Partie A — États d'un processus (3 points)

**Question 1** (1 pt) — Donner le nom des états dans lesquels peut se trouver un processus au cours de sa vie.

**Question 2** (1,5 pt) — Recopier et compléter le tableau suivant. Chaque ligne décrit un événement et donne la transition correspondante (état de départ → état d'arrivée).

| Événement | État de départ | État d'arrivée |
|---|:---:|:---:|
| Le processus est créé puis admis | Nouveau | Prêt |
| L'ordonnanceur donne le processeur au processus (mise en exécution) | ... | ... |
| Le quantum de temps est écoulé, le processus n'est pas terminé | ... | ... |
| Le processus demande une ressource qui n'est pas disponible (blocage) | ... | ... |
| La ressource attendue devient disponible (déblocage) | ... | ... |
| Le processus a fini son exécution | ... | ... |

**Question 3** (0,5 pt)

- a) Un processus bloqué peut-il passer directement à l'état « élu » ? Justifier.
- b) Combien de processus peuvent être à l'état « élu » en même temps sur ce processeur ?

---

## Partie B — Chronogramme (5 points)

On considère cinq processus dont les caractéristiques sont données ci-dessous. Les durées et les instants sont exprimés en **unités de temps**.

| Processus | P1 | P2 | P3 | P4 | P5 |
|---|:---:|:---:|:---:|:---:|:---:|
| Instant d'arrivée | 0 | 1 | 2 | 3 | 6 |
| Durée d'exécution | 5 | 3 | 6 | 2 | 4 |

L'ordonnanceur applique l'algorithme du **tourniquet** avec un **quantum de 1 unité de temps**, selon les règles suivantes :

1. Les processus prêts sont rangés dans une **file d'attente**.
2. Le processeur est attribué au premier processus de la file pendant **1 unité de temps** (le quantum).
3. Au bout de cette unité de temps, si le processus n'est pas terminé, il est **remis à la fin de la file** ; s'il est terminé, il quitte le système.
4. Si un nouveau processus arrive **à l'instant même** où un autre est interrompu, le nouvel arrivant est placé dans la file **avant** le processus interrompu.
5. Le temps de changement de processus est négligé.

**Question 4** (3 pts) — Recopier et compléter le chronogramme ci-dessous en marquant d'une croix la case du processus élu pendant chaque unité de temps. La colonne `t` correspond à l'intervalle de temps [t ; t+1[.

| |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| P1 | | | | | | | | | | | | | | | | | | | | |
| P2 | | | | | | | | | | | | | | | | | | | | |
| P3 | | | | | | | | | | | | | | | | | | | | |
| P4 | | | | | | | | | | | | | | | | | | | | |
| P5 | | | | | | | | | | | | | | | | | | | | |

**Question 5** (1 pt) — Donner l'état de chacun des cinq processus aux instants t = 5 et t = 9 (pendant les intervalles [5 ; 6[ et [9 ; 10[).

**Question 6** (1 pt) — Le **temps d'attente** d'un processus est le temps total qu'il passe à l'état « prêt » (dans la file d'attente) :

temps d'attente = (instant de fin − instant d'arrivée) − durée d'exécution.

Calculer le temps d'attente de chaque processus, puis le temps d'attente moyen.

---

## Partie C — Modélisation d'un processus (4 points)

On modélise un processus par la classe `Processus`, dont les objets possèdent les attributs suivants :

- `pid` : l'identifiant du processus (entier) ;
- `arrivee` : son instant d'arrivée ;
- `duree` : sa durée totale d'exécution ;
- `reste_a_faire` : le nombre d'unités de temps qu'il lui reste à exécuter (initialement égal à `duree`) ;
- `etat` : son état, une chaîne de caractères (`"Nouveau"`, `"Prêt"`, `"Élu"`, `"Bloqué"` ou `"Terminé"`), initialement `"Nouveau"`.

**Question 7** (2 pts) — Écrire le constructeur `__init__(self, pid, arrivee, duree)` de la classe `Processus`.

**Question 8** (1,5 pt) — Écrire les trois méthodes suivantes de la classe `Processus` :

- `execute_un_cycle(self)` : met à jour `reste_a_faire` après l'exécution d'une unité de temps ;
- `change_etat(self, nouvel_etat)` : change l'état du processus ;
- `est_termine(self)` : renvoie `True` si le processus a fini son exécution, `False` sinon.

**Question 9** (0,5 pt) — Écrire l'instruction qui crée une liste `processus` contenant les cinq objets de la partie B, dans l'ordre de leur instant d'arrivée.

---

## Partie D — Modélisation de l'ordonnanceur (8 points)

On modélise l'ordonnanceur par une classe `RoundRobin`. On dispose de la classe `File` dont l'interface est la suivante :

- `File()` : crée et renvoie une file vide ;
- `enfiler(self, e)` : ajoute l'élément `e` à la fin de la file ;
- `defiler(self)` : renvoie, en le supprimant, le premier élément de la file ;
- `est_vide(self)` : renvoie `True` si la file est vide, `False` sinon.

Un objet de la classe `RoundRobin` possède les attributs suivants :

- `quantum` : la durée du quantum (entier) ;
- `a_venir` : la liste des processus qui ne sont pas encore arrivés, **triée par instant d'arrivée croissant** ;
- `file` : la file (objet de type `File`) des processus à l'état « prêt » ;
- `temps` : l'horloge du système (entier), initialement égale à 0 ;
- `chronogramme` : la liste des `pid` des processus exécutés, un élément par unité de temps (la valeur `None` est utilisée si le processeur est inactif).

**Question 10** (1 pt) — Pourquoi une **file** est-elle la structure adaptée pour mémoriser les processus prêts ? Pourquoi une pile ne conviendrait-elle pas ?

**Question 11** (1 pt) — Écrire le constructeur `__init__(self, quantum, processus)`. Le paramètre `processus` est la liste de tous les processus, triée par instant d'arrivée. On veillera à ne pas modifier la liste passée en paramètre.

**Question 12** (1,5 pt) — Écrire la méthode `admettre_arrivees(self)` qui fait entrer dans la file, à l'état « prêt », tous les processus de `a_venir` dont l'instant d'arrivée est inférieur ou égal à l'horloge. On pourra utiliser `liste.pop(0)`.

**Question 13** (2 pts) — Écrire la méthode `executer(self, p)` qui fait exécuter le processus `p` (déjà retiré de la file) pendant un quantum au plus :

- `p` passe à l'état « élu » ;
- à chaque unité de temps, son `pid` est ajouté au chronogramme, `p` exécute un cycle et l'horloge avance de 1 ;
- on s'arrête quand le quantum est écoulé **ou** quand `p` est terminé ;
- on admet alors les processus qui viennent d'arriver, puis `p` passe à l'état « terminé », ou bien à l'état « prêt » et il est remis à la fin de la file.

**Question 14** (2 pts) — Écrire la méthode `simuler(self)` qui exécute l'algorithme jusqu'à la fin de tous les processus et renvoie le chronogramme.

*Attention : la file peut être vide alors que certains processus ne sont pas encore arrivés. Le processeur est alors inactif : on ajoute `None` au chronogramme et l'horloge avance de 1.*

**Question 15** (0,5 pt) — Écrire le programme principal qui crée l'ordonnanceur de quantum 1 avec les cinq processus de la partie B et affiche le résultat de `simuler()`. Donner la valeur affichée.

**Squelette fourni :**

```python
class RoundRobin:
    def __init__(self, quantum, processus):
        """Crée un ordonnanceur de quantum donné pour la liste de processus
        (triée par instant d'arrivée)."""
        ...

    def admettre_arrivees(self):
        """Met dans la file, à l'état Prêt, les processus arrivés à l'instant courant."""
        ...

    def executer(self, p):
        """Fait exécuter le processus p pendant un quantum au plus."""
        ...

    def simuler(self):
        """Simule l'ordonnancement complet et renvoie le chronogramme."""
        ...
```

<!-- ===================== ÉNONCÉ : FIN ===================== -->

---
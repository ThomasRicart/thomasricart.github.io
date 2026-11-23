<!-- ===================== CORRIGÉ : DÉBUT ===================== -->

# <span style="color:red">RÉVISION NSI — Round Robin</span> : corrigé

## Partie A — États d'un processus

**Question 1**

Les états sont : **Nouveau** (création), **Prêt**, **Élu** (en cours d'exécution), **Bloqué** (en attente d'une ressource) et **Terminé**.

**Question 2**

| Événement | État de départ | État d'arrivée |
|---|:---:|:---:|
| Le processus est créé puis admis | Nouveau | Prêt |
| Mise en exécution | Prêt | Élu |
| Quantum écoulé, processus non terminé | Élu | Prêt |
| Blocage (ressource indisponible) | Élu | Bloqué |
| Déblocage (ressource disponible) | Bloqué | Prêt |
| Fin de l'exécution | Élu | Terminé |

**Question 3**

- a) **Non.** Un processus débloqué repasse d'abord à l'état « prêt ». Seul l'ordonnanceur peut ensuite l'élire.
- b) **Un seul** : le processeur n'a qu'un cœur, donc un seul processus s'exécute à un instant donné.

---

## Partie B — Chronogramme

**Question 4**

| |0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| P1 |■| |■| | | |■| | | | |■| | |■| | | | | |
| P2 | |■| | |■| | | |■| | | | | | | | | | | |
| P3 | | | |■| | | |■| | | | |■| | |■| |■| |■|
| P4 | | | | | |■| | | | |■| | | | | | | | | |
| P5 | | | | | | | | | |■| | | |■| | |■| |■| |

Déroulement. La colonne « File » donne la file d'attente **à l'instant t, avant l'élection** (la tête de file est à gauche), nouveaux arrivants compris :

| Instant t | File | Élu | Reste à faire après | Remarque |
|:---:|---|:---:|:---:|---|
| 0 | P1 | P1 | 4 | |
| 1 | P2, P1 | P2 | 2 | P2 arrive à t = 1 : il passe **avant** P1 (règle 4) |
| 2 | P1, P3, P2 | P1 | 3 | P3 arrive à t = 2 : il passe avant P2 |
| 3 | P3, P2, P4, P1 | P3 | 5 | P4 arrive à t = 3 : il passe avant P1 |
| 4 | P2, P4, P1, P3 | P2 | 1 | |
| 5 | P4, P1, P3, P2 | P4 | 1 | |
| 6 | P1, P3, P2, P5, P4 | P1 | 2 | P5 arrive à t = 6 : il passe avant P4 |
| 7 | P3, P2, P5, P4, P1 | P3 | 4 | |
| 8 | P2, P5, P4, P1, P3 | P2 | 0 | **P2 terminé** (fin à t = 9) |
| 9 | P5, P4, P1, P3 | P5 | 3 | |
| 10 | P4, P1, P3, P5 | P4 | 0 | **P4 terminé** (fin à t = 11) |
| 11 | P1, P3, P5 | P1 | 1 | |
| 12 | P3, P5, P1 | P3 | 3 | |
| 13 | P5, P1, P3 | P5 | 2 | |
| 14 | P1, P3, P5 | P1 | 0 | **P1 terminé** (fin à t = 15) |
| 15 | P3, P5 | P3 | 2 | |
| 16 | P5, P3 | P5 | 1 | |
| 17 | P3, P5 | P3 | 1 | |
| 18 | P5, P3 | P5 | 0 | **P5 terminé** (fin à t = 19) |
| 19 | P3 | P3 | 0 | **P3 terminé** (fin à t = 20) |

La durée totale est de 20 unités de temps : 5 + 3 + 6 + 2 + 4 = 20, donc le processeur n'a jamais été inactif.

**Question 5**

| Instant | P1 | P2 | P3 | P4 | P5 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| t = 5 | Prêt | Prêt | Prêt | **Élu** | **Nouveau** (il n'arrive qu'à t = 6) |
| t = 9 | Prêt | **Terminé** (fin à t = 9) | Prêt | Prêt | **Élu** |

**Question 6**

| Processus | Fin | Fin − arrivée | Durée | Temps d'attente |
|:---:|:---:|:---:|:---:|:---:|
| P1 | 15 | 15 | 5 | 10 |
| P2 | 9 | 8 | 3 | 5 |
| P3 | 20 | 18 | 6 | 12 |
| P4 | 11 | 8 | 2 | 6 |
| P5 | 19 | 13 | 4 | 9 |

Temps d'attente moyen = (10 + 5 + 12 + 6 + 9) / 5 = 42 / 5 = **8,4 unités de temps**.

---

## Partie C — Classe `Processus`

**Question 7**

```python
class Processus:
    def __init__(self, pid, arrivee, duree):
        """Crée un processus à l'état Nouveau, avec toute sa durée restant à exécuter."""
        self.pid = pid
        self.arrivee = arrivee
        self.duree = duree
        self.reste_a_faire = duree
        self.etat = "Nouveau"
```

**Question 8**

```python
    def execute_un_cycle(self):
        """Met à jour le reste à faire après l'exécution d'une unité de temps."""
        self.reste_a_faire = self.reste_a_faire - 1

    def change_etat(self, nouvel_etat):
        """Change l'état du processus avec la valeur passée en paramètre."""
        self.etat = nouvel_etat

    def est_termine(self):
        """Renvoie True si le processus a fini son exécution, False sinon."""
        return self.reste_a_faire == 0
```

**Question 9**

```python
processus = [Processus(1, 0, 5), Processus(2, 1, 3), Processus(3, 2, 6),
             Processus(4, 3, 2), Processus(5, 6, 4)]
```

---

## Partie D — Classe `RoundRobin`

**Question 10**

Dans le tourniquet, les processus sont servis **dans l'ordre où ils sont arrivés** dans la file : le premier arrivé est le premier servi (FIFO). Un processus interrompu est remis **à la fin**, ce qui garantit que tous les processus passent à tour de rôle. C'est exactement le fonctionnement d'une file (`enfiler` à la fin, `defiler` au début). Avec une pile (LIFO), le dernier arrivé serait toujours servi en premier : les processus les plus anciens risqueraient de ne jamais s'exécuter (famine).

**Question 11**

```python
class RoundRobin:
    def __init__(self, quantum, processus):
        """Crée un ordonnanceur de quantum donné pour la liste de processus
        (triée par instant d'arrivée)."""
        self.quantum = quantum
        self.a_venir = list(processus)   # copie : la liste de l'appelant n'est pas modifiée
        self.file = File()
        self.temps = 0
        self.chronogramme = []
```

**Question 12**

```python
    def admettre_arrivees(self):
        """Met dans la file, à l'état Prêt, les processus arrivés à l'instant courant."""
        while self.a_venir != [] and self.a_venir[0].arrivee <= self.temps:
            p = self.a_venir.pop(0)
            p.change_etat("Prêt")
            self.file.enfiler(p)
```

**Question 13**

```python
    def executer(self, p):
        """Fait exécuter le processus p pendant un quantum au plus."""
        p.change_etat("Élu")
        compteur = 0
        while compteur < self.quantum and not p.est_termine():
            self.chronogramme.append(p.pid)
            p.execute_un_cycle()
            self.temps = self.temps + 1
            compteur = compteur + 1
        self.admettre_arrivees()          # les nouveaux arrivés passent AVANT p (règle 4)
        if p.est_termine():
            p.change_etat("Terminé")
        else:
            p.change_etat("Prêt")
            self.file.enfiler(p)          # p est remis à la fin de la file
```

L'appel à `admettre_arrivees()` doit se faire **avant** la remise de `p` dans la file : c'est ce qui respecte la règle 4 (à t = 1, P2 passe avant P1 ; à t = 2, P3 avant P2 ; à t = 3, P4 avant P1 ; à t = 6, P5 avant P4).

**Question 14**

```python
    def simuler(self):
        """Simule l'ordonnancement complet et renvoie le chronogramme."""
        self.admettre_arrivees()
        while self.a_venir != [] or not self.file.est_vide():
            if self.file.est_vide():
                # aucun processus prêt : le processeur est inactif pendant une unité
                self.chronogramme.append(None)
                self.temps = self.temps + 1
                self.admettre_arrivees()
            else:
                p = self.file.defiler()
                self.executer(p)
        return self.chronogramme
```

**Question 15**

```python
processus = [Processus(1, 0, 5), Processus(2, 1, 3), Processus(3, 2, 6),
             Processus(4, 3, 2), Processus(5, 6, 4)]
ordonnanceur = RoundRobin(1, processus)
print(ordonnanceur.simuler())
```

Valeur affichée (une valeur par unité de temps, elle correspond au chronogramme de la question 4) :

```text
[1, 2, 1, 3, 2, 4, 1, 3, 2, 5, 4, 1, 3, 5, 1, 3, 5, 3, 5, 3]
```

### Pour tester sur machine (facultatif)

Une écriture possible de la classe `File`, si elle n'est pas déjà définie :

```python
class File:
    def __init__(self):
        """Crée une file vide."""
        self.contenu = []

    def enfiler(self, e):
        """Ajoute l'élément e à la fin de la file."""
        self.contenu.append(e)

    def defiler(self):
        """Renvoie et supprime le premier élément de la file."""
        return self.contenu.pop(0)

    def est_vide(self):
        """Renvoie True si la file est vide, False sinon."""
        return self.contenu == []
```

### Erreurs fréquentes à surveiller

- Oublier la transition **Élu → Prêt** (fin de quantum) dans le tableau des états.
- Remettre le processus interrompu dans la file **avant** le nouvel arrivant (violation de la règle 4). Avec un quantum de 1, cette règle intervient quatre fois (t = 1, 2, 3 et 6) : la moindre erreur fausse tout le reste du chronogramme.
- Confondre l'état « Nouveau » (pas encore arrivé) et l'état « Prêt » (arrivé, dans la file).
- Oublier la remise à 0 du compteur du quantum à chaque nouveau processus élu.
- Ne pas traiter le cas de la file vide alors que des processus n'ont pas encore démarré : sans ce traitement, la boucle principale ne se termine jamais.

<!-- ===================== CORRIGÉ : FIN ===================== -->
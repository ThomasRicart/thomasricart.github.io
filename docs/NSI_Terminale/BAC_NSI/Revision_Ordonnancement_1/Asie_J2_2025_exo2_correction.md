<!-- ===================== SUJET 1 : DÉBUT ===================== -->

# <span style="color:red">ASIE J2 2025</span> — Exercice 2 : ordonnancement avec priorités

**Notions :** ordonnanceur, états d'un processus, files, programmation objet, famine et vieillissement.
**Difficulté :** soutenue (la question 10 est la plus délicate).

**Convention de représentation** (elle se déduit de la simulation de la question 5) : chaque file est une liste Python dont la **tête** (le processus arrivé le premier, donc le prochain à être élu) est **à droite**.

- enfiler un processus `p` : `file.insert(0, p)` ;
- défiler : `file.pop()`.

## Question 1

Ce programme est un **ordonnanceur** (*scheduler*). C'est la partie du système d'exploitation qui décide quel processus prêt reçoit le processeur.

## Question 2

États possibles d'un processus :

- **nouveau** : le processus vient d'être créé ;
- **prêt** : il attend que le processeur soit libre ;
- **élu** (en cours d'exécution) : il utilise le processeur ;
- **bloqué** (en attente) : il attend une ressource (entrée/sortie, par exemple) ;
- **terminé**.

## Question 3

**Proposition 2 : la file.** Pour une même priorité, les processus doivent être servis dans l'ordre d'arrivée (*premier arrivé, premier servi*, structure FIFO). Une pile (LIFO) ferait passer les derniers arrivés devant les plus anciens. Une liste n'impose aucune discipline d'accès.

## Question 4

```python
class Processus:
    def __init__(self, PID, priorite, temps_CPU):
        """Constructeur : crée un processus de priorité et de durée données."""
        self.priorite = priorite
        self.PID = PID
        self.temps_utilisation = 0
        self.temps_CPU = temps_CPU
```

## Question 5

```text
Cycle 3 : CPU=P3  liste_files=[[], [P2, P1], []]
Cycle 4 : CPU=P3  liste_files=[[], [P2, P1], []]
Cycle 5 : CPU=P1  liste_files=[[], [P2], [P3]]
```

Justification :

- **Cycle 3** : P2 (priorité 0) a utilisé un cycle et P3 (priorité 0) attend. Une priorité « supérieure ou égale » attend, donc P2 passe à la priorité 1 et rejoint la file 1 *derrière* P1, ce qui donne `[P2, P1]`. P3 est élu.
- **Cycle 4** : les processus en attente (P2 et P1) ont la priorité 1, donc ils sont *moins* prioritaires que P3 (priorité 0). Il n'y a pas de préemption : P3 passe à la priorité 1 mais **reste sur le processeur**. La file d'indice 2 est toujours vide.
- **Cycle 5** : P3 (priorité 1) est en concurrence avec P1 et P2 (priorité 1, donc priorité égale). P3 est retiré, passe à la priorité 2 et va dans la file 2. P1 est en tête de la file 1 (arrivé avant P2), il est élu.

## Question 6

À chaque cycle où il s'exécute, le processus long voit sa priorité augmenter de 1 (elle ne redescend jamais). Après quelques cycles, sa priorité vaut donc au moins 5.

Un processus court (4 cycles) se termine avant de dépasser la priorité 4. Chaque processus terminé étant remplacé par un nouveau, qui arrive avec la priorité 0, il y a **toujours** dans les files un processus plus prioritaire que le processus long. Celui-ci n'est plus jamais élu : c'est la **famine** (*starvation*).

## Question 7

Avec `temps_d_attente`, un processus qui attend plus de `Max_Temps` cycles voit sa priorité remonter d'un niveau (sa valeur diminue de 1), et son temps d'attente est remis à 0.

Le processus long remonte donc régulièrement de file. Au bout d'un temps fini, il retrouve la priorité 0 comme les nouveaux arrivants. Comme il est dans la file depuis plus longtemps, il est devant eux (structure FIFO) et finit par être élu. Il reçoit ainsi régulièrement le processeur et finira par se terminer. Cette technique s'appelle le **vieillissement** (*aging*).

## Question 8

```python
def meilleur_priorite(liste_files):
    """Renvoie la priorité (indice de la file non vide la plus prioritaire),
    ou None s'il n'y a plus aucun processus en attente."""
    for i in range(len(liste_files)):
        if liste_files[i] != []:
            return i
    return None
```

## Question 9

```python
def prioritaire(liste_files):
    """Renvoie un des processus les plus prioritaires (le plus ancien de sa file)
    en le supprimant de sa file, ou None si toutes les files sont vides."""
    mp = meilleur_priorite(liste_files)
    if mp is None:
        return None
    return liste_files[mp].pop()   # la tête de file est à la fin de la liste
```

## Question 10

```python
def gerer(p, liste_files):
    """Simule un cycle d'horloge.
    p : processus en cours d'exécution (ou None s'il n'y en a pas).
    liste_files : liste des files d'attente (indice = priorité).
    Renvoie le processus en cours d'exécution après ce cycle (ou None)."""
    if p is None:
        # aucun processus en cours : on élit le plus prioritaire (None s'il n'en reste plus)
        return prioritaire(liste_files)
    if p.temps_utilisation >= p.temps_CPU:
        # le processus a terminé : on le retire du processeur
        return None
    p.temps_utilisation = p.temps_utilisation + 1
    meilleure = meilleur_priorite(liste_files)
    # un processus de priorité supérieure ou égale attend-il ? (on teste AVANT de dégrader p)
    doit_ceder = meilleure is not None and meilleure <= p.priorite
    # on réduit la priorité de p (valeur + 1), sans dépasser la dernière file existante
    p.priorite = min(p.priorite + 1, len(liste_files) - 1)
    if doit_ceder:
        liste_files[p.priorite].insert(0, p)   # p rejoint la fin de sa nouvelle file
        return prioritaire(liste_files)        # on élit un autre processus
    return p                                   # sinon p continue
```

**Remarque.** Le `min(...)` évite un `IndexError` : sans lui, un processus qui s'exécute longtemps dépasserait le nombre de files de la liste (trois dans l'exemple).

### Pour vérifier avec Python (facultatif)

```python
def simulation(liste_files, nb_cycles):
    """Affiche, cycle par cycle, le processus élu et l'état des files."""
    cpu = None
    for cycle in range(1, nb_cycles + 1):
        cpu = gerer(cpu, liste_files)
        print("Cycle", cycle, ": CPU =", cpu, "liste_files =", liste_files)

# Pour un affichage lisible, ajouter dans la classe Processus :
#     def __repr__(self):
#         """Représentation du processus : P suivi du PID."""
#         return "P" + str(self.PID)
P1 = Processus(1, 0, 10)
P2 = Processus(2, 0, 7)
P3 = Processus(3, 0, 5)
simulation([[P3, P2, P1], [], []], 5)
```

<!-- ===================== SUJET 1 : FIN ===================== -->
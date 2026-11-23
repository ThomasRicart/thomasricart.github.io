<!-- ===================== SUJET 3 : DÉBUT ===================== -->

# <span style="color:red">POLYNESIE J1 2023</span> — Exercice 2 : ordonnancement par tourniquet

**Notions :** ordonnancement *round robin*, quantum, file d'attente simulée par une liste, POO.
**Difficulté :** directement dans le cours.

## Question 1

**a)** Quantum = 1. La file contient initialement 11 (4 cycles), 20 (2 cycles) et 32 (3 cycles). On fait des « tours » successifs :

- tour 1 : 11, 20, 32 (il reste 3, 1 et 2 cycles) ;
- tour 2 : 11, 20, 32 (le 20 se termine ; il reste 2 et 1 cycles) ;
- tour 3 : 11, 32 (le 32 se termine ; il reste 1 cycle pour le 11) ;
- tour 4 : 11.

```text
11, 20, 32, 11, 20, 32, 11, 32, 11
```

**b)** Quantum = 2 :

- 11 s'exécute 2 cycles (il lui en reste 2) et va en fin de file ;
- 20 s'exécute 2 cycles et se termine ;
- 32 s'exécute 2 cycles (il lui en reste 1) et va en fin de file ;
- 11 s'exécute 2 cycles et se termine ;
- 32 s'exécute 1 cycle et se termine.

```text
11, 11, 20, 20, 32, 32, 11, 11, 32
```

## Question 2

**a)**

```python
liste_attente = [Processus(11, 4), Processus(20, 2), Processus(32, 3)]
```

**b)**

```python
    def execute_un_cycle(self):
        """Met à jour le reste à faire après l'exécution d'un cycle."""
        self.reste_a_faire = self.reste_a_faire - 1

    def change_etat(self, nouvel_etat):
        """Change l'état du processus avec la valeur passée en paramètre."""
        self.etat = nouvel_etat

    def est_termine(self):
        """Renvoie True si le processus est terminé, False sinon."""
        return self.reste_a_faire == 0
```

**c)**

```python
def tourniquet(liste_attente, quantum):
    """Renvoie la liste des PID dans l'ordre d'exécution par le processeur
    (ordonnancement du tourniquet)."""
    ordre_execution = []
    while liste_attente != []:
        # On extrait le premier processus
        processus = liste_attente.pop(0)
        processus.change_etat("En cours d'exécution")
        compteur_tourniquet = 0
        while compteur_tourniquet < quantum and not processus.est_termine():
            ordre_execution.append(processus.pid)
            processus.execute_un_cycle()
            compteur_tourniquet = compteur_tourniquet + 1
        if not processus.est_termine():
            processus.change_etat("Suspendu")
            liste_attente.append(processus)      # retour en fin de file
        else:
            processus.change_etat("Terminé")
    return ordre_execution
```

Le test de la boucle interne a deux conditions : le quantum n'est pas épuisé **et** le processus n'est pas fini. Un processus qui termine avant la fin de son quantum libère donc le processeur immédiatement, comme le 32 à la question 1.b.

**Remarque (lien avec le cours sur les files).** `liste_attente.pop(0)` décale tous les éléments de la liste (coût linéaire). Avec la classe `File` vue en cours, `defiler()` serait plus naturel.

<!-- ===================== SUJET 3 : FIN ===================== -->
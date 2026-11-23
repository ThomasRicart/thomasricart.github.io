<!-- ===================== ÉNONCÉ : DÉBUT ===================== -->

# <span style="color:red">SYNTHÈSE RÉCURSIVITÉ — Suites, listes et dichotomie</span> : énoncé

**Exercice (14 points)** — Cet exercice porte sur la **récursivité** classique : cas de base, réduction du problème, justification de la terminaison, trace d'exécution et conception d'algorithmes récursifs.

---

## Partie 1 — Récursivité sur une suite numérique (4 points)

On considère la suite $(u_n)_{n \ge 0}$ définie par :

- $u_0 = 3$ ;
- pour tout entier naturel $n$, $u_{n+1} = 2u_n - 1$.

**Question 1** (1 pt) — Calculer à la main $u_1$, $u_2$ et $u_3$.

**Question 2** (1,5 pt) — Écrire une fonction récursive `terme(n)` qui prend en paramètre un entier naturel `n` et renvoie la valeur de $u_n$.

**Question 3** (1,5 pt) — Quel appel récursif de `terme(n)` déclenche le cas de base ? 

**Question 4** (1,5 pt) — En prenant $n=4$, compléter le tableau ci-dessous pour montrer la suite des appels récursifs et des valeurs renvoyées par `terme(n)`.
| Fonction évaluée | Return | Valeur renvoyée |
|----------------|----------------|-----------------|
|  terme(4)      |                | 33|
|       |                ||
|        |                ||
|        |               ||
|        |              ||

**Question 5** (1,5 pt) — Justifier rigoureusement que l'appel `terme(n)` **termine** pour tout entier naturel `n`.

---

## Partie 2 — Récursivité sur des listes (5 points)

**Question 6** (1,5 pt) — Écrire une fonction récursive `est_present(x, lst)` qui renvoie `True` si la valeur `x` est présente dans la liste `lst`, et `False` sinon. On considère que la liste peut être vide.

```python
def est_present(x, lst):
    ''' Renvoie True si x est présent dans lst, False sinon.'''

assert est_present(3, [1, 2, 3, 4]) == True
assert est_present(5, [1, 2, 3, 4]) == False
```

**Question 7** (1,5 pt) — Écrire une fonction récursive `est_triee(lst)` qui renvoie `True` si la liste `lst` de nombres est triée par ordre croissant au sens large (chaque élément est supérieur ou égal au précédent), et `False` sinon. On considère qu'une liste vide ou à un seul élément est triée.

```python
def est_triee(lst):
    ''' Renvoie True si lst est triée par ordre croissant (au sens large), False sinon.'''

assert est_triee([]) == True
assert est_triee([7]) == True
assert est_triee([1, 2, 2, 5]) == True
assert est_triee([1, 4, 3]) == False
``` 

**Question 8** (1,5 pt) — Écrire une fonction récursive `compter_occurrences(lst, cible)` qui renvoie le nombre de fois où la valeur `cible` apparaît dans la liste `lst`.

```python
def compter_occurrences(lst, cible):
    ''' Renvoie le nombre de fois où cible apparaît dans lst.'''

assert compter_occurrences([1, 3, 2, 3, 3, 4], 3) == 3
assert compter_occurrences([1, 2, 4], 3) == 0
```

**Question 9** (2 pts) — Écrire une fonction récursive `somme_pairs(lst)` qui renvoie la somme de tous les nombres **pairs** présents dans la liste `lst` d'entiers (renvoyant `0` s'il n'y en a aucun).

```python
def somme_pairs(lst):
    ''' Renvoie la somme des entiers pairs de lst.'''

assert somme_pairs([1, 2, 3, 4, 5, 6]) == 12
assert somme_pairs([1, 3, 5]) == 0
```
*Rappel : en Python, un entier `x` est pair lorsque `x % 2 == 0`.*

---

## Partie 3 — Synthèse : recherche dichotomique récursive (5 points)

On dispose d'une **liste triée par ordre croissant** `tab` de nombres et d'une valeur `x` recherchée. Plutôt que de parcourir toute la liste, on utilise une **recherche dichotomique récursive** avec deux indices `gauche` et `droite` (inclus), sans recopier de sous-listes.

À chaque étape :

- si `gauche` est strictement supérieur à `droite`, l'intervalle est vide : on renvoie `-1` ;
- sinon, on calcule l'indice du milieu `milieu = (gauche + droite) // 2` :
  - si `tab[milieu] == x`, on a trouvé : on renvoie `milieu` ;
  - si `tab[milieu] < x`, on cherche dans la moitié droite ;
  - sinon (`tab[milieu] > x`), on cherche dans la moitié gauche.

**Question 10** (2 pt) — Écrire la fonction `recherche_dicho_rec(tab, x, gauche, droite)` qui renvoie un indice où `x` apparaît dans `tab[gauche : droite + 1]`, ou `-1` s'il n'y est pas.
```def recherche_dicho_rec(tab, x, gauche, droite):
    ''' Recherche dichotomique récursive de x dans tab entre les indices gauche et droite.'''

assert recherche_dicho_rec([2, 5, 8, 12, 16, 23, 38], 16, 0, 6) == 4
assert recherche_dicho_rec([2, 5, 8, 12, 16, 23, 38], 2, 0, 6) == 0
assert recherche_dicho_rec([2, 5, 8, 12, 16, 23, 38], 38, 0, 6) == 6
assert recherche_dicho_rec([2, 5, 8, 12, 16, 23, 38], 99, 0, 6) == -1
```

**Question 11** (1,5 pt) — On considère `tab = [2, 5, 8, 12, 16, 23, 38]` et on appelle `recherche_dicho_rec(tab, 16, 0, 6)`. Donner la suite des valeurs prises par `gauche`, `droite` et `milieu` à chaque appel récursif, puis la valeur renvoyée.

**Question 12** (1,5 pt) — Expliquer pourquoi la taille de l'intervalle de recherche diminue strictement à chaque appel récursif lorsque l'on ne trouve pas `tab[milieu] == x`, et en déduire la terminaison de l'algorithme.

<!-- ===================== ÉNONCÉ : FIN ===================== -->

---
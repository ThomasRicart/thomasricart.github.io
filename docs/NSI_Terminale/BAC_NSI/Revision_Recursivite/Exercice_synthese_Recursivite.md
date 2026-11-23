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

**Question 8** (2 pts) — Écrire une fonction récursive `somme_pairs(lst)` qui renvoie la somme de tous les nombres **pairs** présents dans la liste `lst` d'entiers (renvoyant `0` s'il n'y en a aucun).

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

**Question 7** (2 pt) — Écrire la fonction `recherche_dicho_rec(tab, x, gauche, droite)` qui renvoie un indice où `x` apparaît dans `tab[gauche : droite + 1]`, ou `-1` s'il n'y est pas.

**Question 8** (1,5 pt) — On considère `tab = [2, 5, 8, 12, 16, 23, 38]` et on appelle `recherche_dicho_rec(tab, 16, 0, 6)`. Donner la suite des valeurs prises par `gauche`, `droite` et `milieu` à chaque appel récursif, puis la valeur renvoyée.

**Question 9** (1,5 pt) — Expliquer pourquoi la taille de l'intervalle de recherche diminue strictement à chaque appel récursif lorsque l'on ne trouve pas `tab[milieu] == x`, et en déduire la terminaison de l'algorithme.

<!-- ===================== ÉNONCÉ : FIN ===================== -->

---

<!-- ===================== CORRIGÉ : DÉBUT ===================== -->

# <span style="color:red">SYNTHÈSE RÉCURSIVITÉ — Suites, listes et dichotomie</span> : corrigé

## Partie 1 — Récursivité sur une suite numérique

**Question 1**

- $u_1 = 2 \times 3 - 1 = 5$
- $u_2 = 2 \times 5 - 1 = 9$
- $u_3 = 2 \times 9 - 1 = 17$

**Question 2**

```python
def terme(n):
    """Renvoie le terme u_n de la suite définie par u_0 = 3 et u_{k+1} = 2*u_k - 1."""
    if n == 0:
        return 3
    return 2 * terme(n - 1) - 1
```

**Question 3**

Pour tout entier naturel `n` donné en entrée :

- si `n == 0`, le cas de base est atteint immédiatement sans appel récursif ;
- si `n > 0`, chaque appel récursif fait diminuer `n` de `1` (`n - 1`). Comme `n` est un entier positif qui décroît strictement de `1` à chaque étape, il atteint nécessairement `0` en un nombre fini d'étapes (`n` appels), ce qui déclenche le cas de base et garantit la terminaison.

---

## Partie 2 — Récursivité sur des listes

**Question 4**

```python
def est_triee(lst):
    """Renvoie True si lst est triée par ordre croissant (au sens large), False sinon."""
    if len(lst) <= 1:
        return True
    if lst[0] > lst[1]:
        return False
    return est_triee(lst[1:])
```

**Question 5**

```python
def compter_occurrences(lst, cible):
    """Renvoie le nombre de fois où cible apparaît dans lst."""
    if lst == []:
        return 0
    reste = compter_occurrences(lst[1:], cible)
    if lst[0] == cible:
        return 1 + reste
    return reste
```

**Question 6**

```python
def somme_pairs(lst):
    """Renvoie la somme des entiers pairs de lst."""
    if lst == []:
        return 0
    reste = somme_pairs(lst[1:])
    if lst[0] % 2 == 0:
        return lst[0] + reste
    return reste
```

---

## Partie 3 — Synthèse : recherche dichotomique récursive

**Question 7**

```python
def recherche_dicho_rec(tab, x, gauche, droite):
    """Recherche dichotomique récursive de x dans tab entre les indices gauche et droite."""
    if gauche > droite:
        return -1
    milieu = (gauche + droite) // 2
    if tab[milieu] == x:
        return milieu
    if tab[milieu] < x:
        return recherche_dicho_rec(tab, x, milieu + 1, droite)
    return recherche_dicho_rec(tab, x, gauche, milieu - 1)
```

**Question 8**

Avec `tab = [2, 5, 8, 12, 16, 23, 38]` et `x = 16` :

- **Appel 1 :** `gauche = 0`, `droite = 6` $\implies$ `milieu = (0 + 6) // 2 = 3`. `tab[3]` vaut `12` (`12 < 16`) : appel suivant avec `gauche = 4`, `droite = 6`.
- **Appel 2 :** `gauche = 4`, `droite = 6` $\implies$ `milieu = (4 + 6) // 2 = 5`. `tab[5]` vaut `23` (`23 > 16`) : appel suivant avec `gauche = 4`, `droite = 4`.
- **Appel 3 :** `gauche = 4`, `droite = 4` $\implies$ `milieu = (4 + 4) // 2 = 4`. `tab[4]` vaut `16` (`16 == 16`) : trouvé.

La fonction renvoie **`4`**.

**Question 9**

Lorsque `tab[milieu] != x`, l'indice `milieu` est exclu du nouvel intervalle :

- soit `gauche` devient `milieu + 1` (strictement supérieur à l'ancien `gauche`, car `milieu <= droite`) ;
- soit `droite` devient `milieu - 1` (strictement inférieur à l'ancien `droite`, car `gauche <= milieu`).

Dans les deux cas, la quantité `droite - gauche` diminue strictement d'au moins `1` à chaque appel récursif. Comme `droite - gauche` est un entier qui décroît strictement, on atteint nécessairement soit `tab[milieu] == x` (arrêt par succès), soit `gauche > droite` (arrêt sur intervalle vide, renvoyant `-1`). L'algorithme termine donc toujours.

### Pour tester sur machine (facultatif)

```python
assert terme(0) == 3
assert terme(1) == 5
assert terme(2) == 9
assert terme(3) == 17

assert est_triee([]) is True
assert est_triee([7]) is True
assert est_triee([1, 2, 2, 5]) is True
assert est_triee([1, 4, 3]) is False

assert compter_occurrences([1, 3, 2, 3, 3, 4], 3) == 3
assert compter_occurrences([1, 2, 4], 3) == 0
assert compter_occurrences([], 3) == 0

assert somme_pairs([1, 2, 3, 4, 5, 6]) == 12
assert somme_pairs([1, 3, 5]) == 0
assert somme_pairs([]) == 0

tab = [2, 5, 8, 12, 16, 23, 38]
assert recherche_dicho_rec(tab, 16, 0, len(tab) - 1) == 4
assert recherche_dicho_rec(tab, 2, 0, len(tab) - 1) == 0
assert recherche_dicho_rec(tab, 38, 0, len(tab) - 1) == 6
assert recherche_dicho_rec(tab, 99, 0, len(tab) - 1) == -1
print("tous les tests passent")
```

### Erreurs fréquentes à surveiller

- **Oublier le cas de base** ou ne pas faire décroître le paramètre (`terme(n)` au lieu de `terme(n - 1)`, ou `lst` au lieu de `lst[1:]`) : boucle infinie (`RecursionError`).
- **Oublier un cas limite sur une liste** : par exemple tester `len(lst) == 0` au lieu de `len(lst) <= 1` dans `est_triee`, ce qui provoquerait `IndexError: list index out of range` sur `lst[1]` pour une liste à un élément.
- **Inclure `milieu` dans le nouvel intervalle** (`milieu` au lieu de `milieu + 1` ou `milieu - 1`) dans `recherche_dicho_rec` : lorsque `gauche == droite` et que `x` n'est pas présent, l'intervalle ne diminuerait plus et bouclerait indéfiniment.

<!-- ===================== CORRIGÉ : FIN ===================== -->
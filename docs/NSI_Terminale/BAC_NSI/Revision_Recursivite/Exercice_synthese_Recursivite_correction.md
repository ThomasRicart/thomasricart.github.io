

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
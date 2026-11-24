# 🐍 PR02 : Récursivité


---

## 📂 Ressources du Chapitre

Accédez ici à l'ensemble des documents de cours et aux outils de révision interactive.

| Support | Description | Corrections |
| :--- | :--- | :--- |
| [📕 **Cours**](./TNSI_LP02-Recursivite.pdf) | Le support de cours complet en version PDF. | |
| [📚 **Activité Capytale 1**](https://capytale2.ac-paris.fr/web/c/c5eb-12669358/meo) | **c5eb-12669358** | [Correction]()|

[🚀 Ouvrir et exécuter le TP 1 en local](https://notebook.basthon.fr/?from=https://thomasricart.github.io/NSI_Terminale/26-PR_Programmation/PR02_Recursivite/TNSI-LP02-TP-Recursivite.ipynb){ .md-button .md-button--primary }



Algorithmes à connaitre:

1. Implémenter une suite récurrente. Par exemple, la suite $(u_n)$ définie par $u_0 = 1$ et $u_{n+1} = 3 u_n - 1$.

```python
def suite_recurrente(n):
    if n == 0:
        return 1
    else:
        return 3 * suite_recurrente(n - 1) - 1
```

2. Implémenter la puissance d'un nombre. Par exemple, $a^n$ avec $a$ un nombre réel et $n$ un entier naturel.

```python
def puissance(a, n):
    if n == 0:
        return 1
    else:
        return a * puissance(a, n - 1)
```

3. Implémenter la factorielle d'un nombre. Par exemple, $n!$ avec $n$ un entier naturel.

```python   
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)
```

4. Implémenter la suite de Fibonacci. Par exemple, la suite $(F_n)$ définie par $F_0 = 0$, $F_1 = 1$ et $F_{n} = F_{n-1} + F_{n-2}$.

```python
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

5. Implémenter le calcul des coefficients binomiaux. Par exemple, le coefficient binomial $\binom{n}{k}$ avec $n$ et $k$ des entiers naturels.

```python
def coefficient_binomial(n, k):
    if k == 0 or k == n:
        return 1
    if k > n:
        return 0
    else:
        return coefficient_binomial(n - 1, k - 1) + coefficient_binomial(n - 1, k)
```

6. Implémenter la fonction de somme des éléments d'une liste. Par exemple, la somme des éléments d'une liste $L$.

```python

def somme_liste(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + somme_liste(L[1:])
``` 

7. Implémenter la fonction qui retourne le maximum d'une liste. Par exemple, le maximum des éléments d'une liste $L$.

```python
def maximum_liste(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0], maximum_liste(L[1:]))
```

8. Fonction quotient(a, b) qui retourne le quotient de la division entière de a par b. 

```python
def quotient(a, b):
    if a < b:
        return 0
    else:
        return 1 + quotient(a - b, b)
```

9. Fonction reste(a, b) qui retourne le reste de la division entière de a par b.

```python
def reste(a, b):
    if a < b:
        return a
    else:
        return reste(a - b, b)
```

10. Implémenter la fonction qui teste si une chaine de caractères est un palindrome. Par exemple, tester si une chaine $s$ est un palindrome.

```python

def est_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and est_palindrome(s[1:-1])
```

11. Exponentiation rapide. Par exemple, calculer $a^n$ avec $a$ un nombre réel et $n$ un entier naturel.

```python

def exponentiation_rapide(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return exponentiation_rapide(a, n // 2) ** 2
    else:
        return a * exponentiation_rapide(a, n //2) ** 2
``` 

12. Ecrire la fonction recherche(L, val) qui retourne True si val est dans la liste L et False sinon.

```python
def recherche(L, val):
    if len(L) == 0:
        return False
    else:
        return L[0] == val or recherche(L[1:], val)
```

13. Ecrire la fonction `hanoi(n, depart, arrivee, intermediaire)` qui affiche les déplacements nécessaires pour résoudre le problème des tours de Hanoï avec `n` disques. Le disque le plus grand est au départ et doit être déplacé vers l'arrivée en utilisant l'intermédiaire comme tour temporaire.

```python
def hanoi(n, depart, arrivee, intermediaire):
    if n == 0:
        return
    else:
        hanoi(n - 1, depart, intermediaire, arrivee)
        print(f"Déplacer le disque de {depart} vers {arrivee}")
        hanoi(n - 1, intermediaire, arrivee, depart)
```

---
---

### 🧩 Concepts illustrés
```python
```
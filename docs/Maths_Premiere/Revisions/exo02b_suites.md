# Exercice : Étude de l'évolution d'une population (Modélisation et Sommes)

**Niveau :** Première Spécialité Mathématiques  
**Thème :** Suite homographique, suite arithmético-géométrique et calcul de sommes.

---

## Partie A : Étude d'une suite explicite
Soit $(u_n)$ la suite définie pour tout entier naturel $n \geq 0$ par :  
$$u_n = \frac{4n + 2}{n + 5}$$

1. Calculer les termes $u_0$, $u_1$ et $u_2$ sous forme de fractions simplifiées.

2. Étudier le sens de variation de la suite $(u_n)$ sur $\mathbb{N}$.

3. Déterminer, par le calcul, le plus petit entier $n$ tel que $u_n > 3,8$.

4. Compléter l'algorithme suivant pour qu'il retourne le premier rang $n$ à partir duquel la suite dépasse une valeur $seuil$ donnée (avec $seuil < 4$).

```python
def trouve_rang(seuil):
    n = 0
    u = 0.4  # Valeur de u_0
    
    while u <= .........:
        n = .........
        u = .........
        
    return n

# Test de la fonction pour un seuil de 3.99
print("Le rang n est :", trouve_rang(3.99))


```

## Partie B : Modélisation d'une réserve naturelle
Une réserve naturelle compte $3\,000$ oiseaux au 1er janvier 2025. On estime que chaque année, la population diminue de $2\%$, mais que $150$ oiseaux arrivent dans la réserve en raison de la migration.  
On note $v_n$ le nombre d'oiseaux au 1er janvier de l'année $2025 + n$. On a donc $v_0 = 3\,000$.

1. Calculer $v_1$ et $v_2$.

2. Justifier que pour tout $n \in \mathbb{N}$ : $v_{n+1} = 0,98 \times v_n + 150     $.

3. On considère la suite auxiliaire $(w_n)$ définie pour tout $n$ par $w_n = v_n - 7\,500$.

    * **a.** Démontrer que $(w_n)$ est une suite géométrique dont on précisera la raison et son premier terme $w_0$.

    * **b.** Exprimer $w_n$ en fonction de $n$.

    * **c.** En déduire que pour tout $n \in \mathbb{N}$ : $v_n = 0,98^{n} \times 7\,500 + 7\,500$.

---

## Partie C : Cumul et Statistiques

L'administration de la réserve souhaite calculer le "nombre total de nuitées" (la somme des populations annuelles observées) sur les 11 premières années (de 2025 à 2035 inclus, soit de $n=0$ à $n=10$).  
On note $S = v_0 + v_1 + \dots + v_{10}$.

1. Montrer que $S = 11 \times 7\,500 + (w_0 + w_1 + \dots + w_{10})$.

2. À l'aide de la formule de la somme des termes d'une suite géométrique, calculer la valeur exacte de $S$.

3. En déduire une valeur arrondie à l'unité près.

4. Compléter l'algorithme suivant pour qu'il retourne la somme $S$ des populations annuelles sur les 11 premières années.

```python
def somme_population():
    v = ....  # Population initiale
    S = .... # Initialisation de la somme
    
    for n in range(11):
        S = ............
        v = ............  # Calcul de la population pour l'année suivante
        
    return S
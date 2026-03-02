# Exercice 2 : Étude de suites numériques (Modélisation et Sommes)

**Niveau :** Première Spécialité Mathématiques  
**Thème :** Suites explicites, récurrence arithmético-géométrique et calcul de sommes.

---

## Énoncé

### Partie A : Étude d'une suite explicite
Soit $(u_n)$ la suite définie pour tout entier naturel $n \geq 0$ par :  
\\[u_n = \frac{3n - 1}{n + 2}\\]

1. Calculer les termes $u_0$, $u_1$ et $u_2$.
2. Étudier les variations de la suite $(u_n)$ sur $\mathbb{N}$.
3. Déterminer, par le calcul, le plus petit entier $n$ tel que $u_n > 2,5$.
4. Compléter l'algorithme de recherche de seuil qui calcule le plus petit entier $n$ tel que $u_n>cible$, $cible$ étant un réel strictement inférieur à 3. 

```
def cherche_seuil(cible):
    n = 0
    u = -0.5  # Valeur de u_0
    
    while u .........:
        n = .........
        u = .........
        
    return n

# Appel de la fonction pour la valeur demandée
resultat = cherche_seuil(2.99999)
print("Le plus petit entier n est :", resultat)
```

### Partie B : Modélisation et Suite Arithmético-géométrique
Un investisseur place $1\,000$ € le 1er janvier 2024 sur un compte d'épargne. Chaque année, ce capital augmente de $5\%$ grâce aux intérêts, mais l'investisseur retire $40$ € de frais de gestion à la fin de l'année.  
On note $v_n$ le capital au 1er janvier de l'année $2024 + n$. On a $v_0 = 1\,000$.

1. Calculer $v_1$ et $v_2$.
2. Justifier que pour tout $n \in \mathbb{N}$ : $v_{n+1} = 1,05v_n - 40$.
3. On considère la suite auxiliaire $(w_n)$ définie par $w_n = v_n - 800$.
   a. Démontrer que $(w_n)$ est une suite géométrique de raison $q = 1,05$. Préciser son premier terme $w_0$.
   b. Exprimer $w_n$ en fonction de $n$.
   c. En déduire que pour tout $n \in \mathbb{N}$ : $v_n = 200 \times 1,05^n + 800$.

### Partie C : Calcul de somme et cumul
On souhaite calculer la somme totale des capitaux présents sur le compte entre l'année 2024 et l'année 2033 incluse (soit de $n=0$ à $n=9$).  
On note $S = v_0 + v_1 + v_2 + \dots + v_9$.

1. Exprimer $S$ en fonction de la somme des termes de la suite $(w_n)$.
2. En déduire la valeur exacte de $S$, puis une valeur arrondie à l'euro près.
# Correction : Étude de l'évolution d'une population (Modélisation et Sommes)

## Partie A : Étude d'une suite explicite

### 1. Calcul des termes

* $u_0 = \frac{4(0) + 2}{0 + 5} = \frac{2}{5} = 0,4$

* $u_1 = \frac{4(1) + 2}{1 + 5} = \frac{6}{6} = 1$

* $u_2 = \frac{4(2) + 2}{2 + 5} = \frac{10}{7} \approx 1,43$

### 2. Variations
Soit $f$ la fonction définie sur $[0 ; +\infty[$ par $f(x) = \frac{4x + 2}{x + 5}$.  

$f$ est de la forme $\frac{u}{v}$ avec $u(x) = 4x + 2$ et $v(x) = x + 5$.  

$f'(x) = \frac{4(x + 5) - 1(4x + 2)}{(x + 5)^2} = \frac{4x + 20 - 4x - 2}{(x + 5)^2} = \frac{18}{(x + 5)^2}$.

Comme $f'(x) > 0$ sur $[0 ; +\infty[$, la fonction $f$ est strictement croissante. On en déduit que la suite $(u_n)$ est **croissante**.

### 3. Recherche de seuil par le calcul

$u_n > 3,8 \iff \frac{4n + 2}{n + 5} > 3,8$  

$4n + 2 > 3,8(n + 5)$  

$4n + 2 > 3,8n + 19$  

$0,2n > 17 \iff n > \frac{17}{0,2} \iff n > 85$.  

Le plus petit entier est **$n = 86$**.

### 4. Algorithme complété
```python
def trouve_rang(seuil):
    n = 0
    u = 0.4  # Valeur de u_0
    
    while u <= seuil:
        n = n + 1
        u = (4 * n + 2) / (n + 5)
        
    return n

```

## Partie B : Modélisation d'une réserve naturelle

### 1. Premiers termes

* $v_1 = 3\,000 \times 1,02 - 150 = 2\,910$ 

* $v_2 = 2\,910 \times 1,02 - 150 = 2\,818,2$

### 2. Relation de récurrence

Une augmentation de $2\%$ correspond à un coefficient multiplicateur de $1 + \frac{2}{100} = 1,02$. En retranchant les $150$ oiseaux qui quittent la réserve, on obtient bien : **$v_{n+1} = 1,02v_n - 150$**.

### 3. Suite auxiliaire $(w_n)$

a. $w_{n+1} = v_{n+1} - 7\,500 = (1,02v_n - 150) - 7\,500 = 1,02v_n - 7\,650$.  

En factorisant par $1,02$ : $w_{n+1} = 1,02(v_n - \frac{7\,650}{1,02}) = 1,02(v_n - 7\,500) = 1,02w_n$.  

La suite $(w_n)$ est donc **géométrique de raison $q = 1,02$**.  

Premier terme : $w_0 = v_0 - 7\,500 = 3\,000 - 7\,500 = -4\,500$.

b. Expression fonctionnelle : **$w_n = -4\,500 \times 1,02^n$**.

c. Comme $w_n = v_n - 7\,500$, alors $v_n = w_n + 7\,500$.  
D'où : **$v_n = 7\,500 - 4\,500 \times 1,02^n$**.

---

## Partie C : Calcul de somme

### 1. Expression de $S$

$S = \sum_{k=0}^{10} v_k = \sum_{k=0}^{10} (w_k + 7\,500) = \left( \sum_{k=0}^{10} w_k \right) + 11 \times 7\,500$

### 2. Calcul final

Somme des termes de $(w_n)$ :  
$\sum_{k=0}^{10} w_k = -4\,500 \times \frac{1 - 1,02^{11}}{1 - 1,02} = -4\,500 \times \frac{1 - 1,02^{11}}{-0,02} = 225\,000 \times (1 - 1,02^{11})$

Calcul de $S$ :  

$S = 225\,000 \times (1 - 1,02^{11}) + 82\,500$ 

$S \approx 225\,000 \times (1 - 1,24337) + 82\,500$  

$S \approx -54\,758,25 + 82\,500$  

**$S \approx 27\,742$ oiseaux**.
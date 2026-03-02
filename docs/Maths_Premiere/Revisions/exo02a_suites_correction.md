# Exercice 2: Correction : Étude de suites numériques

## Partie A : Suite explicite

### 1. Calcul des termes

* $u_0 = \frac{3(0) - 1}{0 + 2} = -0,5$
* $u_1 = \frac{3(1) - 1}{1 + 2} = \frac{2}{3} \approx 0,67$
* $u_2 = \frac{3(2) - 1}{2 + 2} = \frac{5}{4} = 1,25$

### 2. Variations
Soit $f$ la fonction définie sur $[0 ; +\infty[$ par $f(x) = \frac{3x-1}{x+2}$.  
$f$ est de la forme $\frac{u}{v}$ avec $u(x)=3x-1$ et $v(x)=x+2$.  
$f'(x) = \frac{3(x+2) - 1(3x-1)}{(x+2)^2} = \frac{3x+6-3x+1}{(x+2)^2} = \frac{7}{(x+2)^2}$.

Comme $f'(x) > 0$ sur $[0 ; +\infty[$, la fonction $f$ est croissante. On en déduit que la suite $(u_n)$ est **croissante**.

\\[
\begin{array}{c|ccc}
x & 0 & & +\infty \\\\
\hline
f'(x) & & + & \\\\
\hline
 & & & 3 \\\\
f(x) & & \nearrow & \\\\
 & -0,5 & & 
\end{array}
\\]

### 3. Recherche de seuil

$u_n > 2,5 \iff \frac{3n-1}{n+2} > 2,5$  

$3n - 1 > 2,5(n + 2)$  

$3n - 1 > 2,5n + 5$ 

$0,5n > 6 \iff n > 12$.  

Le plus petit entier est **$n = 13$**.


### 4. Recherche de seuil avec un algorithme

```
def cherche_seuil(cible):
    n = 0
    u = -0.5  # Valeur de u_0
    
    while u <= cible:
        n = n + 1
        u = (3 * n - 1) / (n + 2)
        
    return n

# Appel de la fonction pour la valeur demandée
resultat = cherche_seuil(2.99999)
print("Le plus petit entier n est :", resultat)
```
---

## Partie B : Suite Arithmético-géométrique

### 1. Premiers termes

* $v_1 = 1\,000 \times 1,05 - 40 = 1\,010$ €
* $v_2 = 1\,010 \times 1,05 - 40 = 1\,020,50$ €

### 2. Relation de récurrence
Une augmentation de $5\%$ correspond à un coefficient multiplicateur de $1 + \frac{5}{100} = 1,05$. En retirant les 40 € de frais, on a bien : **$v_{n+1} = 1,05v_n - 40$**.

### 3. Suite auxiliaire $(w_n)$

a. $w_{n+1} = v_{n+1} - 800 = (1,05v_n - 40) - 800 = 1,05v_n - 840$.  
En factorisant par 1,05 : $w_{n+1} = 1,05(v_n - \frac{840}{1,05}) = 1,05(v_n - 800) = 1,05w_n$.  
La suite $(w_n)$ est donc **géométrique de raison $q = 1,05$**.  
Premier terme : $w_0 = v_0 - 800 = 1\,000 - 800 = 200$.

b. Expression fonctionnelle : **$w_n = 200 \times 1,05^n$**.

c. Comme $w_n = v_n - 800$, alors $v_n = w_n + 800$.  
D'où : **$v_n = 200 \times 1,05^n + 800$**.

---

## Partie C : Calcul de somme

### 1. Expression de $S$
$S = \sum_{k=0}^{9} v_k = \sum_{k=0}^{9} (w_k + 800) = \left( \sum_{k=0}^{9} w_k \right) + 10 \times 800$

### 2. Calcul final
Somme des termes de $(w_n)$ :  
$\sum_{k=0}^{9} w_k = 200 \times \frac{1 - 1,05^{10}}{1 - 1,05} = 200 \times \frac{1 - 1,05^{10}}{-0,05} = 4\,000 \times (1,05^{10} - 1)$

Calcul de $S$ :  
$S = 4\,000 \times (1,05^{10} - 1) + 8\,000$  
$S \approx 4\,000 \times (1,62889 - 1) + 8\,000 \approx 2\,515,56 + 8\,000$  
**$S \approx 10\,516$ €**.
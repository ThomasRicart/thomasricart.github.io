# CCF Blanc 02 Mathématiques – BTS CIEL 1ère année
## Session CIEL 1ère année 2026

**Durée : 55 minutes** **Documents autorisés : Calculatrice graphique, logiciel GeoGebra**

---

## Contexte général
En télécommunications, le gain d'un amplificateur peut varier selon la tension de commande. On modélise le gain $G$ (en décibels) en fonction de la tension $x$ (en volts) sur l'intervalle $[1 ; 10]$ par :
$f(x) = A \ln(x) + Bx$

---

## Partie 1 – Configuration des paramètres 

Avant d'étudier le signal, le technicien doit configurer l'amplificateur pour qu'il réponde à deux contraintes techniques :

1. Pour une tension nulle de référence ($x = 1\text{ V}$), le gain doit être exactement de $5\text{ dB}$.

2. Pour stabiliser le signal, le gain doit atteindre son minimum pour une tension de $4\text{ V}$.

### 1.1 – Question préliminaire

1. Justifier que cette fonction est bien définie sur $]0; +\infty[$.

2. Si $A<0$ et $B>0$, justifier que $\displaystyle\lim_{t \to 0} f(x)=+\infty$


### 1.2 – Détermination assistée par ordinateur

> **✋ Appel professeur n°1** : 
> 1. Sur GeoGebra, créer deux curseurs pour les paramètres $A$ (allant de $-50$ à $0$) et $B$ (allant de $0$ à $20$).
>
> 2. Saisir la fo
nction $f(x) = A \ln(x) + Bx$.
>
> 3. En manipulant les curseurs, trouver les valeurs entières de $A$ et $B$ permettant de vérifier les deux contraintes citées plus haut.
>
> 4. Noter ces valeurs sur votre copie et montrer au professeur que votre courbe passe par le point $(1 ; 5)$ et possède un minimum en $x = 4$.

---

## Partie 2 – Étude de la fonction de Gain
Pour la suite, on admet que les paramètres sont fixés à **$A = -20$** et **$B = 5$**. La fonction est donc :
$f(x) = -20 \ln(x) + 5x$

### 2.1 – Valeurs limites

a) Calculer la valeur exacte de $f(1)$.

Vérifier la cohérence avec la Partie 1. 

b) Calculer une valeur approchée à $10^{-2}$ de $f(10)$.

### 2.2 – Étude de la dérivée et des variations

a) Calculer la dérivée $f'(x)$ sur l'intervalle $[1 ; 10]$.  

b) Montrer que $f'(x) = \dfrac{5x - 20}{x}$. 

c) Étudier le signe de $f'(x)$ sur $[1 ; 10]$ et dresser le tableau de variations complet de $f$.

---

## Partie 3 – Calcul de la Puissance Moyenne

### 3.1 – Recherche de primitive

On rappelle qu'une primitive de $\ln(x)$ est $x \ln(x) - x$.  

a) Déterminer une primitive $F$ de la fonction $f$ sur $[1 ; 10]$.  

b) Calculer la valeur exacte de l'intégrale $I = \displaystyle\int_{1}^{5} f(x) \, dx$.

### 3.2 – Valeur moyenne

Calculer la valeur moyenne $G_m$ du gain sur l'intervalle $[1 ; 5]$ (arrondir au dixième) :
$G_m = \frac{1}{5-1} \int_{1}^{5} f(x) \, dx$

---



## Partie 4 – Contrôle qualité et Probabilités conditionnelles

L'entreprise s'approvisionne en puces d'amplification auprès de deux fournisseurs, **S1** et **S2**.

* Le fournisseur **S1** livre **60 %** du stock.

* Le fournisseur **S2** livre le reste du stock.

* On constate que **3 %** des puces de **S1** sont défectueuses ($D$).

* On constate que **2 %** des puces de **S2** sont défectueuses ($D$).

### 4.1 – Modélisation
Construire un arbre pondéré décrivant la situation.



### 4.2 – Probabilités totales
Calculer la probabilité totale $P(D)$ qu'une puce prélevée au hasard soit défectueuse.

### 4.3 – Probabilité "a posteriori"
Une puce prélevée est défectueuse. Calculer la probabilité qu'elle provienne du fournisseur **S1**. Arrondir à $10^{-3}$.


## Partie 5 – Fiabilité et Seuil de Confiance ✋ *Appel professeur n°2*

On utilise des composants dont la probabilité de défaut est $p = 0,04$. On prélève un lot de $n$ résistances.

### 5.1 – Probabilités
Pour un lot de $n = 80$, on admet que le nombre de défauts suit une loi binomiale.

a) Justifier les paramètres de cette loi.

b) Calculer la probabilité d'avoir au moins une résistance défectueuse $P(X \geq 1)$.

### 5.2 – Recherche de seuil
Le responsable veut que la probabilité d'avoir au moins un défaut dépasse **0,99**.

Trouver le nombre minimal de composants à tester pour que au moins un ait un défaut soit supérieur à 0.99

> **✋ Appel professeur n°2**  Expliquer votre démarche au professeur.
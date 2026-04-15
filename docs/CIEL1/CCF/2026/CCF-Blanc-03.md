# CCF Blanc 03 Mathématiques – BTS CIEL 1ère année
## Session CIEL 1ère année 2026

**Durée : 55 minutes** **Documents autorisés : Calculatrice graphique, logiciel GeoGebra**

---

## Contexte général
Dans un laboratoire d'électronique, on étudie la réponse d'un circuit RLC soumis à une impulsion. La tension $u(x)$ (en volts) aux bornes d'un condensateur en fonction du temps $x$ (en millisecondes) est modélisée par :
$f(x) = (ax + 2)e^{-kx}$
où $a$ et $k$ sont des paramètres dépendant des composants choisis.

---

## Partie 1 – Recherche de paramètres ✋ *Appel professeur n°1*

Le technicien souhaite que le signal respecte deux critères de performance :
1. La tension doit être maximale à l'instant $x = 2\text{ ms}$.
2. À cet instant précis, la tension doit être d'environ $2,7\text{ V}$.

### 1.1 – Question préliminaire
Justifier que pour toute valeur de $k > 0$, $\displaystyle\lim_{x \to +\infty} f(x) = 0$. Interpréter ce résultat dans le contexte du circuit électrique.

### 1.2 – Détermination assistée par ordinateur
> **✋ Appel professeur n°1** : 
>
> 1. Sur GeoGebra, créer deux curseurs : $a$ (de $0$ à $10$) et $k$ (de $0$ à $2$).
>
> 2. Saisir la fonction $f(x) = (ax + 2)e^{-kx}$.
>
> 3. En manipulant les curseurs, trouver les valeurs de $a$ et $k$ permettant de placer le maximum de la courbe au point de coordonnées $(2 ; 2,7)$.
>
> 4. Noter ces valeurs sur votre copie (arrondir $a$ à l'entier et $k$ au dixième).

---

## Partie 2 – Étude de la fonction de Tension
Pour la suite, on fixe **$a = 4$** et **$k = 0,5$**. On étudie donc sur $[0 ; +\infty[$ :
$f(x) = (4x + 2)e^{-0,5x}$

### 2.1 – Analyse dérivée

a) Montrer que la dérivée de $f$ est $f'(x) = (3 - 2x)e^{-0,5x}$.  

b) Étudier le signe de $f'(x)$ sur $[0 ; 20]$.  
c) Dresser le tableau de variations complet de $f$ sur cet intervalle.

### 2.2 – Application

Déterminer par le calcul l'instant précis $x$ où la tension est maximale et calculer la valeur exacte de ce maximum.

---

## Partie 3 – Valeur moyenne et Énergie

### 3.1 – Vérification de primitive
On considère la fonction $F$ définie par $F(x) = (-8x - 20)e^{-0,5x}$.  

Montrer que $F$ est une primitive de $f$ sur $[0 ; +\infty[$.

### 3.2 – Tension moyenne

Calculer la valeur moyenne $U_m$ de la tension entre les instants $x=0$ et $x=10$ :
$U_m = \dfrac{1}{10-0} \displaystyle\int_{0}^{10} f(x) \, dx$
(Arrondir au centième).

---

## Partie 4 – Fiabilité du système ✋ *Appel professeur n°2*

Le circuit utilise des micro-contrôleurs dont **5 %** présentent un défaut de synchronisation. On teste un lot de **$n$** circuits.

### 4.1 – Probabilités conditionnelles (Arbre)
Le test de diagnostic n'est pas parfait :

* Si le circuit est défectueux, le test est positif dans **98 %** des cas.

* Si le circuit est sain, le test est négatif dans **95 %** des cas.

> **Question :** Construire l'arbre pondéré et calculer la probabilité qu'un circuit soit sain sachant que son test est positif.

### 4.2 – Loi Binomiale et Seuil
On prélève $n$ circuits (loi binomiale de paramètres $n$ et $p=0,05$).
On veut que la probabilité d'avoir au moins un circuit défectueux soit supérieure à **0,99**.

> **✋ Appel professeur n°2** : Résoudre l'inéquation $1 - (0,95)^n > 0,99$ à l'aide du logarithme népérien pour déterminer la taille minimale du lot $n$.
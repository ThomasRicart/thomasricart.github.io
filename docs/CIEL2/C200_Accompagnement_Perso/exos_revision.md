<entry path="exercices_revision_bts_ciel.md" title="Série d'Exercices de Révision - BTS CIEL 1">
# Exercices d'Entraînement - Révision Mathématiques BTS CIEL 1

Cette série d'exercices couvre l'ensemble des modules du programme de révision. Pour chaque notion, trois exercices progressifs accompagnés de leurs corrections détaillées sont proposés.

---

## Module 1 : Probabilités et Événements

### Exercice 1.1 : Calculs de probabilités conditionnelles et arbre
Dans un parc informatique d'une entreprise, 60% des ordinateurs sont des postes fixes et 40% sont des portables. 
- 5% des ordinateurs fixes présentent une défaillance matérielle au cours de l'année.
- 10% des ordinateurs portables présentent une défaillance matérielle au cours de l'année.

On choisit un ordinateur au hasard dans le parc. On note :
- $F$ : « L'ordinateur est un poste fixe »
- $D$ : « L'ordinateur présente une défaillance »

1. Représenter la situation par un arbre pondéré.
2. Calculer la probabilité que l'ordinateur soit fixe et présente une défaillance.
3. Calculer la probabilité globale $P(D)$ qu'un ordinateur choisi au hasard présente une défaillance.
4. Sachant que l'ordinateur choisi présente une défaillance, quelle est la probabilité qu'il s'agisse d'un ordinateur portable ?

---

### Exercice 1.2 : Loi binomiale et contrôle qualité
Une ligne de production de puces électroniques produit des pièces dont 2% présentent un défaut. On prélève au hasard et avec remise un lot de 50 puces. On note $X$ le nombre de puces défectueuses dans ce lot.

1. Justifier que $X$ suit une loi binomiale et préciser ses paramètres.
2. Calculer la probabilité d'obtenir exactement 2 puces défectueuses dans le lot.
3. Calculer la probabilité d'avoir au moins une puce défectueuse.
4. Déterminer l'espérance $E(X)$ et l'écart-type $\sigma(X)$. Que représente $E(X)$ ?

---

## Module 2 : Analyse, Dérivation et Étude de Fonctions

### Exercice 2.1 : Calculs de dérivées fondamentales et composées
Calculer la fonction dérivée $f'(x)$ pour chacune des fonctions suivantes définies sur l'intervalle donné :

1. $f_1(x) = 3x^4 - 5x^2 + \dfrac{2}{x} - 7 \quad \text{sur } ]0\,;\, +\infty[$
2. $f_2(x) = (2x^2 + 3) \cdot (4-x^3) \quad \text{sur } \mathbb{R}$
3. $f_3(x) = \dfrac{4x - 1}{x^2 + 3} \quad \text{sur } \mathbb{R}$

---

### Exercice 2.2 : Étude de fonction polynôme et équation de tangente
Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = x^3 - 3x + 2$.

1. Calculer la dérivée $f'(x)$ et étudier son signe.
2. Dresser le tableau de variations complet de $f$ sur $\mathbb{R}$.
3. Déterminer l'équation de la tangente $\mathcal{T}$ à la courbe représentative de $f$ au point d'abscisse $a = 2$.

---

## Module 3 : Fonctions Exponentielles et Logarithmes

### Exercice 3.1 : Équations et inéquations avec $\exp$ et $\ln$
Résoudre dans $\mathbb{R}$ les équations et inéquations suivantes :

1. $e^{3x - 1} = 5$
2. $\ln(2x + 4) = 3$
3. $e^{2x} - 4e^x + 3 = 0$ (Indication : poser $X = e^x$)


---

### Exercice 3.2 : Étude de fonction logarithme
Soit $f$ la fonction définie sur $]0\,;\, +\infty[$ par $f(x) = x - 2 - \ln(x)$.

1. Calculer la dérivée $f'(x)$ et déterminer son signe sur $]0\,;\, +\infty[$.
2. Déterminer les variations de $f$.
3. Déduire que pour tout $x > 0$, $f(x) \ge -1$.

---

### Exercice 3.3 : Charge d'un condensateur (Application physique)
Lors de la charge d'un condensateur de capacité $C$ à travers une résistance $R$, la tension aux bornes du condensateur est modélisée par :
$$u(t) = U_0 \left(1 - e^{-\frac{t}{\tau}}\right) \quad \text{pour } t \ge 0$$
où $U_0 = 10\text{ V}$ est la tension d'alimentation et $\tau = R \cdot C = 2\text{ ms}$ est la constante de temps du circuit.

1. Calculer la tension aux bornes du condensateur à l'instant $t = 2\text{ ms}$ (à $t = \tau$).
2. Déterminer la valeur limite de $u(t)$ quand $t$ tend vers $+\infty$.
3. Déterminer l'instant $t_1$ auquel la tension atteint $95\%$ de sa valeur maximale $U_0$.


---

## Module 4 : Suites Numériques

### Exercice 4.1 : Suite arithmétique et modélisation
Un technicien réseau intervient sur des incidents. Le premier mois, il traite $u_1 = 120$ tickets. Chaque mois suivant, grâce à l'automatisation, le nombre de tickets à traiter diminue de $8$ tickets. On note $u_n$ le nombre de tickets traités le $n$-ième mois.

1. Donner la nature de la suite $(u_n)$ et préciser son premier terme $u_1$ et sa raison $r$.
2. Exprimer $u_n$ en fonction de $n$.
3. Combien de tickets le technicien traitera-t-il le 12-ième mois ?
4. Calculer le nombre total de tickets traités au cours de la première année (de $n=1$ à $n=12$).

---

### Exercice 4.2 : Suite géométrique et amortissement
La valeur d'un serveur informatique s'élève à $u_0 = 4\,000$ € à l'achat. Chaque année, le serveur perd $15\%$ de sa valeur par rapport à l'année précédente. On note $u_n$ la valeur du serveur après $n$ années.

1. Montrer que la suite $(u_n)$ est géométrique et préciser sa raison $q$.
2. Exprimer $u_n$ en fonction de $n$.
3. Calculer la valeur estimée du serveur au bout de 5 ans (arrondir au centime).
4. Déterminer au bout de combien d'années la valeur du serveur deviendra inférieure à $1\,000$ €.


---

### Exercice 4.3 : Suite arithmetico-géométrique
Soit la suite $(u_n)$ définie par $u_0 = 2$ et pour tout $n \in \mathbb{N}$, $u_{n+1} = 0{,}5 u_n + 3$.
On pose, pour tout $n \in \mathbb{N}$, $v_n = u_n - 6$.

1. Montrer que $(v_n)$ est une suite géométrique de raison $q = 0{,}5$ et préciser son terme initial $v_0$.
2. En déduire l'expression de $v_n$ puis de $u_n$ en fonction de $n$.
3. Déterminer la limite de la suite $(u_n)$ quand $n \to +\infty$.


---

## Module 5 : Trigonométrie

### Exercice 5.1 : Équations trigonométriques fondamentales
Résoudre dans l'intervalle $]-\pi\,;\, \pi]$ les équations trigonométriques suivantes :

1. $\cos(x) = \frac{\sqrt{3}}{2}$
2. $\sin(2x) = -\frac{1}{2}$


---

### Exercice 5.3 : Signal sinusoïdal temporel (Application physique)
La tension $u(t)$ d'un signal alternatif est donnée par :
$$u(t) = 311 \cdot \sin(100\pi t + \frac{\pi}{4}) \quad \text{où } t \text{ est en secondes et } u(t) \text{ en Volts.}$$

1. Déterminer l'amplitude maximale $U_{max}$, la fréquence $f$ (en Hz) et la phase à l'origine $\varphi$.
2. Calculer la valeur efficace $U_{eff} = \frac{U_{max}}{\sqrt{2}}$.
3. Calculer la valeur instantanée $u(0)$ à l'instant $t = 0\text{ s}$.

---

## Module 6 : Nombres Complexes

### Exercice 6.1 : Forme algébrique et opérations
Soient les deux nombres complexes $z_1 = 3 + 4i$ et $z_2 = 1 - 2i$.

1. Calculer $z_1 + z_2$ et $z_1 - 2z_2$.
2. Calculer le produit $z_1 \cdot z_2$ sous forme algébrique.
3. Calculer le quotient $\frac{z_1}{z_2}$ sous forme algébrique.

---

### Exercice 6.2 : Passage forme algébrique $\leftrightarrow$ forme trigonométrique / exponentielle
1. Soit $z_A = -2 + 2i\sqrt{3}$.
   - Calculer le module $|z_A|$.
   - Déterminer un argument $\arg(z_A)$.
   - En déduire la forme trigonométrique et la forme exponentielle de $z_A$.
2. Soit $z_B = 4 e^{i\frac{2\pi}{3}}$. Donner la forme algébrique de $z_B$.


---

### Exercice 6.3 : Application en Électricité (Calcul d'impédance complexe)
Dans un circuit $RLC$ série alimenté par un courant alternatif de fréquence $f$, l'impédance complexe totale est donnée par :
$$\underline{Z} = R + j\left(L\omega - \frac{1}{C\omega}\right) \quad (\text{avec } j^2 = -1)$$
On donne : $R = 30\ \Omega$, $L\omega = 80\ \Omega$, et $\frac{1}{C\omega} = 40\ \Omega$.

1. Déterminer l'expression algébrique de l'impédance complexe $\underline{Z}$.
2. Calculer le module $|\underline{Z}|$ (représentant l'impédance réelle du circuit en Ohms).
3. Calculer le déphasage $\varphi = \arg(\underline{Z})$ du courant par rapport à la tension.

</entry>
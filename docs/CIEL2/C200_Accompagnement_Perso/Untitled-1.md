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

#### Correction 1.1
1. **Arbre pondéré :**
   - $P(F) = 0{,}60$, donc $P(\overline{F}) = 0{,}40$.
   - $P_F(D) = 0{,}05$, donc $P_F(\overline{D}) = 0{,}95$.
   - $P_{\overline{F}}(D) = 0{,}10$, donc $P_{\overline{F}}(\overline{D}) = 0{,}90$.

2. **Probabilité de $F \cap D$ :**
   $$P(F \cap D) = P(F) \times P_F(D) = 0{,}60 \times 0{,}05 = 0{,}03$$

3. **Probabilité totale $P(D)$ :**
   D'après la formule des probabilités totales :
   $$P(D) = P(F \cap D) + P(\overline{F} \cap D) = P(F) \times P_F(D) + P(\overline{F}) \times P_{\overline{F}}(D)$$
   $$P(D) = 0{,}03 + (0{,}40 \times 0{,}10) = 0{,}03 + 0{,}04 = 0{,}07$$

4. **Probabilité conditionnelle $P_D(\overline{F})$ :**
   $$P_D(\overline{F}) = \frac{P(\overline{F} \cap D)}{P(D)} = \frac{0{,}04}{0{,}07} = \frac{4}{7} \approx 0{,}5714\text{ (soit } 57{,}14\%)$$

---

### Exercice 1.2 : Loi binomiale et contrôle qualité
Une ligne de production de puces électroniques produit des pièces dont 2% présentent un défaut. On prélève au hasard et avec remise un lot de 50 puces. On note $X$ le nombre de puces défectueuses dans ce lot.

1. Justifier que $X$ suit une loi binomiale et préciser ses paramètres.
2. Calculer la probabilité d'obtenir exactement 2 puces défectueuses dans le lot.
3. Calculer la probabilité d'avoir au moins une puce défectueuse.
4. Déterminer l'espérance $E(X)$ et l'écart-type $\sigma(X)$. Que représente $E(X)$ ?

#### Correction 1.2
1. **Justification :**
   On répète $n = 50$ fois de manière indépendante et identique une épreuve de Bernoulli à deux issues (« la puce est défectueuse » de probabilité $p = 0{,}02$, et « la puce est conforme » de probabilité $1-p = 0{,}98$). 
   Ainsi, $X$ suit la loi binomiale $\mathcal{B}(50\,;\, 0{,}02)$.

2. **Calcul de $P(X = 2)$ :**
   $$P(X = 2) = \binom{50}{2} \times (0{,}02)^2 \times (0{,}98)^{48}$$
   $$\binom{50}{2} = \frac{50 \times 49}{2} = 1225$$
   $$P(X = 2) = 1225 \times 0{,}0004 \times 0{,}3792 \approx 0{,}1858\text{ (soit } 18{,}58\%)$$

3. **Calcul de $P(X \ge 1)$ :**
   $$P(X \ge 1) = 1 - P(X = 0) = 1 - \binom{50}{0} \times (0{,}02)^0 \times (0{,}98)^{50} = 1 - 1 \times 1 \times (0{,}98)^{50}$$
   $$P(X \ge 1) \approx 1 - 0{,}3642 = 0{,}6358\text{ (soit } 63{,}58\%)$$

4. **Espérance et écart-type :**
   - Espérance : $E(X) = n \times p = 50 \times 0{,}02 = 1$.
     *Interprétation :* En moyenne, sur un lot de 50 puces, il y a 1 puce défectueuse.
   - Écart-type : $\sigma(X) = \sqrt{n \cdot p \cdot (1-p)} = \sqrt{50 \times 0{,}02 \times 0{,}98} = \sqrt{0{,}98} \approx 0{,}9899$.

---

### Exercice 1.3 : Événements contraires et indépendance
Soient deux événements $A$ et $B$ associés à une même expérience aléatoire tels que :
$$P(A) = 0{,}4 \quad ; \quad P(B) = 0{,}5 \quad ; \quad P(A \cup B) = 0{,}7$$

1. Les événements $A$ et $B$ sont-ils incompatibles ? Justifier.
2. Calculer $P(A \cap B)$.
3. Les événements $A$ et $B$ sont-ils indépendants ? Justifier.
4. Calculer la probabilité de l'événement contraire $P(\overline{A \cup B})$.

#### Correction 1.3
1. **Incompatibilité :**
   Si $A$ et $B$ étaient incompatibles, on aurait $P(A \cup B) = P(A) + P(B) = 0{,}4 + 0{,}5 = 0{,}9$. Or $P(A \cup B) = 0{,}7 \ne 0{,}9$. 
   Donc $A$ et $B$ ne sont **pas incompatibles** ($P(A \cap B) \ne 0$).

2. **Calcul de $P(A \cap B)$ :**
   $$P(A \cup B) = P(A) + P(B) - P(A \cap B) \implies P(A \cap B) = P(A) + P(B) - P(A \cup B)$$
   $$P(A \cap B) = 0{,}4 + 0{,}5 - 0{,}7 = 0{,}2$$

3. **Indépendance :**
   $$P(A) \times P(B) = 0{,}4 \times 0{,}5 = 0{,}20$$
   Puisque $P(A \cap B) = P(A) \times P(B) = 0{,}2$, les événements $A$ et $B$ sont **indépendants**.

4. **Événement contraire :**
   $$P(\overline{A \cup B}) = 1 - P(A \cup B) = 1 - 0{,}7 = 0{,}3$$

---

## Module 2 : Analyse, Dérivation et Étude de Fonctions

### Exercice 2.1 : Calculs de dérivées fondamentales et composées
Calculer la fonction dérivée $f'(x)$ pour chacune des fonctions suivantes définies sur l'intervalle donné :

1. $f_1(x) = 3x^4 - 5x^2 + \frac{2}{x} - 7 \quad \text{sur } ]0\,;\, +\infty[$
2. $f_2(x) = (2x^2 + 3) \cdot \cos(x) \quad \text{sur } \mathbb{R}$
3. $f_3(x) = \frac{4x - 1}{x^2 + 3} \quad \text{sur } \mathbb{R}$

#### Correction 2.1
1. **Pour $f_1(x)$ :**
   $$f_1'(x) = 3 \times (4x^3) - 5 \times (2x) + 2 \times \left(-\frac{1}{x^2}\right) - 0 = 12x^3 - 10x - \frac{2}{x^2}$$

2. **Pour $f_2(x)$ (forme $u \cdot v$) :**
   Posons $u(x) = 2x^2 + 3 \implies u'(x) = 4x$ et $v(x) = \cos(x) \implies v'(x) = -\sin(x)$.
   $$f_2'(x) = u'(x)v(x) + u(x)v'(x) = 4x \cos(x) + (2x^2 + 3)(-\sin(x)) = 4x \cos(x) - (2x^2 + 3)\sin(x)$$

3. **Pour $f_3(x)$ (forme $\frac{u}{v}$) :**
   Posons $u(x) = 4x - 1 \implies u'(x) = 4$ et $v(x) = x^2 + 3 \implies v'(x) = 2x$.
   $$f_3'(x) = \frac{u'(x)v(x) - u(x)v'(x)}{(v(x))^2} = \frac{4(x^2 + 3) - (4x - 1)(2x)}{(x^2 + 3)^2}$$
   $$f_3'(x) = \frac{4x^2 + 12 - (8x^2 - 2x)}{(x^2 + 3)^2} = \frac{-4x^2 + 2x + 12}{(x^2 + 3)^2}$$

---

### Exercice 2.2 : Étude de fonction polynôme et équation de tangente
Soit $f$ la fonction définie sur $\mathbb{R}$ par $f(x) = x^3 - 3x + 2$.

1. Calculer la dérivée $f'(x)$ et étudier son signe.
2. Dresser le tableau de variations complet de $f$ sur $\mathbb{R}$.
3. Déterminer l'équation de la tangente $\mathcal{T}$ à la courbe représentative de $f$ au point d'abscisse $a = 2$.

#### Correction 2.2
1. **Calcul et signe de la dérivée :**
   $$f'(x) = 3x^2 - 3 = 3(x^2 - 1) = 3(x - 1)(x + 1)$$
   Les racines de $f'(x)$ sont $x_1 = -1$ et $x_2 = 1$.
   Un polynôme du second degré est du signe de $a=3 > 0$ à l'extérieur des racines :
   - $f'(x) > 0$ sur $]-\infty\,;\, -1[ \ \cup \ ]1\,;\, +\infty[$
   - $f'(x) < 0$ sur $]-1\,;\, 1[$
   - $f'(x) = 0$ pour $x = -1$ et $x = 1$.

2. **Tableau de variations :**
   - $f(-1) = (-1)^3 - 3(-1) + 2 = -1 + 3 + 2 = 4$ (Maximum local)
   - $f(1) = 1^3 - 3(1) + 2 = 0$ (Minimum local)

   | $x$ | $-\infty$ | | $-1$ | | $1$ | | $+\infty$ |
   |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
   | $f'(x)$ | | $+$ | $0$ | $-$ | $0$ | $+$ | |
   | $f(x)$ | $-\infty$ | $\nearrow$ | $4$ | $\searrow$ | $0$ | $\nearrow$ | $+\infty$ |

3. **Équation de la tangente $\mathcal{T}$ en $a = 2$ :**
   La formule est $y = f'(a)(x - a) + f(a)$.
   - $f(2) = 2^3 - 3(2) + 2 = 8 - 6 + 2 = 4$
   - $f'(2) = 3(2)^2 - 3 = 12 - 3 = 9$

   $$y = 9(x - 2) + 4 \implies y = 9x - 18 + 4 \implies y = 9x - 14$$

---

### Exercice 2.3 : Second degré et optimisation
Un signal électrique traversing un composant produit une puissance thermique dissipée $P(I)$ (en Watts) en fonction de l'intensité $I$ (en Ampères) donnée par :
$$P(I) = -2I^2 + 12I + 5 \quad \text{pour } I \in [0\,;\, 5]$$

1. Résoudre l'équation $P(I) = 0$ sur $\mathbb{R}$ en utilisant le discriminant $\Delta$.
2. Déterminer l'intensité $I_{max}$ pour laquelle la puissance dissipée est maximale.
3. Quelle est la valeur de cette puissance maximale ?

#### Correction 2.3
1. **Résolution de $-2I^2 + 12I + 5 = 0$ :**
   Discriminant : $\Delta = b^2 - 4ac = 12^2 - 4(-2)(5) = 144 + 40 = 184$.
   Comme $\Delta > 0$, l'équation possède deux solutions réelles :
   $$I_1 = \frac{-b - \sqrt{\Delta}}{2a} = \frac{-12 - \sqrt{184}}{-4} = \frac{12 + \sqrt{184}}{4} \approx 6{,}39\text{ A}$$
   $$I_2 = \frac{-b + \sqrt{\Delta}}{2a} = \frac{-12 + \sqrt{184}}{-4} = \frac{12 - \sqrt{184}}{4} \approx -0{,}39\text{ A}$$

2. **Intensité $I_{max}$ pour la puissance maximale :**
   $P(I)$ est un polynôme du second degré de la forme $aI^2 + bI + c$ avec $a = -2 < 0$. La parabole a ses branches tournées vers le bas. Le maximum est atteint au sommet d'abscisse $\alpha = -\frac{b}{2a}$ :
   $$I_{max} = \frac{-12}{2(-2)} = \frac{-12}{-4} = 3\text{ A}$$
   La valeur $I = 3\text{ A}$ appartient bien à l'intervalle $[0\,;\, 5]$.

3. **Valeur de la puissance maximale :**
   $$P(3) = -2(3)^2 + 12(3) + 5 = -2(9) + 36 + 5 = -18 + 41 = 23\text{ W}$$

---

## Module 3 : Fonctions Exponentielles et Logarithmes

### Exercice 3.1 : Équations et inéquations avec $\exp$ et $\ln$
Résoudre dans $\mathbb{R}$ les équations et inéquations suivantes :

1. $e^{3x - 1} = 5$
2. $\ln(2x + 4) = 3$
3. $e^{2x} - 4e^x + 3 = 0$ (Indication : poser $X = e^x$)

#### Correction 3.1
1. **$e^{3x - 1} = 5$ :**
   Comme $5 > 0$, on applique le logarithme népérien des deux côtés :
   $$3x - 1 = \ln(5) \implies 3x = \ln(5) + 1 \implies x = \frac{\ln(5) + 1}{3} \approx 0{,}869$$
   $$S = \left\{ \frac{\ln(5) + 1}{3} \right\}$$

2. **$\ln(2x + 4) = 3$ :**
   - Ensemble de définition : $2x + 4 > 0 \implies x > -2$, soit $D = ]-2\,;\, +\infty[$.
   - Résolution : On applique l'exponentielle :
     $$2x + 4 = e^3 \implies 2x = e^3 - 4 \implies x = \frac{e^3 - 4}{2} \approx 8{,}043$$
   Puisque $\frac{e^3 - 4}{2} > -2$, la solution est valide. $S = \left\{ \frac{e^3 - 4}{2} \right\}$.

3. **$e^{2x} - 4e^x + 3 = 0$ :**
   En posant $X = e^x$ (avec $X > 0$), l'équation devient :
   $$X^2 - 4X + 3 = 0$$
   $\Delta = (-4)^2 - 4(1)(3) = 16 - 12 = 4 > 0$.
   $$X_1 = \frac{4 - 2}{2} = 1 \quad \text{et} \quad X_2 = \frac{4 + 2}{2} = 3$$
   On revient à $x$ :
   - $e^x = 1 \implies x = \ln(1) = 0$
   - $e^x = 3 \implies x = \ln(3)$
   
   $$S = \{0\,;\, \ln(3)\}$$

---

### Exercice 3.2 : Étude de fonction logarithme
Soit $f$ la fonction définie sur $]0\,;\, +\infty[$ par $f(x) = x - 2 - \ln(x)$.

1. Calculer la dérivée $f'(x)$ et déterminer son signe sur $]0\,;\, +\infty[$.
2. Déterminer les variations de $f$.
3. Déduire que pour tout $x > 0$, $f(x) \ge -1$.

#### Correction 3.2
1. **Dérivée $f'(x)$ :**
   $$f'(x) = 1 - 0 - \frac{1}{x} = 1 - \frac{1}{x} = \frac{x - 1}{x}$$
   Pour tout $x \in ]0\,;\, +\infty[$, le dénominateur $x$ est strictement positif. Le signe de $f'(x)$ dépend donc uniquement du numérateur $(x - 1)$ :
   - $f'(x) < 0$ si $x \in ]0\,;\, 1[$
   - $f'(x) = 0$ pour $x = 1$
   - $f'(x) > 0$ si $x \in ]1\,;\, +\infty[$

2. **Variations de $f$ :**
   - $f$ est strictement décroissante sur $]0\,;\, 1]$.
   - $f$ est strictly croissante sur $[1\,;\, +\infty[$.

3. **Minimum et inégalité :**
   La fonction admet un minimum absolu en $x = 1$.
   $$f(1) = 1 - 2 - \ln(1) = -1 - 0 = -1$$
   Par conséquent, pour tout $x \in ]0\,;\, +\infty[$, $f(x) \ge f(1)$, c'est-à-dire $f(x) \ge -1$.

---

### Exercice 3.3 : Charge d'un condensateur (Application physique)
Lors de la charge d'un condensateur de capacité $C$ à travers une résistance $R$, la tension aux bornes du condensateur est modélisée par :
$$u(t) = U_0 \left(1 - e^{-\frac{t}{\tau}}\right) \quad \text{pour } t \ge 0$$
où $U_0 = 10\text{ V}$ est la tension d'alimentation et $\tau = R \cdot C = 2\text{ ms}$ est la constante de temps du circuit.

1. Calculer la tension aux bornes du condensateur à l'instant $t = 2\text{ ms}$ (à $t = \tau$).
2. Déterminer la valeur limite de $u(t)$ quand $t$ tend vers $+\infty$.
3. Déterminer l'instant $t_1$ auquel la tension atteint $95\%$ de sa valeur maximale $U_0$.

#### Correction 3.3
1. **Tension à $t = \tau = 2\text{ ms}$ :**
   $$u(2) = 10 \left(1 - e^{-\frac{2}{2}}\right) = 10 (1 - e^{-1}) \approx 10 (1 - 0{,}3679) = 6{,}32\text{ V}$$
   *(À $t = \tau$, le condensateur est chargé à environ $63{,}2\%$).*

2. **Limite en $+\infty$ :**
   $$\lim_{t \to +\infty} -\frac{t}{2} = -\infty \implies \lim_{t \to +\infty} e^{-\frac{t}{2}} = 0$$
   Par conséquent, $\lim_{t \to +\infty} u(t) = 10(1 - 0) = 10\text{ V}$.

3. **Temps pour atteindre 95% de $U_0$ :**
   On cherche $t_1$ tel que $u(t_1) = 0{,}95 \times 10 = 9{,}5\text{ V}$.
   $$10 \left(1 - e^{-\frac{t_1}{2}}\right) = 9{,}5 \implies 1 - e^{-\frac{t_1}{2}} = 0{,}95 \implies e^{-\frac{t_1}{2}} = 0{,}05$$
   En appliquant la fonction logarithme népérien :
   $$-\frac{t_1}{2} = \ln(0{,}05) \implies t_1 = -2 \ln(0{,}05) \approx -2 \times (-2{,}9957) \approx 5{,}99\text{ ms}$$
   *(Soit environ $3\tau$).*

---

## Module 4 : Suites Numériques

### Exercice 4.1 : Suite arithmétique et modélisation
Un technicien réseau intervient sur des incidents. Le premier mois, il traite $u_1 = 120$ tickets. Chaque mois suivant, grâce à l'automatisation, le nombre de tickets à traiter diminue de $8$ tickets. On note $u_n$ le nombre de tickets traités le $n$-ième mois.

1. Donner la nature de la suite $(u_n)$ et préciser son premier terme $u_1$ et sa raison $r$.
2. Exprimer $u_n$ en fonction de $n$.
3. Combien de tickets le technicien traitera-t-il le 12-ième mois ?
4. Calculer le nombre total de tickets traités au cours de la première année (de $n=1$ à $n=12$).

#### Correction 4.1
1. **Nature de la suite :**
   Chaque terme s'obtient en retranchant 8 au terme précédent ($u_{n+1} = u_n - 8$). 
   $(u_n)$ est donc une **suite arithmétique** de premier terme $u_1 = 120$ et de raison $r = -8$.

2. **Formule explicite :**
   $$u_n = u_1 + (n - 1)r = 120 + (n - 1)(-8) = 120 - 8n + 8 = 128 - 8n$$

3. **Valeur de $u_{12}$ :**
   $$u_{12} = 128 - 8(12) = 128 - 96 = 32\text{ tickets}$$

4. **Somme des termes $S_{12}$ :**
   $$S_{12} = u_1 + u_2 + \dots + u_{12} = \text{Nombre de termes} \times \frac{\text{Premier terme} + \text{Dernier terme}}{2}$$
   $$S_{12} = 12 \times \frac{u_1 + u_{12}}{2} = 12 \times \frac{120 + 32}{2} = 12 \times 76 = 912\text{ tickets}$$

---

### Exercice 4.2 : Suite géométrique et amortissement
La valeur d'un serveur informatique s'élève à $u_0 = 4\,000$ € à l'achat. Chaque année, le serveur perd $15\%$ de sa valeur par rapport à l'année précédente. On note $u_n$ la valeur du serveur après $n$ années.

1. Montrer que la suite $(u_n)$ est géométrique et préciser sa raison $q$.
2. Exprimer $u_n$ en fonction de $n$.
3. Calculer la valeur estimée du serveur au bout de 5 ans (arrondir au centime).
4. Déterminer au bout de combien d'années la valeur du serveur deviendra inférieure à $1\,000$ €.

#### Correction 4.2
1. **Nature de la suite :**
   Diminuer de $15\%$ revient à multiplier par $1 - \frac{15}{100} = 0{,}85$.
   Ainsi, $u_{n+1} = 0{,}85 \times u_n$.
   $(u_n)$ est une **suite géométrique** de premier terme $u_0 = 4000$ et de raison $q = 0{,}85$.

2. **Formule explicite :**
   $$u_n = u_0 \times q^n = 4000 \times (0{,}85)^n$$

3. **Valeur après 5 ans ($u_5$) :**
   $$u_5 = 4000 \times (0{,}85)^5 = 4000 \times 0{,}443705 \approx 1\,774{,}82\ \text{€}$$

4. **Seuil de $1\,000$ € :**
   On cherche le plus petit entier $n$ tel que $u_n < 1000$ :
   $$4000 \times (0{,}85)^n < 1000 \implies (0{,}85)^n < \frac{1000}{4000} \implies (0{,}85)^n < 0{,}25$$
   Comme la fonction logarithme est strictement croissante :
   $$\ln\left((0{,}85)^n\right) < \ln(0{,}25) \implies n \cdot \ln(0{,}85) < \ln(0{,}25)$$
   Attention : $\ln(0{,}85) \approx -0{,}1625 < 0$, donc en divisant par $\ln(0{,}85)$, on inverse le sens de l'inégalité :
   $$n > \frac{\ln(0{,}25)}{\ln(0{,}85)} \approx \frac{-1{,}3863}{-0{,}1625} \approx 8{,}53$$
   Puisque $n$ doit être un entier, la valeur deviendra inférieure à $1\,000$ € au bout de **9 ans**.

---

### Exercice 4.3 : Suite arithmetico-géométrique
Soit la suite $(u_n)$ définie par $u_0 = 2$ et pour tout $n \in \mathbb{N}$, $u_{n+1} = 0{,}5 u_n + 3$.
On pose, pour tout $n \in \mathbb{N}$, $v_n = u_n - 6$.

1. Montrer que $(v_n)$ est une suite géométrique de raison $q = 0{,}5$ et préciser son terme initial $v_0$.
2. En déduire l'expression de $v_n$ puis de $u_n$ en fonction de $n$.
3. Déterminer la limite de la suite $(u_n)$ quand $n \to +\infty$.

#### Correction 4.3
1. **Démonstration de la nature de $(v_n)$ :**
   $$v_{n+1} = u_{n+1} - 6 = (0{,}5 u_n + 3) - 6 = 0{,}5 u_n - 3$$
   En factorisant par $0{,}5$ :
   $$v_{n+1} = 0{,}5 (u_n - 6) = 0{,}5 v_n$$
   Donc $(v_n)$ est une suite géométrique de raison $q = 0{,}5$.
   Son premier terme vaut : $v_0 = u_0 - 6 = 2 - 6 = -4$.

2. **Expressions de $v_n$ et $u_n$ :**
   - $v_n = v_0 \times q^n = -4 \times (0{,}5)^n$
   - Comme $v_n = u_n - 6 \implies u_n = v_n + 6$, d'où :
     $$u_n = 6 - 4 \times (0{,}5)^n$$

3. **Calcul de la limite :**
   Puisque $-1 < 0{,}5 < 1$, on a $\lim_{n \to +\infty} (0{,}5)^n = 0$.
   Par conséquent :
   $$\lim_{n \to +\infty} u_n = 6 - 4 \times 0 = 6$$

---

## Module 5 : Trigonométrie

### Exercice 5.1 : Équations trigonométriques fondamentales
Résoudre dans l'intervalle $]-\pi\,;\, \pi]$ les équations trigonométriques suivantes :

1. $\cos(x) = \frac{\sqrt{3}}{2}$
2. $\sin(2x) = -\frac{1}{2}$

#### Correction 5.1
1. **$\cos(x) = \frac{\sqrt{3}}{2}$ dans $]-\pi\,;\, \pi]$ :**
   Sur le cercle trigonométrique, les deux angles ayant un cosinus égal à $\frac{\sqrt{3}}{2}$ sont $\frac{\pi}{6}$ et $-\frac{\pi}{6}$.
   $$S = \left\{ -\frac{\pi}{6}\,;\, \frac{\pi}{6} \right\}$$

2. **$\sin(2x) = -\frac{1}{2}$ dans $]-\pi\,;\, \pi]$ :**
   On sait que $\sin(-\frac{\pi}{6}) = -\frac{1}{2}$. Ainsi, l'équation s'écrit $\sin(2x) = \sin(-\frac{\pi}{6})$.
   $$2x = -\frac{\pi}{6} + 2k\pi \quad \text{ou} \quad 2x = \pi - \left(-\frac{\pi}{6}\right) + 2k\pi \quad (k \in \mathbb{Z})$$
   $$x = -\frac{\pi}{12} + k\pi \quad \text{ou} \quad x = \frac{7\pi}{12} + k\pi$$
   Cherchons les valeurs de $k$ pour rester dans $]-\pi\,;\, \pi]$ :
   - Pour $x = -\frac{\pi}{12} + k\pi$ :
     - $k = 0 \implies x = -\frac{\pi}{12}$
     - $k = 1 \implies x = \frac{11\pi}{12}$
     - $k = -1 \implies x = -\frac{13\pi}{12}$ (hors intervalle)
   - Pour $x = \frac{7\pi}{12} + k\pi$ :
     - $k = 0 \implies x = \frac{7\pi}{12}$
     - $k = -1 \implies x = -\frac{5\pi}{12}$
     - $k = 1 \implies x = \frac{19\pi}{12}$ (hors intervalle)
   
   $$S = \left\{ -\frac{5\pi}{12}\,;\, -\frac{\pi}{12}\,;\, \frac{7\pi}{12}\,;\, \frac{11\pi}{12} \right\}$$

---

### Exercice 5.2 : Transformation de formule $a\cos(x) + b\sin(x)$
Soit l'expression $f(x) = \sqrt{3}\cos(x) + \sin(x)$.

1. Mettre $f(x)$ sous la forme d'une unique fonction sinusoïdale $A \cos(x - \varphi)$.
2. En déduire les valeurs maximales et minimales de $f(x)$.

#### Correction 5.2
1. **Mise sous forme amplitude/phase :**
   On calcule le facteur d'amplitude $A = \sqrt{a^2 + b^2} = \sqrt{(\sqrt{3})^2 + 1^2} = \sqrt{3 + 1} = \sqrt{4} = 2$.
   En factorisant par $2$ :
   $$f(x) = 2 \left( \frac{\sqrt{3}}{2}\cos(x) + \frac{1}{2}\sin(x) \right)$$
   On identifie un angle $\varphi$ tel que $\cos(\varphi) = \frac{\sqrt{3}}{2}$ et $\sin(\varphi) = \frac{1}{2}$, ce qui donne $\varphi = \frac{\pi}{6}$.
   En utilisant la formule d'addition $\cos(x - \varphi) = \cos(x)\cos(\varphi) + \sin(x)\sin(\varphi)$ :
   $$f(x) = 2 \left( \cos(x)\cos\left(\frac{\pi}{6}\right) + \sin(x)\sin\left(\frac{\pi}{6}\right) \right) = 2\cos\left(x - \frac{\pi}{6}\right)$$

2. **Valeurs extremums :**
   Puisque $-1 \le \cos\left(x - \frac{\pi}{6}\right) \le 1$ pour tout $x \in \mathbb{R}$ :
   - Le maximum vaut $2 \times 1 = 2$.
   - Le minimum vaut $2 \times (-1) = -2$.

---

### Exercice 5.3 : Signal sinusoïdal temporel (Application physique)
La tension $u(t)$ d'un signal alternatif est donnée par :
$$u(t) = 311 \cdot \sin(100\pi t + \frac{\pi}{4}) \quad \text{où } t \text{ est en secondes et } u(t) \text{ en Volts.}$$

1. Déterminer l'amplitude maximale $U_{max}$, la fréquence $f$ (en Hz) et la phase à l'origine $\varphi$.
2. Calculer la valeur efficace $U_{eff} = \frac{U_{max}}{\sqrt{2}}$.
3. Calculer la valeur instantanée $u(0)$ à l'instant $t = 0\text{ s}$.

#### Correction 5.3
1. **Paramètres de la forme $u(t) = U_{max}\sin(\omega t + \varphi)$ :**
   - Amplitude maximale : $U_{max} = 311\text{ V}$.
   - Pulsation : $\omega = 100\pi\text{ rad/s}$.
   - Fréquence : $f = \frac{\omega}{2\pi} = \frac{100\pi}{2\pi} = 50\text{ Hz}$.
   - Phase initiale : $\varphi = \frac{\pi}{4}\text{ rad}$.

2. **Tension efficace :**
   $$U_{eff} = \frac{311}{\sqrt{2}} \approx \frac{311}{1{,}4142} \approx 220\text{ V}$$

3. **Valeur à l'instant $t = 0$ :**
   $$u(0) = 311 \cdot \sin\left(100\pi(0) + \frac{\pi}{4}\right) = 311 \cdot \sin\left(\frac{\pi}{4}\right) = 311 \cdot \frac{\sqrt{2}}{2} \approx 220\text{ V}$$

---

## Module 6 : Nombres Complexes

### Exercice 6.1 : Forme algébrique et opérations
Soient les deux nombres complexes $z_1 = 3 + 4i$ et $z_2 = 1 - 2i$.

1. Calculer $z_1 + z_2$ et $z_1 - 2z_2$.
2. Calculer le produit $z_1 \cdot z_2$ sous forme algébrique.
3. Calculer le quotient $\frac{z_1}{z_2}$ sous forme algébrique.

#### Correction 6.1
1. **Somme et combinaison linéaire :**
   - $z_1 + z_2 = (3 + 4i) + (1 - 2i) = (3 + 1) + i(4 - 2) = 4 + 2i$
   - $z_1 - 2z_2 = (3 + 4i) - 2(1 - 2i) = 3 + 4i - 2 + 4i = 1 + 8i$

2. **Produit :**
   $$z_1 \cdot z_2 = (3 + 4i)(1 - 2i) = 3 - 6i + 4i - 8i^2$$
   Rappel : $i^2 = -1$.
   $$z_1 \cdot z_2 = 3 - 2i - 8(-1) = 3 - 2i + 8 = 11 - 2i$$

3. **Quotient (en multipliant par le conjugué) :**
   Le conjugué de $z_2 = 1 - 2i$ est $\overline{z_2} = 1 + 2i$.
   $$\frac{z_1}{z_2} = \frac{(3 + 4i)(1 + 2i)}{(1 - 2i)(1 + 2i)} = \frac{3 + 6i + 4i + 8i^2}{1^2 - (2i)^2} = \frac{3 + 10i - 8}{1 - (-4)}$$
   $$\frac{z_1}{z_2} = \frac{-5 + 10i}{5} = \frac{-5}{5} + i \frac{10}{5} = -1 + 2i$$

---

### Exercice 6.2 : Passage forme algébrique $\leftrightarrow$ forme trigonométrique / exponentielle
1. Soit $z_A = -2 + 2i\sqrt{3}$.
   - Calculer le module $|z_A|$.
   - Déterminer un argument $\arg(z_A)$.
   - En déduire la forme trigonométrique et la forme exponentielle de $z_A$.
2. Soit $z_B = 4 e^{i\frac{2\pi}{3}}$. Donner la forme algébrique de $z_B$.

#### Correction 6.2
1. **Étude de $z_A = -2 + 2i\sqrt{3}$ ($a = -2$, $b = 2\sqrt{3}$) :**
   - Module :
     $$|z_A| = \sqrt{(-2)^2 + (2\sqrt{3})^2} = \sqrt{4 + 12} = \sqrt{16} = 4$$
   - Argument :
     $$\begin{cases} \cos(\theta) = \frac{a}{|z_A|} = \frac{-2}{4} = -\frac{1}{2} \\[6pt] \sin(\theta) = \frac{b}{|z_A|} = \frac{2\sqrt{3}}{4} = \frac{\sqrt{3}}{2} \end{cases} \implies \theta = \pi - \frac{\pi}{3} = \frac{2\pi}{3} \quad [2\pi]$$
   - Formes représentatives :
     - Forme trigonométrique : $z_A = 4 \left( \cos\left(\frac{2\pi}{3}\right) + i \sin\left(\frac{2\pi}{3}\right) \right)$
     - Forme exponentielle : $z_A = 4 e^{i\frac{2\pi}{3}}$

2. **Forme algébrique de $z_B = 4 e^{i\frac{2\pi}{3}}$ :**
   $$z_B = 4 \left( \cos\left(\frac{2\pi}{3}\right) + i \sin\left(\frac{2\pi}{3}\right) \right)$$
   On sait que $\cos\left(\frac{2\pi}{3}\right) = -\frac{1}{2}$ et $\sin\left(\frac{2\pi}{3}\right) = \frac{\sqrt{3}}{2}$.
   $$z_B = 4 \left( -\frac{1}{2} + i \frac{\sqrt{3}}{2} \right) = -2 + 2i\sqrt{3}$$

---

### Exercice 6.3 : Application en Électricité (Calcul d'impédance complexe)
Dans un circuit $RLC$ série alimenté par un courant alternatif de fréquence $f$, l'impédance complexe totale est donnée par :
$$\underline{Z} = R + j\left(L\omega - \frac{1}{C\omega}\right) \quad (\text{avec } j^2 = -1)$$
On donne : $R = 30\ \Omega$, $L\omega = 80\ \Omega$, et $\frac{1}{C\omega} = 40\ \Omega$.

1. Déterminer l'expression algébrique de l'impédance complexe $\underline{Z}$.
2. Calculer le module $|\underline{Z}|$ (représentant l'impédance réelle du circuit en Ohms).
3. Calculer le déphasage $\varphi = \arg(\underline{Z})$ du courant par rapport à la tension.

#### Correction 6.3
1. **Forme algébrique de $\underline{Z}$ :**
   $$\underline{Z} = 30 + j (80 - 40) = 30 + 40j\ \Omega$$

2. **Impédance réelle $|\underline{Z}|$ :**
   $$|\underline{Z}| = \sqrt{30^2 + 40^2} = \sqrt{900 + 1600} = \sqrt{2500} = 50\ \Omega$$

3. **Déphasage $\varphi = \arg(\underline{Z})$ :**
   $$\begin{cases} \cos(\varphi) = \frac{30}{50} = 0{,}6 \\[6pt] \sin(\varphi) = \frac{40}{50} = 0{,}8 \end{cases}$$
   $$\tan(\varphi) = \frac{40}{30} = \frac{4}{3} \implies \varphi = \arctan\left(\frac{4}{3}\right) \approx 0{,}927\text{ rad (soit environ } 53{,}13^\circ\text{)}$$
</entry>
# Correction — TP Dérivation et thermique
**BTS CIEL 1re année — 20 février / 13 mars 2026**

---

## Exercice 1 — Modélisation de la température d'un microprocesseur

On cherche les réels $a$ et $b$ tels que $f(t) = (at + b)\,e^{-0{,}3t}$ modélise la température (en °C) du microprocesseur en fonction du temps $t$ (en secondes).

---

### Question 1 — Détermination de $a$ et $b$

**Condition 1 :** À $t = 0$, la température vaut 20 °C.

\\[f(0) = (a \times 0 + b)\,e^{0} = b \times 1 = b = 20\\]

\\[\Rightarrow \boxed{b = 20}\\]

**Condition 2 :** Le coefficient directeur de la tangente à l'origine vaut 4, c'est-à-dire $f'(0) = 4$.

On admet provisoirement (cf. Q2) que $f'(t) = (4 - 3t)\,e^{-0{,}3t}$, donc :

\\[f'(0) = (4 - 0)\,e^{0} = 4 \quad \checkmark\\]

Pour retrouver $a$, on développe la dérivée à partir de la règle du produit (voir Q2). On trouve que la condition $f'(0) = 4$ avec $b = 20$ donne :

\\[a - 0{,}3 \times 20 = 4 \Rightarrow a - 6 = 4 \Rightarrow a = 10\\]

\\[\Rightarrow \boxed{a = 10}\\]

**Expression de la fonction :**

\\[\boxed{f(t) = (10t + 20)\,e^{-0{,}3t}}\\]

---

### Question 2 — Calcul de la dérivée de $f$

On applique la **règle de dérivation d'un produit** $(uv)' = u'v + uv'$ avec :

| | Expression | Dérivée |
|---|---|---|
| $u(t)$ | $10t + 20$ | $u'(t) = 10$ |
| $v(t)$ | $e^{-0{,}3t}$ | $v'(t) = -0{,}3\,e^{-0{,}3t}$ |

\\[f'(t) = 10 \cdot e^{-0{,}3t} + (10t + 20) \cdot (-0{,}3)\,e^{-0{,}3t}\\]

On factorise par $e^{-0{,}3t}$ (qui ne s'annule jamais) :

\\[f'(t) = e^{-0{,}3t}\,\bigl[10 - 0{,}3(10t + 20)\bigr]\\]

\\[f'(t) = e^{-0{,}3t}\,\bigl[10 - 3t - 6\bigr]\\]

\\[\boxed{f'(t) = (4 - 3t)\,e^{-0{,}3t}} \quad \checkmark\\]

---

### Question 3 — Signe de $f'(t)$ et tableau de variation

**Analyse du signe de $f'(t) = (4 - 3t)\,e^{-0{,}3t}$ :**

- $e^{-0{,}3t} > 0$ pour tout réel $t$ (une exponentielle est toujours strictement positive).
- Le signe de $f'(t)$ est donc celui de $4 - 3t$.

\\[4 - 3t > 0 \iff t < \frac{4}{3} \approx 1{,}33 \text{ s}\\]

\\[4 - 3t < 0 \iff t > \frac{4}{3}\\]

**Valeur du maximum :**

\\[\!\left(\frac{4}{3}\right) = \left(10 \times \frac{4}{3} + 20\right)e^{-0{,}3 \times \frac{4}{3}} = \left(\frac{40}{3} + \frac{60}{3}\right)e^{-0{,}4} = \frac{100}{3}\,e^{-0{,}4} \approx 33{,}33 \times 0{,}6703 \approx \mathbf{22{,}34 \text{ °C}}\\]

**Tableau de variation de $f$ sur $[0\,;+\infty[$ :**

\\[\begin{array}{c|ccccc}
t & 0 & & \dfrac{4}{3} & & +\infty \\\\
\hline
f'(t) & & + & 0 & - & \\\\
\hline
f(t) & 20 & \nearrow & 22{,}34 & \searrow & 0
\end{array}\\]

> **Limite en $+\infty$ :** $\displaystyle\lim_{t \to +\infty} f(t) = 0$ car $t\,e^{-0{,}3t} \to 0$ et $e^{-0{,}3t} \to 0$.

---

### Question 4 — Équation de la tangente en $t = 0$

L'équation de la tangente à la courbe de $f$ au point d'abscisse $t_0$ est :

\\[y = f'(t_0)\,(t - t_0) + f(t_0)\\]

Avec $t_0 = 0$ :

- $f(0) = (10 \times 0 + 20)\,e^{0} = 20$
- $f'(0) = (4 - 3 \times 0)\,e^{0} = 4$

\\[\boxed{y = 4t + 20}\\]

**Interprétation :** Au démarrage, la température augmente de 4 °C par seconde. (vitesse instantanée)

---

### Question 5 — Instant où la température dépasse 22 °C

On cherche les valeurs de $t \geq 0$ telles que $f(t) > 22$, soit :

\\[(10t + 20)\,e^{-0{,}3t} = 22\\]

Cette équation ne se résout pas analytiquement. On utilise **Géogebra** : on trace $f(t) = (10t + 20)\,e^{-0{,}3t}$ et la droite horizontale $y = 22$, puis on lit les abscisses des points d'intersection.

**Résultat :**

Géogebra donne deux solutions : $t_1 \approx 0{,}11$ s et $t_2 \approx 2{,}07$ s.

> D'après le tableau de variation, $f$ croît de 20 à 22,34 °C puis redescend. La température dépasse donc 22 °C sur l'intervalle $[t_1\,;\,t_2]$.

\\[\boxed{t_1 \approx 0{,}11 \text{ s} \quad \text{et} \quad t_2 \approx 2{,}07 \text{ s}}\\]

**Conclusion :** La température du microprocesseur dépasse 22 °C dès **$t \approx 0{,}11$ s** et repasse en dessous à partir de **$t \approx 2{,}07$ s**. Un système de refroidissement doit intervenir dans cet intervalle.

---

## Exercice 2 — Énergie dissipée par le microprocesseur

On a $p(t) = 5t\,e^{-0{,}3t}$ (puissance en watts).

---

### Question 1 — Recherche d'une primitive $P$ de $p$

On cherche une primitive de $p(t) = 5t\,e^{-0{,}3t}$.

On utilise la méthode de **primitivation par parties**, en s'appuyant sur la forme connue :

$\\[\text{Si } f(t) = (at + b)\,e^{-0{,}3t}, \text{ alors } f'(t) = a\,e^{-0{,}3t} - 0{,}3(at+b)\,e^{-0{,}3t} = \bigl[a - 0{,}3at - 0{,}3b\bigr]e^{-0{,}3t}\\]

On cherche $a$ et $b$ tels que $f'(t) = 5t\,e^{-0{,}3t}$, c'est-à-dire :

\\[-0{,}3a = 5 \Rightarrow a = -\frac{50}{3}\\]
\\[a - 0{,}3b = 0 \Rightarrow -\frac{50}{3} - 0{,}3b = 0 \Rightarrow b = -\frac{50}{3 \times 0{,}3} = -\frac{50}{0{,}9} = -\frac{500}{9}\\]

**Vérification :**

\\[P'(t) = -\frac{50}{3}\,e^{-0{,}3t} + \left(-\frac{50}{3}t - \frac{500}{9}\right)(-0{,}3)\,e^{-0{,}3t}\\]

\\[= e^{-0{,}3t}\left[-\frac{50}{3} + \frac{50}{10}t + \frac{500}{30}\right] = e^{-0{,}3t}\left[-\frac{50}{3} + 5t + \frac{50}{3}\right] = 5t\,e^{-0{,}3t} \quad \checkmark\\]

\\[\boxed{P(t) = \left(-\frac{50}{3}t - \frac{500}{9}\right)e^{-0{,}3t}}\\]

---

### Question 2 — Primitive $H$ vérifiant $H(0) = 0$

Toutes les primitives de $p$ sont de la forme $P(t) + C$ où $C$ est une constante réelle.

On cherche $C$ tel que $H(0) = 0$ :

\\[H(0) = P(0) + C = 0\\]

\\[P(0) = \left(-\frac{50}{3} \times 0 - \frac{500}{9}\right)e^{0} = -\frac{500}{9}\\]

\\[-\frac{500}{9} + C = 0 \Rightarrow C = \frac{500}{9}\\]

\\[\boxed{H(t) = \left(-\frac{50}{3}t - \frac{500}{9}\right)e^{-0{,}3t} + \frac{500}{9}}\\]

**Vérification :** $H(0) = -\dfrac{500}{9} + \dfrac{500}{9} = 0$ ✓

---

### Question 3 — Énergie dissipée au bout de 20 secondes

L'énergie totale dissipée entre $t = 0$ et $t = 20$ s est :

\\[E = H(20) - H(0) = H(20)\\]

**Calcul de $H(20)$ :**

\\[-\frac{50}{3} \times 20 = -\frac{1000}{3}\\]

\\[-\frac{1000}{3} - \frac{500}{9} = -\frac{3000}{9} - \frac{500}{9} = -\frac{3500}{9}\\]

\\[e^{-0{,}3 \times 20} = e^{-6} \approx 0{,}002479\\]

\\[H(20) = -\frac{3500}{9} \times e^{-6} + \frac{500}{9} \approx -388{,}89 \times 0{,}002479 + 55{,}56\\]

\\[H(20) \approx -0{,}964 + 55{,}556 \approx 54{,}59\\]

\\[\boxed{E \approx 55 \text{ joules}}\\]

**Interprétation :** Le microprocesseur dissipe environ **55 joules** d'énergie thermique durant les 20 premières secondes de fonctionnement.

---


###### tags: `bts`, `ciel`, `maths`, `2026`
# Correction : Dérivation

## Partie A : Calculs techniques

1. **$f(x) = (3x-2)\sqrt{x}$** : Formule $(uv)' = u'v + uv'$.

   $u(x) = 3x-2 \Rightarrow u'(x) = 3$

   $v(x) = \sqrt{x} \Rightarrow v'(x) = \frac{1}{2\sqrt{x}}$

   $f'(x) = 3\sqrt{x} + \frac{3x-2}{2\sqrt{x}} = \frac{6x + 3x - 2}{2\sqrt{x}} = \frac{9x - 2}{2\sqrt{x}}$.

2. **$g(x) = (2x^2-5)^4$** : Formule $(u^n)' = n \cdot u' \cdot u^{n-1}$.

   $u(x) = 2x^2-5 \Rightarrow u'(x) = 4x$.

   $g'(x) = 4 \times 4x \times (2x^2-5)^3 = 16x(2x^2-5)^3$.

3. **$h(x) = \frac{1}{x^2+x+1}$** : Formule $(\frac{1}{u})' = -\frac{u'}{u^2}$.

   $u(x) = x^2+x+1 \Rightarrow u'(x) = 2x+1$.

   $h'(x) = -\frac{2x+1}{(x^2+x+1)^2}$.

4. **$k(x) = \frac{2x+1}{x-3}$** : Formule $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$.

   $k'(x) = \frac{2(x-3) - 1(2x+1)}{(x-3)^2} = \frac{2x-6-2x-1}{(x-3)^2} = \frac{-7}{(x-3)^2}$.

---

## Partie B : Étude de fonction

1. **Dérivée :** $f(x) = \frac{x^2 - 3x}{x^2 + 1}$.
   $f'(x) = \frac{(2x-3)(x^2+1) - 2x(x^2-3x)}{(x^2+1)^2} = \frac{2x^3+2x-3x^2-3-2x^3+6x^2}{(x^2+1)^2} = \frac{3x^2+2x-3}{(x^2+1)^2}$.

2. **Signe et Variations :** Le dénominateur est un carré positif. On étudie le signe de $3x^2+2x-3$.

   $\Delta = 2^2 - 4(3)(-3) = 4 + 36 = 40$.

   Racines : $x_1 = \frac{-2-\sqrt{40}}{6} \approx -1,39$ et $x_2 = \frac{-2+\sqrt{40}}{6} \approx 0,72$.

   Le trinôme est positif à l'extérieur des racines.

   * $f$ est croissante sur $]-\infty ; x_1]$, décroissante sur $[x_1 ; x_2]$ et croissante sur $[x_2 ; +\infty[$.

3. **Tangente en $0$ :** $y = f'(0)(x-0) + f(0)$.

   $f(0) = \frac{0}{1} = 0$.

   $f'(0) = \frac{-3}{1^2} = -3$.

   Équation : **$y = -3x$**.

---

## Partie C : Optimisation (Boîte)

1. **Volume :** La base est un carré de côté $(20-2x)$ et la hauteur est $x$.

   $V(x) = \text{Aire de la base} \times \text{hauteur} = (20-2x)^2 \times x$.

2. **Maximum :** On dérive $V(x) = x(400 - 80x + 4x^2) = 4x^3 - 80x^2 + 400x$.

   $V'(x) = 12x^2 - 160x + 400$.

   $\Delta = (-160)^2 - 4(12)(400) = 25600 - 19200 = 6400$.

   $\sqrt{\Delta} = 80$.

   $x_1 = \frac{160-80}{24} = \frac{80}{24} = \frac{10}{3} \approx 3,33$ cm.

   $x_2 = \frac{160+80}{24} = 10$ (Volume nul, correspond au minimum).

   **Le volume est maximal pour $x = 10/3$ cm.**
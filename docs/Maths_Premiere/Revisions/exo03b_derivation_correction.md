# Correction : Dérivation et Étude de fonctions (Variante)

---

## Partie A : Calcul de dérivées

**1. Produit ($u \cdot v$) :** $f(x) = (2x - 5)(x^2 + 3x)$

* On pose $u(x) = 2x - 5 \implies u'(x) = 2$

* On pose $v(x) = x^2 + 3x \implies v'(x) = 2x + 3$

* $f'(x) = u'v + uv' = 2(x^2 + 3x) + (2x - 5)(2x + 3)$

* $f'(x) = 2x^2 + 6x + (4x^2 + 6x - 10x - 15) = \mathbf{6x^2 + 2x - 15}$

**2. Puissance ($u^n$) :** $g(x) = (3x^2 - 4x + 1)^3$

* On pose $u(x) = 3x^2 - 4x + 1 \implies u'(x) = 6x - 4$

* La formule est $g'(x) = n \cdot u' \cdot u^{n-1}$

* $g'(x) = 3(6x - 4)(3x^2 - 4x + 1)^2 = \mathbf{(18x - 12)(3x^2 - 4x + 1)^2}$


**3. Inverse ($1/u$) :** $h(x) = \frac{1}{x^2 + 4}$

* On pose $u(x) = x^2 + 4 \implies u'(x) = 2x$

* La formule est $h'(x) = -\frac{u'}{u^2}$

* $h'(x) = \mathbf{-\frac{2x}{(x^2 + 4)^2}}$

**4. Somme et inverse :** $k(x) = x^2 + \frac{1}{2x + 1}$

* La dérivée de $x^2$ est $2x$.

* Pour $\frac{1}{2x + 1}$, on pose $u(x) = 2x + 1 \implies u'(x) = 2$. La dérivée est $-\frac{2}{(2x+1)^2}$.

* $k'(x) = \mathbf{2x - \frac{2}{(2x + 1)^2}}$

---

## Partie B : Étude complète

**1. Dérivée par le produit :** $f(x) = (x - 2)(x^2 + 2x + 4)$

* $u(x) = x - 2 \implies u'(x) = 1$

* $v(x) = x^2 + 2x + 4 \implies v'(x) = 2x + 2$

* $f'(x) = 1(x^2 + 2x + 4) + (x - 2)(2x + 2)$

* $f'(x) = x^2 + 2x + 4 + (2x^2 + 2x - 4x - 4) = \mathbf{3x^2}$

**2. Vérification par développement :**

* $f(x) = x(x^2 + 2x + 4) - 2(x^2 + 2x + 4) = x^3 + 2x^2 + 4x - 2x^2 - 4x - 8$

* $f(x) = x^3 - 8$

* En dérivant $x^3 - 8$, on retrouve bien **$f'(x) = 3x^2$**.

**3. Variations :**

* Pour tout réel $x$, $x^2 \geq 0$, donc $f'(x) = 3x^2 \geq 0$.

* La dérivée ne s'annule qu'en $0$. La fonction $f$ est donc **strictement croissante** sur $\mathbb{R}$.

**4. Tangente en $x=1$ :**

* Équation : $y = f'(1)(x - 1) + f(1)$

* $f'(1) = 3(1)^2 = 3$


* $f(1) = 1^3 - 8 = -7$
* $y = 3(x - 1) - 7 \implies \mathbf{y = 3x - 10}$

---

## Partie C : Le plaisir de l'optimisation

**1. Expression de $y$ :**

Le périmètre clôturé est $2x + y = 40$. En isolant $y$, on a bien **$y = 40 - 2x$**.

**2. Expression de l'aire :**

* $A(x) = \text{largeur} \times \text{longueur} = x \times y$

* $A(x) = x(40 - 2x) = \mathbf{-2x^2 + 40x}$

**3. Maximum de l'aire :**


* La fonction $A$ est dérivable : $A'(x) = -4x + 40$.

* $A'(x) = 0 \iff -4x = -40 \iff x = 10$.

* Comme $A'(x)$ est une fonction affine décroissante, elle est positive avant $10$ et négative après. L'aire est donc maximale pour **$x = 10$ m**.

* L'aire maximale est $A(10) = 10(40 - 20) = \mathbf{200 \text{ m}^2}$.
# 📝 Corrigé : C106 – Les Primitives

---

## Exercice 1 : Calculs de Primitives Usuelles
*Rappel : La primitive de $x^n$ est $\frac{x^{n+1}}{n+1}$ et celle de $e^{ax}$ est $\frac{1}{a}e^{ax}$.*

1.  **$f(x) = 4x^3 - 6x^2 + 2$**
    * Terme $4x^3$ : $4 \times \frac{x^4}{4} = x^4$
    * Terme $6x^2$ : $6 \times \frac{x^3}{3} = 2x^3$
    * Terme $2$ : $2x$
    * **$F(x) = x^4 - 2x^3 + 2x + k$**

2.  **$g(x) = 5e^x$**
    * La primitive de $e^x$ reste $e^x$.
    * **$G(x) = 5e^x + k$**

3.  **$h(x) = 3\cos(x) + 2\sin(x)$**
    * Primitive de $\cos(x)$ est $\sin(x)$.
    * Primitive de $\sin(x)$ est $-\cos(x)$.
    * **$H(x) = 3\sin(x) - 2\cos(x) + k$**

4.  **$k(x) = e^{-2x}$**
    * On utilise la forme $e^{ax}$ avec $a = -2$.
    * **$K(x) = -\frac{1}{2}e^{-2x} + k$**

---

## Exercice 2 : Primitive particulière et Exponentielle
*Objectif : Déterminer la valeur exacte de la constante $k$ à partir d'une condition initiale.*



1.  **Forme générale des primitives de $f(t) = 12e^{-4t}$ :**
    * On applique la formule $\frac{1}{a}e^{at}$ avec $a = -4$.
    * $F(t) = 12 \times \left( \frac{1}{-4} e^{-4t} \right) + k$
    * **$F(t) = -3e^{-4t} + k$**

2.  **Détermination de $k$ avec la condition $F_0(0) = 10$ :**
    * $F_0(0) = -3e^{-4 \times 0} + k = 10$
    * $-3e^{0} + k = 10$  *(Rappel : $e^0 = 1$)*
    * $-3 + k = 10$
    * $k = 10 + 3 = 13$

3.  **Expression complète :**
    * **$F_0(t) = -3e^{-4t} + 13$**

---

## Exercice 3 : Condition Initiale (Logarithme)
*Rappel : La primitive de $\frac{1}{x}$ est $\ln(x)$ sur $]0 ; +\infty[$.*

1.  **Forme générale de $g(x) = \frac{1}{x} + 1$ :**
    * **$G(x) = \ln(x) + x + k$**

2.  **Détermination de $G_0$ telle que $G_0(1) = 5$ :**
    * $G_0(1) = \ln(1) + 1 + k = 5$
    * $0 + 1 + k = 5$  *(Rappel : $\ln(1) = 0$)*
    * $k = 4$
    * **$G_0(x) = \ln(x) + x + 4$**

3.  **Valeur exacte de $G_0(e)$ :**
    * $G_0(e) = \ln(e) + e + 4$
    * $G_0(e) = 1 + e + 4$  *(Rappel : $\ln(e) = 1$)*
    * **$G_0(e) = e + 5$**

---

## Exercice 4 : Application aux Sciences Physiques
*Contexte : $u(t)$ est la primitive de $\frac{i(t)}{C}$.*



1.  **Expression de la tension $u(t)$ :**
    * On calcule d'abord le coefficient : $\frac{1}{C} = \frac{1}{500 \times 10^{-6}} = 2000$.
    * On doit intégrer : $\frac{i(t)}{C} = 2000 \times 0,05 \sin(100\pi t) = 100 \sin(100\pi t)$.
    * La primitive de $\sin(at)$ est $-\frac{1}{a}\cos(at)$.
    * $u(t) = 100 \times \left( -\frac{1}{100\pi} \cos(100\pi t) \right) + k$
    * **$u(t) = -\frac{1}{\pi} \cos(100\pi t) + k$**

2.  **Calcul de la constante avec $u(0) = 0$ :**
    * $u(0) = -\frac{1}{\pi} \cos(0) + k = 0$
    * $-\frac{1}{\pi} \times 1 + k = 0$
    * $k = \frac{1}{\pi}$
    * **Expression finale : $u(t) = -\frac{1}{\pi} \cos(100\pi t) + \frac{1}{\pi}$ ou $u(t) = \frac{1}{\pi} \left( 1 - \cos(100\pi t) \right)$**
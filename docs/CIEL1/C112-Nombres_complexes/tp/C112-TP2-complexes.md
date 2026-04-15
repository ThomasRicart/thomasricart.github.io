# C112 - TP2 : Rotation, Déphasage et Puissances

**Objectif :** Comprendre l'impact de la multiplication complexe (effet d'une impédance).

## 1. La multiplication par $i$ (Rotation)
1. Créez un point libre $z_A$.
2. Calculez son image par $i$ : `z_B = z_A * i`.
3. Tracez les segments $[Oz_A]$ et $[Oz_B]$.
   > **Question :** Quel est l'angle $\widehat{z_A O z_B}$ ? Que peut-on dire du module de $z_B$ par rapport à celui de $z_A$ ?

## 2. Application : Tension et Courant
En électronique, $U = Z \cdot I$. Imaginons un courant $I$ de module 1.
1. Créez un curseur `ωt` (angle).
2. Définissez le courant : `I = cos(ωt) + i * sin(ωt)`.
3. Définissez une impédance de bobine : `Z_L = 3i`.
4. Calculez la tension : `U_L = Z_L * I`.
   > **Observation :** En faisant varier `ωt`, observez le vecteur $U_L$. Est-il en avance ou en retard de $90^\circ$ sur le courant $I$ ?

## 3. Puissances et Moivre
1. Créez un point $z_C = 1.1 e^{i \pi / 6}$ (en tapant `z_C = 1.1 * exp(i * pi / 6)`).
2. Créez un curseur entier `n` allant de $1$ à $15$.
3. Saisissez : `Liste = Sequence(z_C^k, k, 1, n)`.
   > **Analyse :** Pourquoi les points forment-ils une spirale ? Justifiez à l'aide de la propriété du cours sur $(r e^{i\theta})^n$.
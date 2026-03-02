# Correction : Vecteurs et Produit Scalaire

## Partie A : Repère orthonormé

1. **Coordonnées :**

   $\vec{AB} = (4 - (-2) ; 3 - 1) = (6 ; 2)$

   $\vec{AC} = (1 - (-2) ; 5 - 1) = (3 ; 4)$

2. **Produit scalaire :**

   $\vec{AB} \cdot \vec{AC} = xx' + yy' = 6 \times 3 + 2 \times 4 = 18 + 8 = 26$.

3. **Angle $\widehat{BAC}$ :**

   On sait que $\vec{AB} \cdot \vec{AC} = AB \times AC \times \cos(\widehat{BAC})$.

   $AB = \sqrt{6^2 + 2^2} = \sqrt{40}$

   $AC = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$

   $26 = \sqrt{40} \times 5 \times \cos(\widehat{BAC}) \Rightarrow \cos(\widehat{BAC}) = \frac{26}{5\sqrt{40}} \approx 0,822$.

   L'angle $\widehat{BAC} \approx \arccos(0,822) \approx 35^\circ$.

4. **Orthogonalité :**

   $\vec{AB} \cdot \vec{AC} = 26 \neq 0$, donc les vecteurs ne sont pas orthogonaux. Le triangle n'est pas rectangle en $A$.

---

## Partie B : Géométrie plane

1. **Relation de Chasles :** 

$\vec{DI} = \vec{DA} + \vec{AI} = \vec{DA} + \frac{1}{2}\vec{AB}$.

2. **Projection :** 

Pour $\vec{AC} \cdot \vec{AB}$, le projeté orthogonal de $C$ sur $(AB)$ est le point $B$.

   Donc $\vec{AC} \cdot \vec{AB} = \vec{AB} \cdot \vec{AB} = AB^2 = 8^2 = 64$.

3. **Calcul de $\vec{DI} \cdot \vec{AC}$ :**

   $\vec{DI} \cdot \vec{AC} = (\vec{DA} + \frac{1}{2}\vec{AB}) \cdot (\vec{AB} + \vec{AD})$

   $= \vec{DA} \cdot \vec{AB} + \vec{DA} \cdot \vec{AD} + \frac{1}{2}\vec{AB} \cdot \vec{AB} + \frac{1}{2}\vec{AB} \cdot \vec{AD}$

   Comme $ABCD$ est un rectangle, les produits scalaires de vecteurs orthogonaux sont nuls.

   $= 0 - AD^2 + \frac{1}{2}AB^2 + 0 = -4^2 + \frac{1}{2}(8^2) = -16 + 32 = 16$.

   Le produit scalaire est non nul, donc les droites ne sont pas perpendiculaires.

---

## Partie C : Al-Kashi

1. **Longueur $FG$ :**

   D'après le théorème d'Al-Kashi : $FG^2 = EF^2 + EG^2 - 2 \times EF \times EG \times \cos(60^\circ)$.

   $FG^2 = 5^2 + 8^2 - 2 \times 5 \times 8 \times 0,5 = 25 + 64 - 40 = 49$.

   Donc **$FG = 7$**.

2. **Produit scalaire :**

   $\vec{EF} \cdot \vec{EG} = 5 \times 8 \times \cos(60^\circ) = 40 \times 0,5 = 20$.
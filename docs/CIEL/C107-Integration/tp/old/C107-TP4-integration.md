# TP 4: Synthèse d'Analyse - Détermination et Étude du signal $p(x)$

**Objectif :** Déterminer les paramètres d'un signal à partir de contraintes géométriques, puis valider son étude par la dérivation et l'intégration.

---

## Partie 1 : Détermination expérimentale des paramètres
On cherche à modéliser un signal par la fonction suivante :  
$p(x) = kx^2 + mx + \ln(x)$

Le signal doit respecter deux contraintes physiques :

1. Passer par le point de mesure **$A(1 ; 2)$**.

2. Présenter un **maximum** (tangente horizontale) à l'instant **$x = 1$**.

**Instructions GeoGebra :**

1. Créez deux curseurs `k` et `m` allant de -5 à 5 (incrément 0.1).

2. Saisissez la fonction : `p(x) = k*x^2 + m*x + ln(x)`.

3. Placez le point cible `A = (1, 2)`.

4. Créez un point `M` sur la courbe, placez-le précisément à $x=1$ et tracez sa **tangente** (Outil Tangente).

5. **Mission :** Ajustez les curseurs `k` et `m` pour que la courbe passe par `A` et que la tangente en $x=1$ soit horizontale.

   * *Note : Les valeurs cibles sont $k = -1.5$ et $m = 2$.*



---

## Partie 2 : Étude du signal identifié
Utilisez maintenant les valeurs trouvées ($k = -1.5$ et $m = 2$) pour analyser le comportement du signal.

1. **Étude des variations :**
   - Saisissez `p'(x)` pour afficher la fonction dérivée.
   - *Question :* Justifiez par le calcul que la fonction est croissante sur $]0 ; 1]$ puis décroissante sur $[1 ; +\infty[$.

2. **Analyse de la pente :**
   - Placer un point `N` appartenant à la courbe et tracer la tangente en ce point
   - Déplacez le point `N` vers la droite (grandes valeurs de $x$).
   - *Observation :* Pourquoi la pente de la tangente devient-elle de plus en plus négative ? Quel terme de la fonction ($x^2$ ou $\ln(x)$) "gagne" sur l'autre à long terme ?

---

## Partie 3 : Intégration et Valeur Moyenne
On souhaite évaluer la valeur moyenne du signal sur une fenêtre temporelle choisie.

1. **Configuration :** Créez deux curseurs `a` (min 0.1) et `b` (min 0.1). Réglez `a = 1` et `b = 4`.

2. **Calcul global :** Saisissez `I = Intégrale(p, a, b)` pour obtenir l'aire sous la courbe.

3. **Valeur Moyenne $\mu$ :**

   - Calculez la hauteur moyenne : `moy = I / (b - a)`.
   - **Visualisation :** Créez le rectangle d'équivalence avec les points `(a,0)`, `(b,0)`, `(b, moy)` et `(a, moy)`. Utilisez l'outil **Polygone** pour le colorer.



4. **Validation théorique (Calcul papier) :**
   - En utilisant la linéarité et la primitive de $\ln(x)$ qui est $(x\ln(x) - x)$, déterminez la primitive $P(x)$ de votre signal.
   - *Rappel :* $P(x) = \display_style\int (-1.5x^2 + 2x + \ln(x)) dx$.
   - **Calcul :** Calculez la valeur exacte de $\mu$ pour l'intervalle $[1 ; 2]$.
   - **Vérification :** Comparez votre résultat avec la valeur `moy` affichée par GeoGebra.
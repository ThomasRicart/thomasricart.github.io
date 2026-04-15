# TP 3: Synthèse d'Analyse - Modélisation et Moyenne d'un signal exponentiel

**Objectif :** Déterminer le paramètre d'un signal amorti à partir de contraintes géométriques, puis valider son étude par la dérivation et l'intégration.

---

## Partie 1 : Détermination expérimentale du paramètre $c$
On cherche à modéliser un signal par la fonction suivante :  
$f(x) = x e^{-cx}$ (où $c > 0$)

Le signal doit respecter une contrainte physique précise :
1. Présenter un **maximum** (tangente horizontale) à l'instant **$x = 0,5$**.

**Instructions GeoGebra :**

1. Créez un curseur **`c`** allant de 0.1 à 5 (incrément 0.1).

2. Saisissez la fonction : `f(x) = x * exp(-c*x)`.

3. Créez un point **`M`** sur la courbe, placez-le précisément à $x=0,5$ et tracez sa **tangente** (Outil Tangente).

4. **Mission :** Ajustez le curseur **`c`** pour que la tangente en $x=0,5$ soit horizontale.
   * *Note : La valeur cible à trouver est $c = 2$.*



---

## Partie 2 : Étude du signal identifié
Utilisez maintenant la valeur trouvée (**$c = 2$**) pour analyser le comportement du signal.

1. **Étude des variations :**
   - Saisissez `f'(x)` pour afficher la fonction dérivée.
   - *Question :* Justifiez par le calcul que la fonction est croissante sur $[0 ; 0,5]$ puis décroissante sur $[0,5 ; +\infty[$.

2. **Analyse de la pente :**
   - Placez un point `N` appartenant à la courbe et tracez la tangente en ce point.
   - Déplacez le point `N` vers la droite (grandes valeurs de $x$).
   - *Observation :* Pourquoi la pente de la tangente tend-elle vers 0 ? Quel terme de la fonction ($x$ ou $e^{-2x}$) "gagne" sur l'autre à long terme ?

---

## Partie 3 : Intégration et Valeur Moyenne
On souhaite évaluer la valeur moyenne du signal sur une fenêtre temporelle choisie.

1. **Configuration :** Créez deux curseurs **`a`** (min 0) et **`b`** (min 0.1). Réglez `a = 0` et `b = 2`.

2. **Calcul global :** Saisissez `I = Intégrale(f, a, b)` pour obtenir l'aire sous la courbe.

3. **Valeur Moyenne $\mu$ :**
   - Calculez la hauteur moyenne : `moy = I / (b - a
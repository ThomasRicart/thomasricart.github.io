# C112 - TP3 : Étude de la Résonance d'un Circuit RLC

**Objectif :** Visualiser l'annulation de la partie imaginaire d'une impédance complexe.

## 1. Paramétrage du circuit
Créez les curseurs suivants :
* `f` (Fréquence) : de $10$ à $2000$ Hz.
* `R` (Résistance) : de $10$ à $100$ $\Omega$.
* `L` (Inductance) : $0.1$ H.
* `C` (Capacité) : $10 \mu F$ (tapez `C = 0.00001`).
* Calculez la pulsation : `ω = 2 * pi * f`.

## 2. Construction du diagramme d'impédance
Saisissez les impédances complexes :
1. `Z_R = R`
2. `Z_L = i * L * ω`
3. `Z_C = -i / (C * ω)`
4. `Z_tot = Z_R + Z_L + Z_C`
5. Tracez le vecteur : `V_Z = Vector(Z_tot)`.

## 3. Analyse de la Résonance
1. **Manipulation :** Faites varier la fréquence `f`. 
2. **Observation :** Trouvez la fréquence précise pour laquelle le vecteur `V_Z` devient parfaitement horizontal (sa partie imaginaire est nulle).
   > **Note :** C'est la fréquence de résonance $f_0$.
3. **Calcul de contrôle :** Calculez $f_{th} = 1 / (2\pi \sqrt{LC})$. Est-ce proche de votre observation ?

## 4. Courbe de réponse
1. Créez le point `M = (f, abs(Z_tot))`.
2. Activez la **Trace** de ce point `M`.
3. Faites varier `f` de $10$ à $1000$ Hz.
   > **Question :** Que représente le point le plus bas de la courbe ainsi tracée ?
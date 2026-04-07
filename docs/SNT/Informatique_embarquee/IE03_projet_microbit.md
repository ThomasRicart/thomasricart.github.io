# 🕹️ Réaliser une Interface Homme-Machine (IHM)
## Séance 3 — Mini projet carte micro:bit
**SNT — Seconde** | Durée : ~2 heures

---

## 🎯 Objectif du projet

Vous allez concevoir et programmer **votre propre objet connecté** simulé dans Tinkercad avec une carte micro:bit.

Votre objet devra :
- Utiliser **au moins 1 capteur**
- Utiliser **au moins 1 actionneur** (affichage LED, etc.)
- Proposer une **IHM** avec les boutons A et/ou B
- Avoir un **usage réel** (vous devrez expliquer à quoi ça sert)

---

## 📋 ÉTAPE 1 — Choisir et décrire votre projet (15 min)

### [Idées de projets](https://microbit.org/fr/projects/make-it-code-it/) (choisissez-en un ou proposez le vôtre !)

### ✏️ Fiche de projet — À remplir AVANT de coder

**Nom du projet :** ...

**Noms des élèves :** ...

**Description en une phrase :** ...

**À quoi ça sert dans la vraie vie ?** ...

### ✏️ Tableau des composants

Identifiez les composants de votre système **avant de programmer** :

| Composant | Nom précis | Rôle dans votre projet |
|-----------|------------|------------------------|
| Capteur 1 | ... | ... |
| Capteur 2 (si utilisé) | ... | ... |
| IHM — Entrée | ... | ... |
| IHM — Sortie | ... | ... |
| Actionneur | ... | ... |


---
## 📋 ÉTAPE 2 — Concevoir l'algorithme (20 min)

Avant d'écrire du code, décrivez le comportement de votre programme en **langage naturel** (pseudo-code).

### Exemple (pour le projet Alerte canicule) :
```
Initialisation :
  seuil = 25

Boucle infinie :
  Lire la température
  Si bouton A appuyé :
    Augmenter le seuil de 1 degré
    Afficher le nouveau seuil
  Sinon si bouton B appuyé :
    Diminuer le seuil de 1 degré
    Afficher le nouveau seuil
  Sinon :
    Si température > seuil :
      Afficher image DANGER + faire défiler "CHAUD"
    Sinon :
      Afficher image HAPPY
  Attendre 200 ms
```

### ✏️ Votre algorithme en pseudo-code :

```
Initialisation :
  ...

Boucle infinie :
  ...
  Si ... :
    ...
  Sinon si ... :
    ...
  Sinon :
    ...
```

---
## 📋 ÉTAPE 3 — Coder et tester dans Tinkercad (50 min)

### Rappel des fonctions micro:bit utiles

```python
from microbit import *
import random

# ── AFFICHAGE ──────────────────────────────────
display.show(Image.HAPPY)          # Image prédéfinie
display.show("A")                  # Un caractère
display.scroll("Texte")            # Faire défiler du texte
display.show(42)                   # Un nombre
display.clear()                    # Éteindre les LEDs

# ── BOUTONS ────────────────────────────────────
button_a.is_pressed()              # True si A est maintenu
button_a.was_pressed()             # True si A a été appuyé (une fois)
button_b.is_pressed()              # Idem pour B
button_a.get_pressed()             # Renvoie le nombre de fois ou A est pressé

# ── CAPTEUR DE TEMPÉRATURE ─────────────────────
t = temperature()                  # Température en degrés Celsius

# ── ACCÉLÉROMÈTRE ──────────────────────────────
accelerometer.was_gesture('shake') # Détection secousse
accelerometer.was_gesture('tilt_left')  # Inclinaison gauche
accelerometer.was_gesture('tilt_right') # Inclinaison droite
accelerometer.get_x()             # Valeur brute axe X

# ── BOUSSOLE ───────────────────────────────────
compass.heading()                  # Direction en degrés (0=Nord)

# ── TIMING ─────────────────────────────────────
sleep(500)                         # Pause de 500 millisecondes

# ── ALÉATOIRE ──────────────────────────────────
de = random.randint(1, 6)               # Entier aléatoire entre 1 et 6

# ── IMAGES UTILES ──────────────────────────────
# Image.HAPPY, Image.SAD, Image.ANGRY, Image.SURPRISED
# Image.HEART, Image.SKULL, Image.ARROW_N, Image.ARROW_S
# Image.YES, Image.NO, Image.CHESSBOARD, Image.DIAMOND
```
---
---
## 📋 ÉTAPE 5 — Présentation et bilan (10 min)

### ✏️ Présentation du projet

Répondez aux questions suivantes pour préparer votre présentation orale :

1. **Quel est votre projet et à quoi sert-il ?**  
   ...

2. **Quels sont les capteurs et actionneurs utilisés ?**  
   ...

3. **Comment fonctionne l'IHM (les boutons) ?**  
   ...

4. **Quelle a été la principale difficulté ?**  
   ...

5. **Qu'amélioreriez-vous si vous aviez plus de temps ?**  
   ...

---
## 💡 Conseils et aide

### Si vous êtes bloqués...

**Problème : le bouton est détecté plusieurs fois**  
→ Utilisez `was_pressed()` plutôt que `is_pressed()`

**Problème : l'affichage clignote ou est illisible**  
→ Ajoutez un `sleep(200)` à la fin de la boucle

**Problème : `display.scroll()` bloque le programme**  
→ Utilisez `display.scroll("texte", wait=False)` pour ne pas bloquer

**Problème : je ne sais pas comment structurer le code**  
→ Reprenez votre pseudo-code et traduisez ligne par ligne

```python
# Structure générale recommandée :
from microbit import *

# 1. Initialisation des variables
# ...

# 2. Boucle principale
while True:
    # 3. Lecture des entrées (capteurs, boutons)
    # ...
    
    # 4. Traitement (if/elif/else)
    # ...
    
    # 5. Sorties (affichage, actionneurs)
    # ...
    
    # 6. Pause
    sleep(100)
```



<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

# 🛡️ TP Co-Enseignement : Mathématiques & Informatique
## Thème : Cryptographie Linéaire – Le Chiffre de Hill

---

### 1. Introduction
En **BTS CIEL**, la sécurisation des communications est primordiale. Le **Chiffre de Hill**, inventé en 1929, est un algorithme de cryptographie symétrique qui utilise le calcul matriciel. 

Contrairement aux chiffrements simples qui travaillent lettre par lettre, le chiffre de Hill traite les lettres par **groupes (blocs)**. Cela empêche de casser le code simplement en comptant la fréquence des lettres, car une même lettre peut être chiffrée différemment selon sa voisine.

---

### 2. Rappel Théorique
#### 📜 Chiffrement
On remplace chaque lettre par son rang dans l'alphabet ($A=0, B=1, \dots, Z=25$).
Pour chiffrer un bloc $P = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$ avec une matrice clé $K$, on calcule :

$$C = (K \times P) \pmod{26}$$

#### 🔓 Déchiffrement
Pour retrouver le message d'origine, on doit utiliser la matrice inverse $K^{-1}$ telle que :

$$P = (K^{-1} \times C) \pmod{26}$$

*Note : En arithmétique modulaire, le calcul de l'inverse est spécifique et nécessite que le déterminant de la matrice soit premier avec 26.*

---

### 3. Travail Préparatoire (Mathématiques)
*À réaliser avant de passer sur ordinateur.*

On donne la matrice clé $K = \begin{pmatrix} 3 & 3 \\ 2 & 5 \end{pmatrix}$ et sa matrice inverse $K^{-1} = \begin{pmatrix} 15 & 17 \\ 20 & 9 \end{pmatrix}$.

**Question 1 : Chiffrement manuel**
1. Convertir le bloc de lettres **"CO"** en nombres $x_1$ et $x_2$. (C=2, O=14).
2. Calculez le vecteur chiffré $C$ :
   - $y_1 = (3 \times x_1 + 3 \times x_2) \pmod{26}$
   - $y_2 = (2 \times x_1 + 5 \times x_2) \pmod{26}$
3. Quel est le bloc chiffré (en lettres) ?

**Question 2 : Déchiffrement manuel**
On reçoit le bloc chiffré **"WW"** (soit le vecteur $C = \begin{pmatrix} 22 \\ 22 \end{pmatrix}$). Utilisons $K^{-1}$ pour décoder :
1. Calculez les valeurs d'origine $x_1$ et $x_2$ :
   - $x_1 = (15 \times 22 + 17 \times 22) \pmod{26}$
   - $x_2 = (20 \times 22 + 9 \times 22) \pmod{26}$
2. Vérifiez que vous retrouvez bien les nombres correspondant à **"CO"**.
   > *Astuce : Pour le modulo sur de grands nombres, divisez par 26 et gardez le reste.*

---

### 4. Partie Informatique : Code à compléter
**Consigne :** Complétez les zones marquées `TODO` dans le script Python pour automatiser le processus.

```python
# ==========================================================
# TP : CHIFFRE DE HILL - BTS CIEL
# ==========================================================

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Matrices fournies
CLE_K = [[3, 3], [2, 5]]
CLE_INV = [[15, 17], [20, 9]]

def lettre_vers_nombre(lettre):
    return ALPHABET.index(lettre.upper())

def nombre_vers_lettre(nombre):
    return ALPHABET[nombre % 26]

def produit_hill(matrice, bloc_nombres):
    """Effectue le calcul matriciel ligne par colonne modulo 26"""
    # TODO : Implémenter le calcul de y1 et y2
    y1 = (matrice[0][0] * bloc_nombres[0] + matrice[0][1] * bloc_nombres[1]) % 26
    y2 = (matrice[1][0] * bloc_nombres[0] + matrice[1][1] * bloc_nombres[1]) % 26
    return [y1, y2]

def traiter_message(message, matrice):
    message = message.upper().replace(" ", "")
    
    # TODO : Gérer les messages de longueur impaire
    if len(message) % 2 != 0:
        message += "X"
    
    resultat = ""
    for i in range(0, len(message), 2):
        # TODO : Extraire le bloc, transformer et convertir en texte
        paire_lettres = message[i:i+2]
        nombres_clairs = [lettre_vers_nombre(paire_lettres[0]), lettre_vers_nombre(paire_lettres[1])]
        
        nombres_transformes = produit_hill(matrice, nombres_clairs)
        
        resultat += nombre_vers_lettre(nombres_transformes[0])
        resultat += nombre_vers_lettre(nombres_transformes[1])
        
    return resultat

# --- ZONE DE TESTS ---
# 1. Tester le chiffrement de "CODE"
print(f"Chiffrement de 'CODE' : {traiter_message('CODE', CLE_K)}")

# 2. DEFI : Déchiffrer le message secret "CPZP"
# secret = traiter_message("CPZP", CLE_INV)
# print(f"Le mot secret est : {secret}")
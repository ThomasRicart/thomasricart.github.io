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

### CHIFFREMENT
def produit_hill(matrice, bloc_nombres):
    """Effectue le calcul matriciel ligne par colonne modulo 26
    Correspond au chiffrement de bloc_nombre par matrice"""
    # TODO : Implémenter le calcul de y1 et y2
    y1 = 0 # A modifier
    y2 = 0 # A modifier
    return [y1, y2]

def test_produit_hill():
    print(f'--- Test de la fonction produit_hill---')
    print(f'La clef est {CLE_K}')
    print(f'Le bloc nombre est [0, 2]')
    print(f'Le produit de hill doit être [6, 10]')
    print(f'Analyse de ce que renvoie la fonction:')
    return produit_hill(CLE_K, [0,2])


### TRAITEMENT DU MESSAGE
def traiter_message(message, matrice):
    message = message.upper().replace(" ", "")

    # TODO : Gérer les messages de longueur impaire
    # Si le message est de longueur impaire, on lui ajoute la lettre 'X' à la fin
    # A compléter


    resultat = ""
    for i in range(0, len(message), 2):
        # TODO : Extraire le bloc, transformer et convertir en texte
        # Extraire le bloc de deux lettres
        paire_lettres = 'AA'    # A modifier

        # Liste de nombres en clairs
        nombres_clairs = [0, 0] # A modifier

        # Liste de nombres transformés par le poduit de hill
        nombres_transformes = [0, 0]    # A modifier

        # Liste de lettres transformées
        lettres_transformees = ['A', 'A']   # A modifier

        # Ajout des nouvelles lettres au résultat
        resultat = resultat + 'A' # A modifier
    return resultat

# --- ZONE DE TESTS ---
# 1. Tester le chiffrement de "CODE"
print(f"Chiffrement de 'CODE' : {traiter_message('CODE', CLE_K)}")

# 2. DEFI : Déchiffrer le message secret "CPZP"
secret = traiter_message("CPZP", CLE_INV)
print(f"Le mot secret est : {secret}")
# ==========================================================

```
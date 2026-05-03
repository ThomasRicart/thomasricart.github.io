# Créé par thoma, le 03/05/2026 en Python 3.7

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
    y1 = (matrice[0][0] * bloc_nombres[0] + matrice[0][1] * bloc_nombres[1]) % 26
    y2 = (matrice[1][0] * bloc_nombres[0] + matrice[1][1] * bloc_nombres[1]) % 26
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

    resultat = ""
    for i in range(0, len(message), 2):
        # TODO : Extraire le bloc, transformer et convertir en texte
        # Extraire le bloc de deux lettres
        paire_lettres = message[i:i+2]

        # Liste de nombres en clairs
        nombres_clairs = [lettre_vers_nombre(paire_lettres[0]), lettre_vers_nombre(paire_lettres[1])]

        # Liste de nombres transformés par le poduit de hill
        nombres_transformes = produit_hill(matrice, nombres_clairs)

        # Liste de lettres transformées
        lettres_transformees = [nombre_vers_lettre(nombres_transformes[0]), nombre_vers_lettre(nombres_transformes[1])]

        # Ajout des nouvelles lettres au résultat
        #resultat += nombre_vers_lettre(nombres_transformes[0])
        #resultat += nombre_vers_lettre(nombres_transformes[1])
        resultat += lettres_transformees[0] + lettres_transformees[1]
    return resultat

# --- ZONE DE TESTS ---
# 1. Tester le chiffrement de "CODE"
print(f"Chiffrement de 'CODE' : {traiter_message('CODE', CLE_K)}")

# 2. DEFI : Déchiffrer le message secret "CPZP"
secret = traiter_message("CPZP", CLE_INV)
print(f"Le mot secret est : {secret}")
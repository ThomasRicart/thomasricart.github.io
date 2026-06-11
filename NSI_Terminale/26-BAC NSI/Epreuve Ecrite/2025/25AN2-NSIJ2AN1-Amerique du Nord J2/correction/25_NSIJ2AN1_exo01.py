def nb_occurrences(tab, i):
    nb_occ = {}
    for j in range(3 * i, 3 * (i + 1)):
        x = tab[j]
        if x in nb_occ:
            nb_occ[x] += 1        # Ligne 14
        else:
            nb_occ[x] = 1         # Ligne 16
    return nb_occ

def majorite(dict):
    cle_max = None
    valeur_max = -1
    for cle in dict.keys():
        if dict[cle] > valeur_max:    # Ligne 11
            valeur_max = dict[cle]    # Ligne 12
            cle_max = cle             # Ligne 13
    return cle_max

def erreur_colonne(mat):
    for col in range(len(mat[0])):
        somme = 0
        for ligne in range(len(mat)):
            somme += mat[ligne][col]
        if somme % 2 == 1:  # Parité impaire = erreur
            return col

def corriger_erreur(code_recu):
    # si le code est correct, on le retourne
    if code_recu in hamming_4_7:
        return code_recu
    else:
        # copie du code reçu
        code = [bit for bit in code_recu]     # Ligne 17
        # on teste chaque bit
        for indice in range(7):
            # on inverse le bit
            code[indice] = (code[indice] + 1) % 2    # Ligne 20
            # on teste si le code est correct
            if code in hamming_4_7:
                return code
            # sinon on reinitialise le bit à sa valeur d'origine
            else:
                code[indice] = code_recu[indice]     # Ligne 25

def decode(arbre, code, i):
    # si on est arrivé à une feuille, retourner l'étiquette
    if i == len(code):
        return arbre.etiquette
    # on est sur un noeud
    # on suit la branche correspondant à la valeur du bit
    if code[i] == 0:
        # on suit la branche gauche
        # on incrémente le bit
        return decode(arbre.gauche, code, i+1)    # Ligne 12
    if code[i] == 1:
        # on suit la branche droite
        # on incrémente le bit
        return decode(arbre.droit, code, i+1)     # Ligne 14



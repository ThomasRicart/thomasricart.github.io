import ascii

#############################################################################
# Question 1 et 2 : Écrire les codes des fonctions bin2dec et qrcode2dec
#              Proposer un test de qrcode2dec
#############################################################################


# implémentation du QR Code de la figure 1:
qrcode_fig1 = ascii.figure1

def bin2dec(val_bin):
    ''' Renvoie l'entier correspondant à val_bin
    val_bin (tuple)
    sortie (int) '''
    # initialisatoin de val_dec
    val_dec = 0
    # initialisation de la puissance de 2
    n = 7
    # Pour chaque bit du tuple
    for bit in val_bin:
        # calcul de la la valeur à ajouter
        p = bit * 2 ** n
        # ajout de la puissance à val_dec
        val_dec += p
        # diminuton de la puissance de 2
        n -= 1
    return val_dec

def test_bin2dec():
    assert bin2dec((1, 1, 1, 1, 1, 1, 1, 1)) == 255
    assert bin2dec((0, 0, 0, 0, 0, 0, 0, 0)) == 0
    assert bin2dec((1, 0, 1, 0, 1, 0, 1, 0)) == 170

def qrcode2dec(tuple_list):
    ''' Renvoie une liste d'entiers correspondant à la liste de tuples
    tuple_list: (list of tuple)
    sortie: (list of int) '''
    qrcode = []
    for ligne in tuple_list:
        val_dec = bin2dec(ligne)
        qrcode.append(val_dec)
    return qrcode

# print(qrcode2dec(ascii.figure1))
assert qrcode2dec(ascii.figure1) == [77, 46, 72, 97, 114, 97]

# implémentation du QR Code de la figure 1:
qrcode_fig1 = ascii.figure1

# test sur la première ligne du QR code:
#print(bin2dec(qrcode_fig1[0]))

#############################################################################
# Question 3 : Fonctions dec2str et test_dec2str
#############################################################################
def dec2str(liste_dec):
    """ entrée: liste d'entiers décimaux
        sortie: chaine de caractère formée des caractères correspondant
        de la table ascii """
    table_ascii = ascii.dict_ascii
    chaine = ""
    for entier in liste_dec:
        # Vérification que entier est une clé de la table_ascii
        if entier in table_ascii.keys():
            chaine += table_ascii[entier]
        else:
            chaine += '?'   # remplacement par un caractère random
    return chaine

def test_dec2str():
    """ Teste la fonction dec2str avec des données issues du module fourni """
    tests = [ascii.test1, ascii.test2, ascii.test3]
    for test in tests:
        print(dec2str(test))

def qrcode2str(qrcode):
    return dec2str(qrcode2dec(qrcode))

#############################################################################
# Question 4 : Fonction str2qrcode déficiente
#############################################################################

def str2qrcode(message):
    """
    Convertit une chaine de caractères en liste de tuples binaires.
    """
    qrcode = []
    table_inverse = {valeur: cle for cle, valeur in ascii.dict_ascii.items()}

    for caractere in message:
        entier = table_inverse.get(caractere, 63)
        binaire_str = bin(entier)[2:]
        # Vérification de la longueur du tuple
        if len(binaire_str) < 8:
            binaire_str = '0'*(8-len(binaire_str)) + binaire_str
        ligne = tuple(int(bit) for bit in binaire_str)
        qrcode.append(ligne)

    return qrcode
# Probleme: le codage ne se fait pas sur 8 bits!

# Validation de l'erreur
assert str2qrcode('M.Hara') == ascii.figure1



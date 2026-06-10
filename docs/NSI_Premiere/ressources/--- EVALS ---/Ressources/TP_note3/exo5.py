### Exercice 5
f = open("pg4548_modif.txt", mode = "r", encoding = "utf-8")
texte = f.read()
tab = texte.split()
f.close()
#print(texte)
print(len(tab))



def occurrences(tableau):
    occ = {}
    for lettre in tableau:
        if lettre in occ.keys():
            occ[lettre] = occ[lettre] + 1
        else:
            occ[lettre] = 1
    return occ

def mot_6_lettres(d):
    dico = {}
    for mot in d:
        if len(mot) == 6:
            if mot in dico.keys():
                dico[mot] = dico[mot] + 1
            else:
                dico[mot] = 1
    val_max = max(dico.values())

    for cle in dico:
        if dico[cle] == val_max:
            return cle

string = texte
characters = ",.!?-;»"

string = ''.join( x for x in string if x not in characters)
#print(string)





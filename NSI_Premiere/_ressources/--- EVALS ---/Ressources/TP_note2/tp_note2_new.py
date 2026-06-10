# Créé par Thomas, le 08/04/2022 en Python 3.7
def recherche_min(liste):
    val_min = liste[0]
    i_min = 0
    for i in range(len(liste)):
        if liste[i] < val_min:
            val_min = liste[i]
            i_min = i
    return i_min


def tri_exo4(L):
    n = len(L)
    for i in range(0,n):
        print(L[i:n])
        j = recherche_min(L[i:n]) + i
        L[i] , L[j] = L[j] , L[i]
        #print(L)
    return L


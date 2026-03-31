import time

def tri_selection(liste):
    n = len(liste)
    for i in range(0,n-1):
        # On recherche le plus petit élément de la liste non triée [i;n-1]
        mini = i
        for j in range(i+1,n):
            if liste[j] < liste[mini]:
                mini = j
        # Echange des éléemnts d'indice i et mini
        liste[i] , liste[mini] = liste[mini] , liste[i]

L = [2,5,1,0,-9]
tri_selection(L)
print(L)


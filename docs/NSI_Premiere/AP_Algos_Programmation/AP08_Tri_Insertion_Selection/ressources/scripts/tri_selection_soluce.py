### Algorithme de tri par sélecton sur une liste en place
def indice_mini(liste,i):
    ### Recherche du minimum d'une sous-liste ###
    i_min , element_min = i , liste[i]
    for j in range(i,len(liste)):
        if liste[j] < element_min:
            element_min = liste[j]
            i_min = j
    return(i_min)

def tri_selection(liste):
    for i in range(len(liste)-1):
        i_min = indice_mini(liste,i)
        if i < i_min:
            liste[i] , liste[i_min] = liste[i_min] , liste[i]

liste = [3,8,1,13,4,21,5,2]
tri_selection(liste)                # Tri de la liste en place
assert liste == [1, 2, 3, 4, 5, 8, 13, 21]
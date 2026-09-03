def tri_selection(liste):
    for i in range(len(liste)-1):
        i_min = indice_mini(liste,i)
        if i < i_min:
            liste[i] , liste[i_min] = liste[i_min] , liste[i]
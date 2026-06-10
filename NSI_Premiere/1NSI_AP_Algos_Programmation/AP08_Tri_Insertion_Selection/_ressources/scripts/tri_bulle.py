def tri_bulle(liste):
    permutation = True
    passage = 0
    while permutation == True:
        permutation = False
        passage = passage + 1
        for en_cours in range(0,len(liste)-passage):
            if liste[en_cours] > liste[en_cours + 1]:
                permutation = True
                # On échange les deux éléments
                liste[en_cours] , liste[en_cours + 1] = liste[en_cours + 1],liste[en_cours]

liste = [2,1,4,5,-2,0]
tri_bulle(liste)
print(liste)
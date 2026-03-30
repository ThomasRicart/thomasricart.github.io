import time
from random import *
from pylab import *
#############################################################################
###         TRI INSERTION ###################################################
#############################################################################
def indice_mini(liste,i):
    element_min = liste[i]
    i_min = i
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
#############################################################################
###         TRI INSERTION ###################################################
#############################################################################
def decalage_valeurs(liste,i):
    liste[i] = liste[i-1]

def tri_insertion(liste):
    for i in range(len(liste)-1):
        k = i + 1           # indice de la clé
        cle = liste[k]      # récuperation de la clé
        while cle < liste[k-1] and k > 0:   # verif position de la clé
            decalage_valeurs(liste,k)
            k = k - 1                       # Décalage suivant
        liste[k] = cle      # placement de la clé au bon endroit
#############################################################################
###         TRI INSERTION ###################################################
#############################################################################
def calcul_temps(nb_valeurs):
    liste = [i for i in range(nb_valeurs)]
    shuffle(liste)
    l1 = liste[:]
    l2 = liste[:]
    ### Tri par sélection
    t1_TS = time.process_time()
    tri_selection(l1)
    t2_TS = time.process_time()
    duree_tri_selection = t2_TS - t1_TS
    ### Tri par insertion
    t1_TI = time.process_time()
    tri_insertion(l2)
    t2_TI = time.process_time()
    duree_tri_insertion = t2_TI - t1_TI
    ####################
    return(nb_valeurs,duree_tri_selection,duree_tri_insertion)

def trace_courbe(n):
    x,y1,y2=[],[],[]
    for i in range(n):
        temps = calcul_temps(10**(i+1))
        nb_valeurs , duree_S , duree_I = temps[0],temps[1],temps[2]
        x.append(nb_valeurs)
        y1.append(duree_S)
        y2.append(duree_I)
    plot(x,y1,label="Tri par selection")
    plot(x,y2,label="Tri par insertion")
    legend()
    show()




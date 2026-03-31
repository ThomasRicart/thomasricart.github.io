import time
from random import randint
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(3100)

# Créé par Thomas, le 01/06/2024 en Python 3.7
def tri_selection(L):
    n = len(L)
    for i in range(0,n-1):
        mini = i
        for j in range(i+1, n):
            if L[j] < L[mini]:
                mini = j
        L[i], L[mini] = L[mini], L[i]

def tri_insertion(L):
    n = len(L)
    for i in range(1, n):
        k = i                               # Indice de la clé
        # Tant que le bord de la liste n'est pas atteint
        # ET que le suivant est plus petit que le précédent
        while k > 0 and L[k] < L[k-1]:
            L[k-1], L[k] = L[k], L[k-1]     # Echange des deux éléments
            k = k - 1                       # La clé se déplace vers la gauche


def temps_exec(fonction, n):
    L =[randint(0,n) for _ in range(n)]
    debut = time.time()
    fonction(L)
    fin = time.time()
    return(fin - debut)

def tableau(max):
    plt.close()
    abs = [i for i in range(0, max, 1000)]
    ord = []
    for i in range(0, max, 1000):
        ord.append(temps_exec(tri_insertion, i))
    plt.plot(abs, ord, label = "tri insertion")
    abs = [i for i in range(0, max, 1000)]
    ord = []
    for i in range(0, max, 1000):
        ord.append(temps_exec(tri_selection, i))
    plt.plot(abs, ord, label = "tri selection")
    plt.legend()
    plt.show()


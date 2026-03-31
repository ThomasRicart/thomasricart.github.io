import time
def tri_insertion(liste):
    for i in range(1,len(liste)):
        k = i       # la cle est liste[k]
        while liste[k] < liste[k-1] and k > 0:
            liste[k-1] , liste[k] = liste[k] , liste[k-1]
            k = k - 1

#n= 10
#liste = [n-i for i in range(n)]
#print(liste)


#liste = [8,4,1,0,-5,6,7]
#tri_insertion(liste)
#assert liste == [-5, 0, 1, 4, 6, 7, 8]


def calcul_temps_tri_insertion(n):
    liste = [n-i for i in range(n)]
    temps1 = time.process_time()
    tri_insertion(liste)
    temps2 = time.process_time()
    return temps2 - temps1



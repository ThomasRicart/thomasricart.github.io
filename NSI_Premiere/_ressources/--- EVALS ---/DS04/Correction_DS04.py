### EXO 1
def exo1(c, chaine):
    compteur = 0
    for lettre in chaine:
        if lettre == c:
            compteur = compteur + 1
    return compteur
assert exo1('v', 'ggvytv6') == 2
assert exo1('r', 'bateau') == 0

### EXO 2
def exo2(n):
    somme = 0
    for i in range(1, n+1):
        somme = somme + i
    return somme
assert exo2(3) == 6
assert exo2(4) == 10

### EXO 3
def exo3(nombre):
    sortie = ''
    for chiffre in nombre:
        if chiffre != '0':
            sortie = sortie + chiffre
    return sortie
assert exo3('328045076') == '3284576'
assert exo3('32876') == '32876'

### EXO 4
L = [3, 7, 9, 4, 8, 0, -5]
print(L[3])
L[4] = -3
L.append(15)
L = L + [15]

### EXO 5
def exo5(n):
    sortie = []
    for i in range(0, n):
        sortie.append(2**i)
    return sortie
assert exo5(5) == [1, 2, 4, 8, 16]

### EXO 6
def exo6(L):
    val_max = L[0]
    for i in range(1, len(L)):
        if L[i] > val_max:
            val_max = L[i]
    return val_max
assert exo6([-6, -7, -1, -9]) == -1

def exo6_bis(L):
    val_max = L[0]
    for elt in L:
        if elt > val_max:
            val_max = elt
    return val_max

### EXO7
def exo7(L, val):
    for valeur in L:
        if valeur == val:
            return True
    return False
assert exo7([1, 8, 3, 6], 3) == True
assert exo7([1, 8, 3, 6], 4) == False

def exo7_v2(L, val):
    est_present = False
    while not est_present and len(L) != 0:
        est_present = L.pop() == val
    return est_present
assert exo7_v2([1, 8, 3, 6], 3) == True
assert exo7_v2([1, 8, 3, 6], 4) == False

### EXO8
def est_premier(n, d = None):
    ''' Un exemple de programmation de la fonction est_premier
    Cette fonction n'était pas demandée à l'évaluation
    On emploie ici une méthode récursive vue en Terminale '''
    if n <= 1:              # Les nombres inférieurs à 2 ne sont pas premiers
        return False
    if d is None:           # Initialisation du diviseur
        d = int(n**0.5)
    if d < 2:               # Si le diviseur devient 1 alors n n'a pas de diviseur autre que lui meme
        return True
    if n % d == 0:          # si n est divisible par d alors il n'est pas premier
        return False
    return est_premier(n, d - 1)    # Récursivité

def exo8(n):
    sortie = []
    i = 1
    while len(sortie) < n:
        if est_premier(i):
            sortie.append(i)
        i += 1
    return sortie
assert exo8(6) == [2,3,5,7,11,13]
assert exo8(10) == [2,3,5,7,11,13,17,19,23,29]
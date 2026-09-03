### CORRECTION DS05
import math

# Exo1
L = [4, 8, 9, 3, -3, 6]
print(L[2])     # question a
L[1] = -1       # question b
L.append(15)    # question c

# Exo2
d = {'Alice':4, 'Bob':6}
print(d['Alice'])   # question a
d['Charlie'] = 7    # question b
for val in d.values():
    print(val)

# Exo3
d = {'Alice':{'Maths':12, 'NSI':15}, 'Bob':{'Maths':15, 'NSI':14}}
print(d['Bob']['NSI'])

# Exo4
def exo4(L):
    val_max = L[0]
    for v in L:
        if v > val_max:
            val_max = v
    return val_max
assert exo4([7,3,4,8,-5,1]) == 8

# Exo5
def exo5(instructions):
    position = 0
    for v in instructions:
        if v == 'A':
            position += 1
        elif v == 'R':
            position -= 1
    return position
assert exo5(['A', 'A', 'R', 'T', 'U', 'A']) == 2

# Exo6
def exo6(dico, cle):
    for k, v in dico.items():
        if cle == k:
            return v
    return False
dico = {'Alice' : 4, 'Bob' : 8}
assert exo6(dico, 'Alice') == 4
assert exo6(dico, 'Charly') == False

# Exo7
def exo7(mot):
    d = {}
    for lettre in mot:
        if lettre in d.keys():
            d[lettre] += 1
        else:
            d[lettre] = 1
    return d
mot = 'abracadabra'
assert exo7(mot) == {'a':5, 'b':2, 'r': 2, 'c':1, 'd': 1}

# Exo8






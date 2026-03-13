# Question 29
def initialiser(n):
    return [False] * n
assert initialiser(5) == [False, False, False, False, False]

# Question 30
def victoire(tab):
    for etat_case in tab:
        if etat_case == False:
            return False
    return True
assert victoire([False, False, False, False, False]) == False
assert victoire([False, True, False, False, False]) == False
assert victoire([True, True, True, True, True]) == True

# Question 31
def indice_premiere_case_occupee(tab):
    for i in range(len(tab)):
        if tab[i] == True:
            return i
    return None
assert indice_premiere_case_occupee([False, False, True, True, False]) == 2
assert indice_premiere_case_occupee([True, True, True, True, True]) == 0
assert indice_premiere_case_occupee([False, False, False, False, False]) == None

# Question 32
def coup_valide(tab, case):
    if case < 0 or case >= len(tab):
        return False
    if case == 0:
        return True
    i_premiere_case_occupee = indice_premiere_case_occupee(tab)
    if i_premiere_case_occupee is None:
        return True
    return case == i_premiere_case_occupee + 1

tab01 = [False, False, True, True, False]
assert coup_valide(tab01, 0) == True    # Première case
assert coup_valide(tab01, 1) == False
assert coup_valide(tab01, 2) == False
assert coup_valide(tab01, 3) == True    # suivant la premiere case non occupée
assert coup_valide(tab01, 4) == False

# Question 33
def changer_case(tab, case):
    if coup_valide(tab, case):
        tab[case] = not(tab[case])
    return tab

assert changer_case([False, False, False], 0) == [True, False, False]
assert changer_case([False, False, False], 1) == [False, True, False]
assert changer_case([False, False, False], 2) == [False, False, True]

# Question 34
def vider(n):
    if n == 1:
        print('Vider case 1')
    elif n > 1:
        vider(n-2)
        print('Vider case', n)
        remplir(n-2)
        vider(n-1)
# Question 36
def remplir(n):
    if n == 1:
        print('Remplir case 1')
    elif n > 1:
        vider(n-2)
        print('Remplir case', n)
        remplir(n-2)
        vider(n-1)

# Question 35 à décommenter
print(vider(3))
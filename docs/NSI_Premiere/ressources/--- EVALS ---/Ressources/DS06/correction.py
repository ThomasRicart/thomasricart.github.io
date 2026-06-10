### DS05 - Les listes ###

# Question 2
A = "gomu"
B = len(A)
A = A + A + "no mi"
b = B > 3

assert type(A) == str
assert type(B) == int
assert type(b) == bool

# Question 3
assert A == "gomugomuno mi"
assert B == 4
assert b == True

# Question 4
def question4():
    for i in range(100,1001):
        if i % 2 == 0:
            print(i)

# Question 5
def question5(une_liste):
    n = len(une_liste)
    indice_max = 0
    valeur_max = une_liste[0]
    for i in range(n):
        if une_liste[i] > valeur_max:
            indice_max = i
            valeur_max = une_liste[i]
    return indice_max

assert question5([1,5,-5,8,-3,0]) == 3

# Question 6
def question6(une_liste):
    nouvelle_liste = []
    for elt in une_liste:
        if elt % 2 != 0 and elt > 0:
            nouvelle_liste.append(elt)
    return nouvelle_liste

assert question6([1,5,-5,8,-3,0]) == [1,5]
## Question 1.1.
# La variable a est de type int
# La variable b est de type str
# L'opérateur + ne permet pas de faire d'opérations entre un type int et str

## Question 1.2.
# La variable a est de type str car la fonctionalité input renvoie un str
# L'opérateur + ne permet pas de faire d'opérations entre un str et un int
# Il faudrait convertir a en int grâce à:
# a = int(input())

## Question 2.1.
def fonction1(a):
    if a > 0:
        reponse = True
    else:
        reponse = False
    return reponse

    # Attention:
        # Un seul return
        # Pas de print
    # Autre façon de coder:
        # return (a>0) qui est déjà un booléen

## Question 2.2.
def fonction2(a,b):
    if a > b:
        plus_grand = a
    else:
        plus_grand = b
    return plus_grand

## Question 2.3.
def fonction3(a,b):
    if (a%2 == b%2):
        meme_parite = True
    else:
        meme_parite = False
    # Autre façon de coder:
        # return a%2 == b%2 qui est déjà un booléen

## Question 3
def fonction4(a,b):
    '''
    : param a et b des entiers strictement positifs avec
    a strictement supérieur à b
        '''
    ### A compléter
    ### Il peut y avoir plusieurs lignes d'assert
    assert type(a) == type(b)
    assert a > b > 0
    ### Partie du programme à ne pas modifier
    return a // b
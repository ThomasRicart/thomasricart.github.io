def recherche_dicho_imperative(tab, val):
    i_deb = 0
    i_fin = len(tab) - 1
    while i_deb < i_fin:
        i_mil = (i_fin + i_deb)//2
        if tab[i_mil] == val:
            return True
        if tab[i_mil] > val:
            i_fin = i_mil - 1
        else:
            i_deb = i_mil + 1
    return False

tab = [2, 3, 4, 6, 7, 8]
print(recherche_dicho_imperative(tab, 4))
print(recherche_dicho_imperative(tab, 5))

def recherche(L, val):
    if L == []:
        return False
    if len(L) == 1:
        return L[0] == val
    return recherche(L[:len(L)//2], val) or recherche(L[len(L)//2:], val)

print(recherche(tab, 4))
print(recherche(tab, 5))
L = [1, 3, 9, 2, 7]


def division(L):
    n = len(L)
    return (L[:n//2], L[n//2:])

def fusion(L1, L2, L = None):
    if L == None:
        L = []
    return fusion_rec(L1, L2, L)
def fusion_rec(L1, L2, L):
    if L1 == [] or L2 == []:
        return L + L1 + L2
    if L1[0] < L2[0]:
        e = L1.pop(0)
    else:
        e = L2.pop(0)
    L = L + [e]
    return fusion_rec(L1, L2, L)

def tri_fusion(L):
    ''' Renvoie la liste L triée '''
    n = len(L)
    if n < 2:
        return L
    else:
        L1, L2 = division(L)
        L1 = tri_fusion(L1)
        L2 = tri_fusion(L2)
        return fusion(L1, L2)


L1 = [1, 4, 6, 15]


L2 = [3, 9, 10]
#print(fusion(L1, L2))
assert fusion(L1, L2) == [1, 3, 4, 6, 9, 10, 15]
L1 = [1, 4, 6, 15]
L2 = [3, 9, 10]
assert division (L1) == ([1, 4], [6, 15])
assert division (L2) == ([3], [9, 10])
assert division ([1]) == ([] , [1])
def maximum(L):
    if len(L) == 1:
        return L[0]
    return max(maximum(L[:len(L)//2]), maximum(L[len(L)//2:]))
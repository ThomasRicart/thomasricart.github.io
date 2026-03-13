from random import *
def maximum(tab):
    if len(tab) == 1:
        return tab[0]
    max_g = maximum(tab[:len(tab)//2])
    max_d = maximum(tab[len(tab)//2:])
    return max(max_g, max_d)

tab = [randint(0, 100) for i in range(10)]

print(tab)
m = maximum(tab)
print(m)


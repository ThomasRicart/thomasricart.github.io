# Créé par picart8, le 29/09/2020 en Python 3.7

import numpy as np
import matplotlib.pyplot as plt

fe=10
y=[10.0, 19.01, 10.31, 9.69, 0.99, 10.0, 19.01, 10.31, 9.69, 0.99, 10.0, 19.01] #tableau des ordonnées
N=len(y)
x=[n for n in range(N)] #tableau des abscisses
t=[n/fe for n in range(N)] #tableau des instants
f=[v*fe/N for v in range(N)]   #tableau des fréquences

sp = np.fft.fft(y)
plt.stem(x[:N//2], abs(sp)[:N//2],basefmt = 'k:',use_line_collection=True)
plt.show()

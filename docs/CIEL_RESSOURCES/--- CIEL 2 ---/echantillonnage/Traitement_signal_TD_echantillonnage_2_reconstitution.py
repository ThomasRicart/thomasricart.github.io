#-------------------------------------------------------------------------------
# Nom_fichier:        Traitement_signal_TD_echantillonnage_2_reconstitution.py
#
# Auteur:      Ph. Picart
# Created:     05/10/2020
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft


########## Déclaration d'une figure ##########
plt.figure()


########## paramètres d'échantillonnage ##########
fe = 10         # fréquence d'échantillonnage
duree=4.0       # durée d'échantillonnage
temps = np.arange(start=0.0, stop=duree, step=1/fe)
N=len(temps)    # nombre d'échantillons
numeros = np.arange(0, N//2)
frequences = np.arange(0, N//2)*1/duree

print(f'f_e = {fe}\nduree = {duree}\nN = {N}' )
print(frequences)

########## signal échantillonné ##########
def signal(t):
    return 10+7*np.sin(2*2*np.pi*t) + 4*np.sin(4*2*np.pi*t)

echantillons = signal(temps)  # tableau des N échantillons

########## Tracé du signal  échantillonné ##########
plt.subplot(221)
plt.plot(temps, echantillons, 'b.')
plt.xlabel('temps')
plt.ylabel('échantillons')
plt.title('SIGNAL ÉCHANTILLONNÉ')
plt.grid(True)


########## Calcul du spectre du signal échantillonné ##########
tfd = fft(echantillons)/N
amplitudes =  np.absolute(tfd)[:N//2]  # tableau des amplitudes jusque N//2
amplitudes[1:]=amplitudes[1:]*2        # le signal est réel donc la TFD est paire, on double l'amplitude des fréquences non-nulles

########## Tracé du spectre original ##########
plt.subplot(222)
#plt.vlines(np.arange(0, fe//2), 0, amplitudes, colors='red')
plt.stem(np.arange(0, N//2), amplitudes, basefmt = 'k:',use_line_collection=True)
plt.xlabel('fréquence')
plt.xticks(np.arange(0, N//2),np.round(frequences,1))
plt.ylabel('amplitude')
plt.title('SPECTRE par TFD')
plt.grid(True)


########## Tracé du signal reconstitué par TFD inverse ##########
signal_tfd_inv=ifft(tfd).real*N

plt.subplot(223)
plt.plot(temps, signal_tfd_inv, 'g.')
plt.xlabel('temps')
plt.ylabel('valeur')
plt.title('SIGNAL RECONSTITUÉ après TFD')
plt.grid(True)



########## Affichage ##########
plt.tight_layout()
plt.show()

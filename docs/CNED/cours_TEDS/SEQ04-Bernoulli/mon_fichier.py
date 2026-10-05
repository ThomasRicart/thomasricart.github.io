from random import *

def victoire(n):
  E, S=0, 0
  while (E<n) and (S<n):
    a=random()
    if a<0.6:
      E=???
    else:
      S=???
  if ???:
    return("Eve a gagné")
  else:
    return("Sarah a gagné")
  
def frequence_victoire(n,m):
  nbre_victoire_eve=???
  for k in range(???):
    E, S=0, 0
    while (E<n) and (S<n):
      a=random()
      if a<0.6:
        E=E+1
      else:
        S=S+1
    if E==n:
      ???
  return(???)
    
print(victoire(???))
print(frequence_victoire(???))
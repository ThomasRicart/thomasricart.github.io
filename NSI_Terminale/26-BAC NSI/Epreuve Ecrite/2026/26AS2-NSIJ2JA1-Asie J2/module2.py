# Table personne
### personne(id_pers, pseudo_pers, date_pers)
### participation(id_partie, id_pers, nb_point)

# Q1: La table participation
# Q2: plusieurs personnes peuvent participer à une même partie.

# Q3
# INSERT INTO personne (id_pers, pseudo_pers, date_pers)
# VALUES (42, 'theorie', '2022-12-14');

# Q4
# SELECT participation.id_partie
# FROM participation
# JOIN personne ON participation.id_pers = personne.id_pers
# WHERE personne.pseudo_per = 'test'

# Q5
# DELETE FROM participation
# WHERE participation.id_pers = 8;
# DELETE FROM personne
# WHERE personne.id_pers = 8;

alphabet = 'aeiouy'

def indice(lettre, ordre):
    for i in range(len(ordre)):
        if lettre == ordre[i]:
            return i
def comparer(mot1, mot2, ordre):
    i = 0
    while i < len(mot1) and i < len(mot2):
        i1 = indice(mot1[i], ordre)
        i2 = indice(mot2[i], ordre)
        if i1 < i2:
            return True
        elif i1 > i2:
            return False
        i += 1
    # On suppose que les deux mots ne peuvent pas être identiques
    return len(mot1) <= len(mot2)

def premiere_diff(mot1, mot2):
    i = 0
    while i < len(mot1) and i < len(mot2) and mot1[i] == mot2[i]:
        i += 1
    return i

def dico_adj(mots):
    adj = {}
    for (mot1, mot2) in mots:
        ident = premiere_diff(mot1, mot2)
        if ident < len(mot1) and ident < len(mot2):
            petite = mot1[ident]
            grande = mot2[ident]
            if petite not in adj:
                adj[petite] = [grande]
            else:
                adj[petite].append(grande)
    return adj

# Q9 dico obtenu:
##{
##  'u': ['a', 'y'],
##  'y': ['i', 'a'],
##  'a': ['i'],
##  'o': ['u'],
##  'e': ['a']
##}

# Q10 Parcours en profondeur (DFS): la fonction s'appelle récursivement
# sur chaque voisin avant de revenir ajouter le sommet courant à tri,
# ce qui caractérise le tri par DFS

# Q11
def trier(mots):
    adj = dico_adj(mots)
    tri = []
    deja_vus = []
    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
    for v in voyelles:
        if v not in deja_vus:
            deja_vus.append(v)
            parcours(adj, v, deja_vus, tri)
    tri.reverse()
    return tri
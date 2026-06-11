def lire_mesures(nom_fichier):
    ''' Ouverture et lecture du fichier texte
    sortie: une liste de dictionnaires contenant les données relevées
    '''
    mesures = []
    with open(nom_fichier, 'r', encoding='utf-8') as f:
        next(f)  # ignorer l’en-tête
        for ligne in f:
            jour, heure, temp = ligne.strip().split(',')
            mesures.append({'jour': jour, 'heure': heure, 'temperature': float(temp)})
    return mesures

def test_lire_mesures():
    mesures = lire_mesures('meteo.txt')
    print(f'Nombre de valeurs mesurées: {len(mesures)}, valeur attendue: ')
    print(f'Première mesure du fichier: {mesures[0]}')
#test_lire_mesures()

def extraire_temperatures(mesures):
    ''' Renvoie une liste de températures dans l'ordre chronologique
    mesures: liste de dictionnaires contenant les mesures
    sortie: liste de températures
    '''
    liste_temperatures = []
    # -------------------------------------------------------
    # Question 1
    # -------------------------------------------------------
    ### A compléter ######################
    for m in mesures:
        liste_temperatures.append(m['temperature'])
    ######################################
    return liste_temperatures

def test_extraire_temperatures():
    mesures = lire_mesures('meteo.txt')
    liste_temps = extraire_temperatures(mesures)
    print(liste_temps)
    print(f'Résultat attendu: \n[14.8, 14.3, 13.9, 13.7, 13.9, 15.2, 17.5, 19.6, 21.8, 23.1, 25.0, 26.2, 27.5, 28.3, 28.8, 27.9, 26.0, 24.2, 21.9, 19.4, 17.1, 15.6, 15.0, 14.4]')
#test_extraire_temperatures()

def detection_pic_chaleur(mesures, seuil):
    ''' Renvoie la liste des tuples (jour, heure) où la température est supérieure à un seuil
    mesures: liste de dictionnaires contenant les relevés
    sortie: une liste de tuples (jour, heure)
    '''
    pics = []
    # -------------------------------------------------------
    # Question 2
    # -------------------------------------------------------
    ### A compléter ######################
    for m in mesures:
        if m['temperature'] > seuil:
            pics.append((m['jour'], m['heure']))
    ######################################
    return pics

def test_detection_pic_chaleur():
    mesures = lire_mesures('meteo.txt')
    seuil = 28
    pics = detection_pic_chaleur(mesures, seuil)
    print(pics)

#test_detection_pic_chaleur()

def moyennes_glissantes(liste):
    """
    Calcule récursivement la moyenne glissante de 3 valeurs consécutives dans la liste.
    """
    # Cas de base : si la liste contient moins de 3 valeurs, on ne peut pas faire de moyenne
    if len(liste) < 3:
        return []

    # Calcul de la moyenne des trois premières valeurs
    moyenne = round((liste[0] + liste[1] + liste[2]) / 3, 2)

    # Appel récursif : on décale la fenêtre d’une position vers la droite
    nouvelle_liste = []
    for i in range(1, len(liste)):
        nouvelle_liste.append(liste[i])
    return [moyenne] + moyennes_glissantes(nouvelle_liste)

def moyennes_glissantes_f(liste):
    """
    Calcule récursivement la moyenne glissante de 3 valeurs consécutives dans la liste.
    """
    # -------------------------------------------------------
    # Question 3
    # -------------------------------------------------------
    ### A modifier ######################
    if len(liste) == 3:
        return []

    moyenne = (liste[0] + liste[1] + liste[2]) / 3

    nouvelle_liste = []
    for i in range(1, 4):
        nouvelle_liste.append(liste[i])
    return [moyenne] + moyennes_glissantes_f(nouvelle_liste)
    ######################################

def test_moyennes_glissantes():
    liste_temps = [14, 18, 22, 20, 15, 13]
    moy_glis = moyennes_glissantes(liste_temps)
    print(f'Listes de moyennes glissantes obtenues: ')
    print(moy_glis)
    print(f'Résultat attendu: ')
    print('[18.0, 20.0, 19.0, 16.0]')

test_moyennes_glissantes()

def trouve_minimum(liste_temps):
    n = len(liste_temps)
    return trouve_minimum_rec(liste_temps, n - 1)
def trouve_minimum_rec(liste_temps, i):
    if i == 0:
        return liste_temps[0]
    mini_reste = trouve_minimum_rec(liste_temps, i - 1)

    if liste_temps[i] < mini_reste:
        return liste_temps[i]
    return mini_reste

L = [3, 4, -1, 7, 0, -6]
print(trouve_minimum(L))

def mini(liste_temps):
    liste_temps_save = liste_temps[:]
    if len(liste_temps_save) == 1:
        return liste_temps_save[0]
    temperature_observee = liste_temps_save.pop()
    temperature_minimale = mini(liste_temps_save)
    if temperature_observee < temperature_minimale:
        return temperature_observee
    return temperature_minimale
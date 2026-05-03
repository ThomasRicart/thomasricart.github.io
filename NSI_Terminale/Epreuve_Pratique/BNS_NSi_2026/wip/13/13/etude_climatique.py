# ///////////////////////////////////////////////////////////////////////////
# FONCTIONS DONNEES
# ///////////////////////////////////////////////////////////////////////////

def recupere_donnees_fichier_csv(nom_fichier):
    """ Fonction qui récupère les données relevées du ballon sonde sans les en-têtes de la 1ère ligne """
    altitudes = []                                  # Initialisation des listes de valeurs relevées
    temperatures = []
    longitudes = []
    latitudes = []
    # Ouverture du fichier csv au format npm.csv en mode "read"
    contenu_fichier = open(nom_fichier, 'r')
    # Supprime la 1ère ligne avec les en-têtes
    contenu_fichier.readline()
    # Parcours des lignes du fichier csv contenant les donnees relevées
    for ligne in contenu_fichier.readlines():
        # rstrip() supprime les \n et espaces en fin de ligne
        ligne = ligne.rstrip()
        # création d'une listeValeurs. split(";") sépare les valeurs grâce au ;
        listeValeurs = ligne.split(";")
        # conversion string en int de l'altitude et insertion dans la liste correspondante
        altitudes.append(int(listeValeurs[0]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        temperatures.append(float(listeValeurs[1]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        longitudes.append(float(listeValeurs[2]))
        # conversion string en float de l'altitude et insertion dans la liste correspondante
        latitudes.append(float(listeValeurs[3]))
    return altitudes, temperatures, longitudes, latitudes


def genere_kml(liste_longitudes, liste_latitudes):
    """ Fonction qui génère un fichier de données géographiques au format standard international KML
        Ce fichier est visionnable ensuite dans différents logiciels
    """
    assert len(liste_longitudes) == len(liste_latitudes), "Les listes doivent etre de meme longueur"
    fichier_kml = open('ballon sonde.kml', 'w')    # Création et ouverture du fichier kml en mode "write"
    entete_fichier = '<?xml version="1.0" encoding="UTF-8"?>\n'
    entete_fichier += '<kml xmlns="http://www.opengis.net/kml/2.2">\n'
    entete_fichier += '<Document>\n'
    entete_fichier += '<name>Trajectoire ballon sonde</name>\n'
    # Ecriture du contenu de la variable entete_fichier dans le fichier kml
    fichier_kml.write(entete_fichier)
    for i in range(len(liste_longitudes)):
        corps_fichier = '<Placemark>\n'
        corps_fichier += f'<name>Point {i}</name>\n'
        corps_fichier += '<Point>\n'
        corps_fichier += f'<coordinates>{liste_longitudes[i]},{liste_latitudes[i]}</coordinates>\n'
        corps_fichier += '</Point>\n'
        corps_fichier += '</Placemark>\n'
        fichier_kml.write(corps_fichier)
    # QUESTION 6
    bas_fichier = '</Document>\n</kml>'
    fichier_kml.write(bas_fichier)
    fichier_kml.close()                         # Fermeture du fichier kml


# ///////////////////////////////////////////////////////////////////////////
# TRAVAIL DEMANDE
# ///////////////////////////////////////////////////////////////////////////

# QUESTION 1
# Compléter ici
donnees = recupere_donnees_fichier_csv("releves_ballon_sonde.csv") # tuple
altitudes = donnees[0]      # list
temperatures = donnees[1]   # list
longitudes = donnees[2]     # list
latitudes = donnees[3]      # list

# version 2
# altitudes, temperatures, longitudes, latitudes = recupere_donnees_fichier_csv("releves_ballon_sonde.csv")


# QUESTION 2
def conversion_K_en_C(liste_temperatures):
    # 1 ligne
    # return [round(t-273.15, 1) for t in liste_temperatures]
    ''' Convertit une liste de temperature de K en °C
    entree: liste d'int
    sortie: list d'int '''
    for i in range(len(liste_temperatures)):
        T_K = liste_temperatures[i]
        T_C = T_K - 273.15
        T_C = round(T_C, 1)
        liste_temperatures[i] = T_C
#conversion_K_en_C(temperatures)
#assert temperatures == [15.0, 13.7, 11.7, 7.9, 3.4, 0.5, -2.3, -17.7, -28.9, -42.5, -48.3, -56.0, -56.2, -56.5, -56.5, -56.0, -56.1, -53.0, -50.1, -48.0]


def conversion_K_en_C(liste_temperatures):
    temp_C = []
    for t in liste_temperatures:
        t_c = t - 273.15
        t_c = round(t_c, 1)
        temp_C.append(t_c)
    return temp_C

temp_celcius = conversion_K_en_C(temperatures)
assert temp_celcius == [15.0, 13.7, 11.7, 7.9, 3.4, 0.5, -2.3, -17.7, -28.9, -42.5, -48.3, -56.0, -56.2, -56.5, -56.5, -56.0, -56.1, -53.0, -50.1, -48.0]


#print(temperatures)
#conversion_K_en_C(temperatures)
#print(temperatures)

# QUESTION 3
def altitude_la_plus_froide(liste_altitudes, liste_temperatures):
    ''' '''
    # Initialisation.
    # temp la plus froide / altitude temp la plus froide
    t_min = liste_temperatures[0]       # float
    alt_min = [liste_altitudes[0]]      # list
    # Itération sur les températures
    for i in range(1, len(liste_temperatures)):
        # si la temp est strictement plus petite que t_min
        if liste_temperatures[i] < t_min:
            # remplacer t_min
            t_min = liste_temperatures[i]
            # créer un nouveau alt_min
            alt_min = [liste_altitudes[i]]
        elif liste_temperatures[i] == t_min:
            # concaténer la nouvelle altitude dans alt_min
            alt_min.append(liste_altitudes[i])
        # sinon: rien
    return (t_min, alt_min)
altitudes = [7000, 10125, 13896, 14211]
temperatures = [-35.2, -52.1, -57.4, -57.4]
print(altitude_la_plus_froide(altitudes,temperatures))
# doit afficher (-57.4, [13896, 14211])
altitudes = [6000, 7250, 11542, 15214, 17300]
temperatures = [-33.7, -45, -53, -58.5, -60.1]
print(altitude_la_plus_froide(altitudes,temperatures))
# doit afficher (-60.1, [17300])
# AUTRES ELEMENTS DE CODE

genere_kml(longitudes, latitudes)
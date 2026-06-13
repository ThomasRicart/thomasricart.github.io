# ------------------------------------
# gestion_eau.py
# Programme de contrôle des réservoirs
# ------------------------------------
from donnees import reservoirs

# Question 1 : écrire la fonction est_en_penurie

def est_en_penurie(reservoirs, nom_reservoir):
    for reservoir in reservoirs:
        if reservoir["nom"] == nom_reservoir:
            taux = reservoir["volume"] / reservoir["capacite"] * 100
            if taux > 20:
                return False
            else:
                return True

# Question 2 : écrire la fonction volume_par_district


def volume_par_district(reservoirs):
    dico = {}
    for reservoir in reservoirs:
        if reservoir["district"] in dico:
            dico[reservoir["district"]] += reservoir["volume"]
        else:
            dico[reservoir["district"]] = reservoir["volume"]
    return dico

# Question 3


def volume_moyen(reservoirs):
    """
    Renvoie le volume moyen d'eau disponible dans les réservoirs.
    """
    assert len(reservoirs) >= 1
    somme_totale = 0
    maxi = 0
    for r in reservoirs:
        if r["capacite"] > maxi:
            maxi = r["capacite"]
        somme_totale += r["volume"]
    moyenne = somme_totale / len(reservoirs)
    assert moyenne <= maxi
    return moyenne

assert volume_moyen([{"capacite":120000, "volume":10000},{"capacite":120000, "volume":10000}]) == 10000

# Question 4


def liste_districts(reservoirs):
    """
    Renvoie la liste des districts présents dans les données.
    """
    liste = []
    for r in reservoirs:
        if (r["district"] not in liste):
            liste.append(r["district"])
    return liste


def reservoirs_par_district(reservoirs):
    """
    Renvoie un dictionnaire associant chaque district à la liste
    des réservoirs qui s’y trouvent.
    """
    liste_rpd = {}
    for r in reservoirs:
        district = r["district"]
        if district not in liste_rpd:
            liste_rpd[district] = []
        liste_rpd[district].append(r)
    return liste_rpd


def districts_vulnerables(reservoirs):
    liste = []
    ref = volume_moyen(reservoirs) * 0.8
    districts = reservoirs_par_district(reservoirs)
    for district in districts:
        moy = volume_moyen(districts[district])
        if moy < ref:
            liste.append(district)
    return liste
    
    
    
    
    

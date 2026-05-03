# ------------------------------------
# gestion_eau.py
# Programme de contrôle des réservoirs
# ------------------------------------
from donnees import reservoirs

# Question 1 : écrire la fonction est_en_penurie
def est_en_penurie(liste_reservoir, reservoir):
    for r in liste_reservoir:
        if r['nom'] == reservoir:
            if r['volume'] / r['capacite'] > 0.2:
                return False
            return True
def test_est_en_penurie():
    for res in reservoirs:
        print(est_en_penurie(reservoirs, res['nom']))

# Question 2 : écrire la fonction volume_par_district
def volume_par_district(liste_reservoirs):
    reponse = {}
    for res in liste_reservoirs:
        if res['district'] in reponse.keys():
            reponse[res['district']] += res['volume']
        else:
            reponse[res['district']] = res['volume']
    return reponse

def test_volume_par_district():
    print(volume_par_district(reservoirs))



# Question 3
def plus_grande_capa(reservoirs):
    capa_max = 0
    for res in reservoirs:
        if res['capacite'] > capa_max:
            capa_max = res['capacite']
    return capa_max

def volume_moyen(reservoirs):
    """
    Renvoie le volume moyen d'eau disponible dans les réservoirs.
    """
    assert len(reservoirs) > 0, 'la liste des réservoirs doit contenir au moins un reservoir'
    capa_max = plus_grande_capa(reservoirs)
    somme_totale = 0
    for r in reservoirs:
        somme_totale += r["volume"]
    moyenne = somme_totale / (len(reservoirs))
    assert moyenne <= capa_max, 'la moyenne doit être inférieure ou égale à la capa_max'
    return moyenne

reservoirs_test =  [
    {"nom": "Nuiavai", "capacite": 100000, "volume": 100, "district": "Tepua"},
    {"nom": "Farepape", "capacite": 120000, "volume": 100, "district": "Fare"}
    ]

# Question 4
def districts_vulnerables(reservoirs, seuil = 0.8):


def taux_remplissage(reservoir, changement=0):
    """
    Renvoie le taux de remplissage du réservoir (en pourcentage),
    en tenant compte d'un changement éventuel du volume.
    Attention : le changement n'est pas effectif, il est hypothétique.
    - changement > 0 : ajout d'eau
    - changement < 0 : retrait d'eau
    - changement = 0 (par défaut) : taux de remplissage réel
    """
    volume_modifie = reservoir["volume"] + changement
    capacite = reservoir["capacite"]

    # On évite de dépasser les limites physiques
    if volume_modifie < 0:
        volume_modifie = 0
    if volume_modifie > capacite:
        volume_modifie = capacite

    return volume_modifie * 100 / capacite


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
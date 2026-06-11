# Données d'émissions en gCO2e par unité
EMISSIONS = {
    'emails_simples': 4,       # par email
    'emails_pj': 19,           # par email avec pièce jointe
    'streaming_sd': 36,        # par heure
    'streaming_hd': 100,       # par heure
    'recherches': 7,           # par recherche
    'stockage_cloud': 10       # par Go par mois
}

# Exemples d'utilisateurs pour les tests
utilisateur1 = {
    'emails_simples': 150,
    'emails_pj': 20,
    'streaming_sd': 10,
    'streaming_hd': 25,
    'recherches': 500,
    'stockage_cloud': 15
}

utilisateur2 = {
    'streaming_hd': 15,
    'emails_simples': 100,
    'recherches': 10
}

utilisateur3 = {
    'emails_simples': 50,
    'emails_pj': 5,
    'streaming_sd': 30,
    'streaming_hd': 5,
    'recherches': 200,
    'stockage_cloud': 5
}

utilisateur4 = {
    'emails_simples': 100,
    'recherches': 50
}

utilisateur5 = {
    'emails_simples': 50,
    'recherches': 100
}

utilisateur6 = {}

#############################################################################
# Écrire le code de la fonction calculer_empreinte de la question 1         #
#############################################################################

def calculer_empreinte(utilisateur):
    es = epj = ssd = shd = r = sc = 0
    if 'emails_simples' in utilisateur:
        es = utilisateur['emails_simples'] * EMISSIONS['emails_simples']
    if 'emails_pj' in utilisateur:
        epj = utilisateur['emails_pj'] * EMISSIONS['emails_pj']
    if 'streaming_sd' in utilisateur:
        ssd = utilisateur['streaming_sd'] * EMISSIONS['streaming_sd']
    if 'streaming_hd' in utilisateur:
        shd = utilisateur['streaming_hd'] * EMISSIONS['streaming_hd']
    if 'recherches' in utilisateur:
        r = utilisateur['recherches'] * EMISSIONS['recherches']
    if 'stockage_cloud' in utilisateur:
        sc = utilisateur['stockage_cloud'] * EMISSIONS['stockage_cloud']
    return es + epj + ssd + shd + r + sc

#############################################################################
# Écrire le code de la fonction classer_par_impact de la question 2         #
#############################################################################

def classer_par_impact(utilisateur):
    dico = {'fort': [], 'moyen': [], 'faible': []}
    for activite in utilisateur:
        e = utilisateur[activite] * EMISSIONS[activite]
        if e >= 1000:
            dico['fort'].append(activite)
        elif e >= 200 and e < 1000:
            dico['moyen'].append(activite)
        else:
            dico['faible'].append(activite)
    return dico

#############################################################################
# Fonction fournie pour la question 3                                       #
#############################################################################

def comparer(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, la différence des
    émissions (émissions de l’utilisateur 2 moins celles de l’utilisateur 1).
    Si une activité est absente chez un utilisateur, on considère que
    son émission vaut 0."""
    differences = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        differences[activite] = emission2 - emission1
    return differences


def test_comparer():
    diff = comparer(utilisateur4, utilisateur5)
    assert diff['emails_simples'] == -200  # (50-100) * 4
    assert diff['recherches'] == 350     # (100-50) * 7
    # Test avec deux zéro
    assert diff['streaming_sd'] == 0 # pas de streaming
    diff = comparer(utilisateur6, utilisateur1)
    # Test avec un zéro pour le premier
    assert diff['streaming_sd'] == 360  # (10 - 0) * 36
    diff = comparer(utilisateur1, utilisateur6)
    # Test avec un zéro pour le deuxième
    assert diff['streaming_sd'] == -360  # (0 - 10) * 36

#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################
def comparer_v2(u1, u2):
    """Compare les émissions de deux utilisateurs pour toutes les activités.
    Renvoie un dictionnaire avec, pour chaque activité, l'écart des émissions
    sous forme de pourcentage, en proportion de la première émission."""
    ecarts = {}
    for activite in EMISSIONS:
        quantite1 = 0
        quantite2 = 0
        if activite in u1:
            quantite1 = u1[activite]
        if activite in u2:
            quantite2 = u2[activite]
        emission1 = quantite1 * EMISSIONS[activite]
        emission2 = quantite2 * EMISSIONS[activite]
        if emission1 != 0:
            ecarts[activite] = (emission2 - emission1)/emission1 * 100
        else:
            ecarts[activite] = None
    return ecarts

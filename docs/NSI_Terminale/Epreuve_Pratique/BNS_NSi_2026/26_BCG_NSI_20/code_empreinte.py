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
    ''' Renvoie l'emprunte carbone totale mensuelle en gCO2e d'un utilisateur
    - utilisateur (dict): les usages d'un utilisateur
    - sortie (int)
    ex: calculer_empreinte(utilisateur1) renvoie la valeur 7490 '''
    empreinte_totale = 0
    for activite, nombre in utilisateur.items():
        empreinte_totale += nombre * EMISSIONS[activite]
    return empreinte_totale

# Test de la fonction calculer_empreinte
def test_calculer_empreinte():
    print(f"L'empreinte de l'utilisateur1 est {calculer_empreinte(utilisateur1)}")
    print(f"Résultat attendu: 7490")
#test_calculer_empreinte()



#############################################################################
# Écrire le code de la fonction classer_par_impact de la question 2         #
#############################################################################
def classer_par_impact(utilisateur):
    ''' renvoie un dictionnaire classant les impacts de chaque activite
    - utilisateur (dict): les usages des utilisateurs
    - sortie (dict)'''
    dict_impact = {'fort': [], 'moyen': [], 'faible': []}
    for activite, nombre in utilisateur.items():
        if nombre * EMISSIONS[activite] >= 1000:
            dict_impact['fort'].append(activite)
        elif nombre * EMISSIONS[activite] >= 200:
            dict_impact['moyen'].append(activite)
        else:
            dict_impact['faible'].append(activite)
    return dict_impact

# test de la fonction classer_par_impact
def test_classer_par_impact():
    print(f"Classement par impact utilisateur1: \n{classer_par_impact(utilisateur1)}")
    print(f"Résultat attendu:")
    print("{'fort': ['streaming_hd', 'recherches'], 'moyen': ['emails_simples', 'emails_pj', 'streaming_sd'], 'faible': ['stockage_cloud']}")
    print(f"Classement par impact utilisateur2: \n{classer_par_impact(utilisateur2)}")
    print(f"Résultat attendu:")
    print("{'fort': ['streaming_hd'], 'moyen': ['emails_simples'], 'faible': ['recherches']}")
test_classer_par_impact()


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
    # Ajouter vos tests ci-dessous avec justifications
    assert diff['stockage_cloud'] == 0 # test activité absente

    diff2 = comparer(utilisateur1, utilisateur2)
    assert diff2['stockage_cloud'] == -150   # test activité absente chez un utilisateur

    diff3 = comparer(utilisateur1, utilisateur1)
    assert diff3['stockage_cloud'] == 0 # usagers identiques

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
        # Gestion du cas de division par 0
        if emission1 == 0:
            if emission2 == 0:
                ecarts[activite] = 0
            else:
                ecarts[activite] = None
        else:
            ecarts[activite] = (emission2 - emission1)/emission1 * 100
    return ecarts


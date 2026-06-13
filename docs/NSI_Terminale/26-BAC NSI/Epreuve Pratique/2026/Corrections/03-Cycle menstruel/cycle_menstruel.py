import calendar

#############################################################################
# Écrire le code de la fonction est_bissextile de la question 1             #
#############################################################################

def est_bissextile(annee):
    return annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)

#############################################################################
# Écrire le code de la fonction determiner_phase de la question 2           #
#############################################################################

def determiner_phase(n):
    assert n >= 1 and n <= 28, "le nombre doit être compris entre 1 et 28"
    
    if n <= 5:
        return 1
    elif n <= 13:
        return 2
    elif n == 14:
        return 3
    else:
        return 4

#############################################################################
# Fonctions fournies pour la question 3                                     #
#############################################################################

def jours_dans_mois(annee, mois):
    """Renvoie le nombre de jours dans un mois donné d'une année donnée.
       Utilise le module calendar pour gérer les années bissextiles."""
    if mois == 2:  # février
        return 29 if calendar.isleap(annee) else 28
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        return 30

def ajouter_jours(date, nb_jours):
    """Ajoute nb_jours à une date donnée et renvoie la nouvelle date.
       La date est représentée par un tuple (jour, mois, année)."""
    jour, mois, annee = date
    jour = jour + nb_jours

    # Ajustement du jour et du mois si dépassement
    while jour > jours_dans_mois(annee, mois):
        jour = jour - jours_dans_mois(annee, mois)
        mois = mois + 1
        if mois > 12:  # passage à l'année suivante
            mois = 1
            annee = annee + 1

    return (jour, mois, annee)

def test_ajouter_jours():
    assert ajouter_jours((7, 9, 2025), 3) == (10, 9, 2025)
    # Test de changement d'année
    assert ajouter_jours((31, 12, 2025), 1) == (1, 1, 2026)
    # Test d'ajout d'une année non bissextile
    assert ajouter_jours((15, 2, 2025), 365) == (15, 2, 2026)
    # Test d'ajout d'une année bissextile
    assert ajouter_jours((15, 2, 2024), 366) == (15, 2, 2025)
    
#############################################################################
# Fonction fournie pour la question 4                                       #
#############################################################################

def calendrier_cycles(date_regles):
    """Renvoie une chaîne de caractère contenant au format iCalendar, l'ensemble
    des dates de début de règles qui se présentent dans les 100 jours suivants 
    `date_regles`, date incluse.

    Hypothèse : cycle régulier de 28 jours. """

    cal_lignes = ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:Règles']

    date_courante = date_regles
    jours_ecoules = 0

    # On ajoute les dates tant que l'on ne dépasse pas 100 jours écoulés
    while jours_ecoules <= 100:
        jour, mois, annee = date_courante  
        cal_lignes.append('BEGIN:VEVENT')
        date = str(annee)+str(mois).zfill(2)+str(jour).zfill(2)
        cal_lignes.append('DTSTART:'+date)
        cal_lignes.append('SUMMARY: Règles')
        cal_lignes.append('END:VEVENT')
        date_courante = ajouter_jours(date_courante, 28)
        jours_ecoules += 28 

    cal_lignes.append('END:VCALENDAR')

    # La méthode join va renvoyer ici une unique chaîne contenant toutes les
    # chaînes de la liste séparées par des sauts de lignes.
    return '\n'.join(cal_lignes)

def test_calendrier_cycles():
    '''Crée un calendrier et le charge avec le module ics pour vérifier sa
    validité.

    Nécessite que le module ics soit présent sur la machine (pip install ics).
    '''
    #from ics import Calendar
    c = calendrier_cycles( (12,3,2026) )
    print(c)
    #cal = Calendar(c)
    #print(cal.events)
    
test_calendrier_cycles()
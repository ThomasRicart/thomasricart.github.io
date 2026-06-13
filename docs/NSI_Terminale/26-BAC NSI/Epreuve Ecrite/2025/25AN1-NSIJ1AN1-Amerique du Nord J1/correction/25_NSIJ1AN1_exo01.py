# Créé par thoma, le 22/05/2025 en Python 3.7

class Noeud:
    def __init__(self, question, sioui, sinon):
        self.question = question
        self.sioui = sioui
        self.sinon = sinon
    def est_resultat(self):
        """Retourne False car un noeud n'est pas un résultat"""
        return False
    def nb_vegetaux(self):
        """Retourne le nombre total de végétaux identifiables à partir de ce noeud"""
        return self.sioui.nb_vegetaux() + self.sinon.nb_vegetaux()
    def liste_questions(self):
        """Retourne la liste de toutes les questions accessibles à partir de ce noeud"""
        return [self.question] + self.sioui.liste_questions() + self.sinon.liste_questions()


class Feuille_resultat:
    def __init__(self, vegetaux):
        self.vegetaux = vegetaux
    def est_resultat(self):
        """Retourne True car une feuille est un résultat"""
        return True
    def nb_vegetaux(self):
        """Retourne le nombre de végétaux dans cette feuille"""
        return len(self.vegetaux)
    def liste_questions(self):
        """Retourne une liste vide car une feuille ne contient pas de questions"""
        return []

F1 = Feuille_resultat([])
F2 = Feuille_resultat(['Sorbier'])
F3 = Feuille_resultat(['Robinier', 'Noyer'])
F4 = Feuille_resultat([])

N1 = Noeud('Bord denté ?', F2, F3 )
N2 = Noeud('Alternées ?', N1, F4)
N3 = Noeud('Simples ?', F1, N2)

arbre_2 = N3

folia_sorbier = {
    'Simples ?': False,
    'Alternées ?': True,
    'Bord denté ?': True
    }

folia_tilleul = {
    'En forme d\'ovale ?': False,
    'Disposées de façon alternée ?': True,
    'Bord denté ?': True
    }


def est_bien_renseigne(dico_vegetal, arbre):
    """
    Vérifie si toutes les questions présentes dans l'arbre sont des clés du dictionnaire

    Args:
        dico_vegetal: dictionnaire contenant les caractéristiques des folia d'un végétal
        arbre: arbre de décision (objet Noeud ou Feuille_resultat)

    Returns:
        True si toutes les questions de l'arbre sont des clés du dictionnaire, False sinon
    """
    questions_arbre = arbre.liste_questions()   # list
    for q in questions_arbre:
        if q not in dico_vegetal.keys():
            return False
    return True

def identifier_vegetaux(arbre, dico_vegetal):
    """
    Identifie les végétaux correspondant aux caractéristiques données

    Args:
        dico_vegetal: dictionnaire contenant les caractéristiques des folia d'un végétal
        arbre: arbre de décision (objet Noeud ou Feuille_resultat)

    Returns:
        Liste des noms des végétaux identifiés (peut être vide)
    """
    # Si on est arrivé à une feuille, retourner les végétaux
    if arbre.est_resultat():
        return arbre.vegetaux
    # Si on est sur un noeud, suivre la branche correspondant à la réponse
    question = arbre.question
    reponse = dico_vegetal[question]
    if reponse:
        return identifier_vegetaux(arbre.sioui, dico_vegetal)
    else:
        return identifier_vegetaux(arbre.sinon, dico_vegetal)








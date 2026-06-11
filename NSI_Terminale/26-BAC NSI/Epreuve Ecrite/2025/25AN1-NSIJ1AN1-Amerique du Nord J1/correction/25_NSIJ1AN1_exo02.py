class Colis:
    def __init__(self, id, poids, adresse):
        self.id = id
        self.poids = poids
        self.adresse = adresse
        self.etat = 'préparé'

    # Question 1 : Méthode pour changer l'état à 'transit'
    def passer_transit(self):
        """Change l'état du colis à 'transit'"""
        self.etat = 'transit'


# Question 2 : Fonction ajouter_colis modifiée avec vérification du poids
def ajouter_colis(liste, colis):
    """Ajoute un colis à la liste si son poids est <= 25kg, sinon affiche un message d'erreur"""
    if colis.poids <= 25:
        liste.append(colis)
    else:
        print("Dépassement du poids maximal autorisé")

# Question 3 : Fonction pour compter le nombre de colis dans une liste
def nb_colis(liste):
    """Renvoie le nombre de colis dans la liste"""
    return len(liste)


# Question 4 : Fonction pour calculer le poids total
def poids_total(liste):
    """Renvoie le poids total de tous les colis dans la liste"""
    total = 0
    for c in liste:
        total = total + c.poids
    return total

# Question 5 : Fonction pour filtrer les colis par état
def liste_colis_etat(liste, statut):
    """Renvoie une nouvelle liste contenant les colis ayant l'état spécifié"""
    nouvelle_liste = []
    for colis in liste:
        if colis.etat == statut:
            nouvelle_liste.append(colis)
    return nouvelle_liste

# Question 6 : Identification de l’algorithme de tri
# La fonction tri_decroissant utilise le TRI PAR SÉLECTION
# Complexité dans le pire des cas : O(n²)

def tri_decroissant(liste):
    """Trie les colis par poids décroissant en utilisant le tri par sélection"""
    n = len(liste)
    for i in range(n - 1):
        min_pos = i
        for j in range(i + 1, n):
            if liste[j].poids > liste[min_pos].poids:
                min_pos = j
        # Échange des éléments
        temp = liste[i]
        liste[i] = liste[min_pos]
        liste[min_pos] = temp
    return liste

# Question 7 : Autre algorithme de tri
# On pourrait utiliser le TRI FUSION (MERGE SORT)
# Complexité dans le pire des cas : O(n log n) – meilleure que le tri par sélection

# Questions 8 & 9 : Algorithme récursif glouton de chargement
def chargement_glouton(liste, rang, capacite):
    """
    Algorithme glouton récursif pour charger des colis

    Arguments :
        liste : liste de colis triée par poids décroissant
        rang : indice courant entre 0 et len(liste)
        capacite : capacité restante du camion en kg

    Renvoie :
        liste de colis à charger en utilisant un algorithme glouton
    """
    # Cas de base : si tous les colis ont été examinés
    if rang == len(liste):
        return []
    # Si le colis courant rentre dans la capacité restante
    elif liste[rang].poids <= capacite:
        return [liste[rang]] + chargement_glouton(liste, rang + 1, capacite - liste[rang].poids)
    # Sinon, on le saute
    else:
        return chargement_glouton(liste, rang + 1, capacite)



# Question 9 : Explication de RecursionError
# Une RecursionError se produit lorsque la profondeur maximale de récursion est atteinte.
# Cela arrive lorsque la fonction récursive s'appelle trop de fois sans atteindre un cas de base,
# typiquement avec des listes très longues.

# Question 10 : Version itérative de l’algorithme glouton
def chargement_glouton2(liste, capacite):
    """
    Algorithme glouton itératif pour charger des colis

    Arguments :
        liste : liste de colis triée par poids décroissant
        capacite : capacité du camion en kg

    Renvoie :
        liste des colis à charger pour maximiser le poids total sans dépasser la capacité
    """
    colis_a_charger = []
    poids_actuel = 0

    for colis in liste:
        if poids_actuel + colis.poids <= capacite:
            colis_a_charger.append(colis)
            poids_actuel += colis.poids

    return colis_a_charger

colisA = Colis('AC12', 5.0, '20 rue de la paix 57000 Metz')
colisB = Colis('AF34', 10.25, '32 rue du centre 57000 Metz')

liste_colis = []
ajouter_colis(liste_colis, colisA)
ajouter_colis(liste_colis, colisB)


# Tests des fonctions
if __name__ == "__main__":
    # Création de colis de test
    colis1 = Colis('C001', 15.5, 'Adresse 1')
    colis2 = Colis('C002', 8.2, 'Adresse 2')
    colis3 = Colis('C003', 30.0, 'Adresse 3')  # Plus de 25kg
    colis4 = Colis('C004', 12.1, 'Adresse 4')

    # Test des fonctions
    liste_colis = []

    print("=== Test de ajouter_colis ===")
    ajouter_colis(liste_colis, colis1)
    ajouter_colis(liste_colis, colis2)
    ajouter_colis(liste_colis, colis3)  # Doit afficher une erreur
    ajouter_colis(liste_colis, colis4)

    print(f"Nombre de colis : {nb_colis(liste_colis)}")
    print(f"Poids total : {poids_total(liste_colis)} kg")

    # Changement d'état de certains colis
    colis1.passer_transit()
    colis2.etat = 'livré'

    print(f"Colis en 'transit' : {len(liste_colis_etat(liste_colis, 'transit'))}")
    print(f"Colis 'préparés' : {len(liste_colis_etat(liste_colis, 'préparé'))}")

    # Test du tri et du chargement
    print("\n=== Test du chargement glouton ===")
    tri_decroissant(liste_colis)
    print("Colis triés par poids décroissant :")
    for colis in liste_colis:
        print(f"  {colis.id} : {colis.poids} kg")

    # Test des algorithmes gloutons
    capacite_camion = 25
    packages_recursive = chargement_glouton(liste_colis, 0, capacite_camion)
    packages_iterative = chargement_glouton2(liste_colis, capacite_camion)

    print(f"\nRésultat glouton récursif : {[p.id for p in packages_recursive]}")
    print(f"Résultat glouton itératif : {[p.id for p in packages_iterative]}")
    print(f"Poids total chargé : {sum(p.poids for p in packages_iterative)} kg")
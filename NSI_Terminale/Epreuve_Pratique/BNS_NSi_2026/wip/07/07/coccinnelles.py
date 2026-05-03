import random


class Coccinelle:
    def __init__(self, sexe, age, niv_nutrition):
        self.age = age
        self.esperance_de_vie = random.randint(200, 350)
        self.sexe = sexe
        self.niv_nutrition = niv_nutrition

    def chasser(self, nb_proies, nb_coccinelles):
        ''' Méthode prenant en paramètre:
            - 1 coccinelle de type Coccinelle
            - le nombre de proies (type int)
            - le nombre de coccinelles restant (type int)
        Renvoie le nombre de proies restantes après que la coccinelle ait chassé
        '''
        # Cas où il n'y a plus de coccinelles -> le nombre de proies n'a pas changé
        # sortie de la méthode
        if nb_coccinelles == 0:
            return nb_proies

        # Calcul de la moyenne donnant le nb de proies par coccinelles
        proies_par_cocci = nb_proies / nb_coccinelles

        # Structure if/elif/else qui scinde en 3 cas et choisit au hasard un nombre de
        # proies consommées.
        # plus il y a de coccinelles, plus le nombre de proies consommées par une
        # coccinelle est élevé (décidé en random)
        if proies_par_cocci > 20:
            consomme = random.randint(12, 20)
        elif proies_par_cocci > 10:
            consomme = random.randint(8, 15)
        else:
            consomme = random.randint(3, 8)

        # La coccinelle ne peut pas consommer plus de proies qu'il en existe.
        consomme = min(consomme, nb_proies)

        # si la coccinelle a consommé plus de 10 proies, son niveau de nutrition augmente
        # sinon il diminue avec un minimum de 0
        if consomme >= 10:
            self.niv_nutrition += 1
        else:
            self.niv_nutrition = max(0, self.niv_nutrition - 1)

        # On renvoie le nombre de proies restantes
        return nb_proies - consomme

    def reproduction(self):
        """
        Une femelle avec un niveau de nutrition >= 2 engendre exactement
        deux descendants : un mâle et une femelle.
        """
        descendants = []
        # Ajout question 4
        if self.sexe == "femelle" and self.niv_nutrition >= 2 and self.age >= 20:
            descendants.append(Coccinelle("male", 0, 0))
            descendants.append(Coccinelle("femelle", 0, 0))
            self.niv_nutrition = 0

        return descendants

    def a_survecu(self):
        """
        Met à jour l'âge de la coccinelle et indique si elle est encore en vie.
        """
        # AJOUT Question 4
        if self.niv_nutrition == 0:
            if random.randint(1, 3) == 3:
                return False
        self.age = self.age + 1
        return self.age < self.esperance_de_vie

    def __repr__(self):
        return f"Coccinelle {self.sexe}, âge: {self.age}/{self.esperance_de_vie}, niv_nutrition: {self.niv_nutrition}"


def evolution(population, nb_proies):
    """
    Simule une journée dans l'écosystème :
    - chasse des coccinelles
    - reproduction
    - vieillissement et mortalité
    - croissance des pucerons

    population est une liste d'instances de la classe Coccinelle
    nb_proies est un entier indiquant le nombre de proies

    Cette fonction renvoie un couple (population_suivante, nouveau_nb_proies) indiquant
    la nouvelle population à la fin de la journée et le nombre de proies.
    """
    population_suivante = []
    nouveau_nes = []
    nb_coccinelles = len(population)

    for coccinelle in population:
        nb_proies = coccinelle.chasser(nb_proies, nb_coccinelles)

        if coccinelle.a_survecu():
            population_suivante.append(coccinelle)

        nouveau_nes += coccinelle.reproduction()

    # Croissance naturelle des pucerons (augmentation de 20% par jour)
    nb_proies = int(nb_proies * 1.2)

    # Ajout des nouveau-nés en fin de journée
    population_suivante += nouveau_nes

    return population_suivante, nb_proies


#############################################################################
# Écrire ci-dessous le code pour les questions de l'énoncé                  #
#############################################################################

def init_pop():
    c1 = Coccinelle("femelle", 10, 2)
    c2 = Coccinelle("femelle", 10, 2)
    c3 = Coccinelle("male", 10, 2)
    return [c1, c2, c3]

def test_evolution():
    liste_pop = init_pop()
    print(len(liste_pop))
    nb_pucerons = 200
    for i in range(1, 6):
        liste_pop, nb_pucerons = evolution(liste_pop, nb_pucerons)
        print(f'Jour: {i}, Coccinelles: {len(liste_pop)}, Pucerons: {nb_pucerons}')

def simulation_simple(population, nb_proies):
    for k in range(1, 31):
        population, nb_proies = evolution(population, nb_proies)
        resultat = (len(population), nb_proies, k)
        if len(population) == 0:
            print('Plus de coccinelles')
            return resultat
        elif nb_proies == 0:
            print('Plus de pucerons')
            return resultat
    return resultat

def test_simulation_simple():
    population = init_pop()
    nb_proies = 1000
    return simulation_simple(population, nb_proies)

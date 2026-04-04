import csv

with open('starwars.csv', newline='', encoding='utf-8') as csvfile:
    dataset = list(csv.DictReader(csvfile, delimiter=','))

# Question 1:
# Combien y a t -il de personnage dans la base?


# Question 2:
# Quelle est l'espèce de Dooku?

# Question 3:
# Quelle est l'age de Anakin? (birth_year)

# Question 4:
# Quelle est la planete (homeworld) de Jabba the Hutt?

# Question 5:
# Créer une liste contenant les noms des personnages d'espèce 'human'
# Afficher le nombre d'éléments de cette liste

# Question 6: Créer une liste contenant les différentes planetes (homeworld) présentes dans la base (élminer les doublons)
# Afficher le nombre d'éléments de cette liste

# Question 7: Créer une liste contenant les 20 personnages les plus grands (height)

# Question 8: Créer une liste contenant les 20 personnages les plus agés (birth_year)

# Question 9: Créer une liste contenant les 10 personnages humains originaires de Tatooine les plus grands.

# Question 10: Trier la liste des personnages selon leur espèce (par ordre alphabétique croissant) puis par taille (ordre décroissant)



for p in dataset:
    if p['name'] == 'Greedo':
        print(p['mass'])
import csv

def get_data(fichier):
    with open(fichier, newline='', encoding='utf-8') as dataset:
        data = list(csv.DictReader(dataset, delimiter=','))
    return data

dataset = get_data('starwars.csv')
print(dataset[0])
print(type(dataset[0]))

import csv

# 1. Chargement des deux bases de données
with open('starwars.csv', newline='', encoding='utf-8') as f1:
    table_perso = list(csv.DictReader(f1, delimiter=';'))

with open('vaisseaux.csv', newline='', encoding='utf-8') as f2:
    table_vaisseaux = list(csv.DictReader(f2, delimiter=','))

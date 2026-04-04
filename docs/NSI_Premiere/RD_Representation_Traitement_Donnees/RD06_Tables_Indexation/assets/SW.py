import csv

with open('starwars.csv', newline='', encoding='utf-8') as csvfile:
    dataset = list(csv.DictReader(csvfile, delimiter=','))

perso = dict(dataset[0])


for p in dataset:
    if p['name'] == 'Greedo':
        print(p['mass'])
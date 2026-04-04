import csv

with open('countries.csv', newline='', encoding='utf-8') as csvfile:
    pays = list(csv.DictReader(csvfile, delimiter=';'))


def cle_population(p):
    return int(p['population'].replace(",", ""))

def cle_continent(p):
    return p['continent']

pays.sort(key=cle_population, reverse=True)  # tri par population
pays.sort(key=cle_continent)                 # tri par continent
resultat = []
for p in pays[:5] : # extraction
	resultat.append((p['country'], p['population'], p['continent']))

for p in resultat : # affichage
    print(p)
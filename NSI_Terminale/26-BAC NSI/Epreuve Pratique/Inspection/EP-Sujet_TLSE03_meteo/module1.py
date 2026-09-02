



def somme_valeurs_liste(liste):
    # Ecrire
    if liste == []:
        return 0
    return liste[0] + somme_valeurs_liste(liste[1:])

def test_somme_valeurs_liste():
    liste = [1, 2, 3, 4, 5, 6]
    somme = somme_valeurs_liste(liste)
    print(f'La somme des valeurs de la liste {liste} est: {somme}')
test_somme_valeurs_liste()

def moyenne(liste):
    return somme_valeurs_liste(liste) / len(liste)


def extremums_temps(liste_temps):
    # compléter
    temp_min = liste_temps[0]
    temp_max = liste_temps[1]


def resume_meteo(liste_temp):
    moyenne = sum(liste_temp) / len(liste_temp)
    print("=== RÉSUMÉ MÉTÉO ===")
    print("Température moyenne :", round(moyenne, 1))
    # Erreur d’origine : prenait la dernière valeur au lieu du max
    print("Température max :", max(liste_temp))
    print("Température min :", min(liste_temp))
    print("Amplitude thermique :", round(max(liste_temp) - min(liste_temp), 1))
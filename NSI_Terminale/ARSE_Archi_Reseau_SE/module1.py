def crypte_xor(donnees, cle):
    """
    Fonction symétrique :
    - Si 'donnees' est une chaîne, elle renvoie une liste d'entiers (chiffrement).
    - Si 'donnees' est une liste d'entiers, elle renvoie une chaîne (déchiffrement).
    """
    resultat = []
    for i in range(len(donnees)):
        # On récupère la valeur numérique de la donnée (caractère ou entier)
        valeur_data = ord(donnees[i]) if isinstance(donnees[i], str) else donnees[i]

        # On récupère le code de la clé (en bouclant avec le modulo)
        valeur_cle = ord(cle[i % len(cle)])

        # Application du XOR
        transformation = valeur_data ^ valeur_cle

        # On stocke le résultat
        if isinstance(donnees[i], str):
            resultat.append(transformation)
        else:
            resultat.append(chr(transformation))

    return resultat if isinstance(donnees[0], str) else "".join(resultat)

### 1. Test de réversibilité
### C'est le test fondamental du chiffrement symétrique.
### Si on applique la fonction deux fois avec la même clé,
### on doit retrouver exactement le message de départ.
# Configuration
message_original = "NSI TERMINALE"
cle = "BAC"

# Étape A : Chiffrement
message_chiffre = crypte_xor(message_original, cle)
print(f"Chiffré : {message_chiffre}")
# On obtient une liste d'entiers

# Étape B : Déchiffrement
message_retrouve = crypte_xor(message_chiffre, cle)
print(f"Retrouvé : {message_retrouve}")

# Assertion (Test automatique)
assert message_retrouve == message_original

### 2. Test de la Clé de Longueur Différente
### Clé plus courte que le message : La clé doit "boucler".
### Clé plus longue que le message : Seul le début de la clé doit être utilisé.
# Test clé courte
msg_long = "INFORMATIQUE"
cle_courte = "X" # La clé est répétée pour chaque lettre
assert crypte_xor(crypte_xor(msg_long, cle_courte), cle_courte) == msg_long

# Test clé longue
cle_longue = "C'EST_UNE_CLE_TRES_LONGUE_POUR_UN_PETIT_MOT"
msg_court = "OUI"
assert crypte_xor(crypte_xor(msg_court, cle_longue), cle_longue) == msg_court

### 3. Test des Caractères Spéciaux et Espaces
### Le chiffrement XOR s'appuie sur les valeurs numériques (Unicode/ASCII).
### Il est crucial de vérifier que les espaces et la ponctuation
### ne font pas planter la fonction.
# Test avec caractères variés
test_special = "Hello World! @ 2026"
cle_speciale = "Key#1"

chiffre = crypte_xor(test_special, cle_speciale)
assert crypte_xor(chiffre, cle_speciale) == test_special
print("Test caractères spéciaux : Réussi")

### 4. Test de Sécurité (Propriété de Kerckhoffs)
### si vous changez un seul caractère dans la clé,
### le déchiffrement doit totalement échouer et produire un "bruit" illisible.
message = "SECRET"
bonne_cle = "PROFS"
mauvaise_cle = "PROFT" # Une seule lettre de différence

code = crypte_xor(message, bonne_cle)
tentative = crypte_xor(code, mauvaise_cle)

print(f"Déchiffrement avec mauvaise clé : {tentative}")
assert tentative != message
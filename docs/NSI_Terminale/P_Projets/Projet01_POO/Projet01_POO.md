# TP : Concevoir un système orienté objet avec classes interdépendantes

## 1. Objectifs du TP

Après avoir manipulé des classes simples et interdépendantes (comme `Point`, `Segment` et `Vecteur`), vous allez maintenant **concevoir et implémenter votre propre mini-projet en Programmation Orientée Objet (POO)**.

Ce travail vous permettra de valider les compétences suivantes :
* **Définir des classes** avec des attributs d'instance et des méthodes.
* **Modéliser des relations d'association et de composition** (une classe qui contient ou utilise des objets d'une autre classe).
* **Encapsuler** la logique métier au bon endroit (chaque classe est responsable de ses données).
* **Créer un script de démonstration** pour valider le bon fonctionnement de votre système via des instanciations et des jeux de tests.

Pour ce mini-projet vous pouvez utiliser n'importe quel IDE. Le site `codeshare.io` est également une bonne option pour tester votre code en ligne.
---

## 2. Consignes et Cahier des Charges

Vous devez imaginer, concevoir et programmer un mini-projet respectant impérativement la structure suivante :

### Contraintes obligatoires :
1. **Au moins 3 classes distinctes** interconnectées.
2. **Une relation d'inclusion / d'agrégation** : au moins une classe doit contenir une liste (ou un dictionnaire) d'objets issus d'une autre classe.
3. **Des méthodes d'interaction** :
   * Une méthode permettant d'ajouter ou d'associer un objet à un autre.
   * Une méthode d'affichage claire ou une implémentation de `__repr__` / `__str__`.
   * Des méthodes de calcul, de recherche ou d'action globales (ex. calculer une moyenne, effectuer un combat, calculer un prix total, etc.).
4. **Un script principal de test** : à la fin de votre fichier, vous devez écrire un scénario complet montrant la création des objets, leur assemblage et l'appel des différentes méthodes.

---

## 3. Pistes d'inspiration et Exemples de Contextes

Vous êtes libres de choisir le thème qui vous intéresse. Voici quelques idées pour vous guider :

### 🎴 Option A : Jeu de cartes ou de plateau
* **Classe 1 : `Carte`** (attributs : `valeur`, `couleur`).
* **Classe 2 : `Main` ou `Paquet`** (attributs : liste de `Carte`, méthodes : `ajouter_carte()`, `tirer_carte()`, `valeur_totale()`).
* **Classe 3 : `Joueur`** (attributs : `nom`, `solde`, objet `Main`, méthodes : `jouer_tour()`, `miser()`).

### 🗡️ Option B : Jeu de Rôle (JDR) / RPG
* **Classe 1 : `Equipement` ou `Arme`** (attributs : `nom`, `degats`, `durabilite`).
* **Classe 2 : `Personnage`** (attributs : `nom`, `points_de_vie`, liste d'objets `Equipement`, méthodes : `equiper()`, `attaquer()`).
* **Classe 3 : `Equipe` ou `Guilde`** (attributs : liste de `Personnage`, méthodes : `ajouter_membre()`, `points_de_vie_totaux()`, `soigner_tout_le_monde()`).

### 📚 Option C : Gestion de Bibliothèque / Médiathèque
* **Classe 1 : `Livre`** (attributs : `titre`, `auteur`, `isbn`, `est_emprunte`).
* **Classe 2 : `Abonne`** (attributs : `nom`, `num_adherent`, liste des objets `Livre` empruntés, méthodes : `emprunter()`, `rendre()`).
* **Classe 3 : `Bibliotheque`** (attributs : liste des `Livre`, liste des `Abonne`, méthodes : `rechercher_par_auteur()`, `gerer_retard()`).

### 🏫 Option D : Gestion Scolaire (Base Élèves / Classe)
* **Classe 1 : `Note`** (attributs : `valeur`, `coefficient`, `matiere`).
* **Classe 2 : `Eleve`** (attributs : `nom`, `prenom`, liste d'objets `Note`, méthodes : `ajouter_note()`, `calculer_moyenne()`).
* **Classe 3 : `Classe`** (attributs : `nom_classe`, liste d'objets `Eleve`, méthodes : `ajouter_eleve()`, `moyenne_generale_classe()`, `major_de_promo()`).

---

## 4. Livrables attendus

Vous rendrez un fichier Python `mini_projet_poo.py` structuré de la manière suivante :

1. **Diagramme texte ou court paragraphe d'introduction** (en commentaire au début du fichier) expliquant le domaine choisi et l'interaction entre vos 3 classes.
2. **Définition des 3 classes** avec des docstrings d'en-tête pour chaque méthode.
3. **Zone de démonstration** (`if __name__ == "__main__":`) contenant un exemple concret d'utilisation étape par étape avec des `print()` explicites.

---

## 5. Grille d'évaluation indicative

| Critère | Description | Points |
| :--- | :--- | :---: |
| **Structure POO** | Les 3 classes sont bien définies et bien encapsulées. | / 4 |
| **Interdépendance** | La manipulation d'objets imbriqués/associés est fonctionnelle. | / 5 |
| **Qualité des méthodes** | Les méthodes réalisent des calculs ou actions pertinents. | / 5 |
| **Script de test** | Le scénario final est complet et montre toutes les fonctionnalités. | / 3 |
| **Lisibilité & Code** | Noms de variables explicites, présence de docstrings, indentation. | / 3 |
# WEB01 — Langages du Web (1) : HTML5

🎯Objectifs et Compétences

### Capacités attendues 

| Capacités visées | Description                                                                     |
| ---------------- | ------------------------------------------------------------------------------- |
| Analyser         | Examiner le code HTML d'une page comprenant des composants graphiques           |
| Distinguer       | Séparer la description (HTML) du comportement (JavaScript) et de la forme (CSS) |
|Structurer        | Créer l'ossature d'une interface répondant à un besoin (Mini-projet Domotique)                                                                                |

## 1. Phase d'Exploration : "L'envers du décor"

* **Activité** : Ouvrir une page Web simple (par exemple [`http://www.wikipedia.fr`](http://www.wikipedia.fr)) et utiliser l'outil `Inspecteur d'élément` (`F12` ou  `Clic droit > Inspecter`).

* **Notion** : Comprendre que le navigateur interprète un fichier texte balisé pour générer un rendu visuel. Le langage utilisé (`HTML`) n'est pas **WYSIWYG**. (*What you see is what you get*)
* **Repère historique** 

![image alt](./images/web_historique.png)

* **Anatomie d'une balise**: La mise en page est effectuée grâce à des balises. Il existe des balises doubles (`<p>...</p>`) ou orphelines (`<img>`)

* **Attributs**: Les balises peuvent être personnalisées (ex: `<a href = "..."> ou <img src = "...">`)

## 2. Structure en arbre (DOM)

Le **HTML** structure les données de manière hiérarchique. On parle de **DOM** (Document Object Model). Chaque balise ouverte à l'intérieur d'une autre devient sont "enfant".

* **Structure minimale**: 
    * `html`: la racine qui englobe tout,
    * `head`:  les métadonnées (titre de l'onglet, encodage UTF-8),
    * `body`: le contenu visible par l'utilisateur
* **Regles d'indentation:** Pour rendre le code lisible, on décale (touche Tab) chaque balise enfant par rapport à sa balise parente.

``` html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ma Première Page</title>
</head>
<body>

    <h1>Bienvenue sur mon site</h1>

    <p>Ceci est un paragraphe d'introduction pour présenter le contenu de la page.</p>

    <p>Voici une liste de mes liens préférés :</p>
    <ul>
        <li><a href="https://www.google.com">Moteur de recherche Google</a></li>
        <li><a href="https://wikipedia.org">Encyclopédie Wikipédia</a></li>
        <li>Un élément de liste sans lien pour l'exemple</li>
    </ul>

</body>
</html>
```

![image alt](./images/dom_tree2.webp)

## 3. Les différentes balises

| Balise    | Nom complet   | Rôle principal                                      |
|:--------- |:------------- |:--------------------------------------------------- |
| `<html>`  | Document HTML | Racine du document (englobe tout le code).          |
| `<head>`  | En-tête       | Contient les infos techniques (métadonnées, titre). |
| `<meta>`  | Métadonnées   | Définit l'encodage (UTF-8).                         |
| `<title>` | Titre         | Texte affiché dans l'onglet du navigateur.          |
| `<body>`  | Corps         | Contient tout le contenu visible (texte, images).   |
| `<h1>`    | Titre H1      | Le titre principal de la page.                      |
| `<p>`     | Paragraphe    | Bloc de texte standard.                             |
| `<a>`     | Lien          | Crée un lien hypertexte (attribut href).            |
| `<ul>`    | Liste         | Définit une liste à puces (non ordonnée).           |
| `<li>`    | Élément       | Un item spécifique dans une liste.                  |
| `<ol>`    | Liste         | Définit une liste numérotée                      |



## 4. Mini projet: 

Vous allez construire la structure de contrôle d'une pièce (Salon, Garage ou Cuisine).

Vous devez réaliser l'ossature (le squelette) de l'interface de contrôle d'une pièce (Salon, Cuisine ou Garage).

**Cahier des charges :**

* Structure : Respecter les balises obligatoires  `html`, `head` et `body`.

* Contenu :

    * Un titre principal `<h1>` (ex: "Contrôle du Salon").

    * Deux sous-sections `<h2>` (ex: "Éclairage" et "Chauffage").

    * Une liste à puces `<ul>` et `<li>` affichant 3 capteurs (Ex: `Température : 21°C`).

* Interactions : Insérer deux balises `<button>` : `Allumer` et `Éteindre`.

* Médias : Une image `<img>` avec l'attribut `alt` (obligatoire pour l'accessibilité des malvoyants).

* Lien : Un lien `<a>` vers un site météo.

<a href = "./html/WEB01-dashboard.html"> Le rendu devrait ressembler à quelque chose comme cela.</a>

**Zoom sur la balise `<button>`**

Dans cette séance, la balise `<button>` sert de composant graphique d'interaction.

* Ce qu'elle fait aujourd'hui : Elle affiche un élément cliquable sur l'interface.

* Ce qu'elle fera plus tard : Dans les séances suivantes, nous lui associerons un événement JavaScript pour qu'elle puisse réellement piloter un objet.

 ✅ **Liste de contrôle du projet**

☐ **Le document commence par `<!DOCTYPE html>`.**

☐ **Mon code est bien indenté (décalé pour être lisible).**

☐ **Toutes mes balises ouvertes sont refermées.**

☐ **L'attribut `alt` est présent sur mon image.**

☐ **Les boutons s'affichent correctement dans le navigateur.**

☐ **Validation W3C. le <a href = "https://validator.w3.org/">W3C Validator</a> permet de valider la synthaxe du code**

☐ **Défi (Optionnel): ajouter une balise `<input type="range">` pour simuler un variateur de lumière.**



## 5. Synthèse

* Le **HTML5** permet de structurer les données de manière hiérarchique (structure en arbre).

* on sépare le **fond** (HTML) de la **forme** (CSS) et du **comportement** (JS).

* Les **balises** :

    * Doubles : `<p>Texte</p>` (ouvrent et ferment).

    * Orphelines : `<img>` ou `<br>` (autoférmentes).

* Les **attributs** : Ils complètent les balises (ex: `href` pour un lien, `src` pour une image).

* La balise `<button>` : C'est un composant graphique d'interaction. En HTML, on définit son apparence ; son action réelle sera codée plus tard en JavaScript.
<!-- ===================== ÉNONCÉ : DÉBUT ===================== -->

# <span style="color:red">SYNTHÈSE POO — Le navigateur web</span> : énoncé

**Exercice (20 points)** — Cet exercice porte sur la programmation orientée objet et la structure de pile.

Un navigateur web mémorise les pages visitées pour permettre à l'utilisateur de revenir en arrière (bouton « Précédent ») puis d'avancer à nouveau (bouton « Suivant »). On modélise ces mécanismes en programmation orientée objet.

---

## Partie 1 — Les classes `Page` et `Historique` (10 points)

### 1.1 La classe `Page`

Une page web est caractérisée par son **adresse** (`url`, une chaîne de caractères) et par son **titre** (`titre`, une chaîne de caractères).

**Question 1** (1 pt) — Écrire le constructeur `__init__(self, url, titre)` de la classe `Page`.

**Question 2** (0,5 pt) — Écrire les instructions qui créent :

- la variable `p1`, page de titre `"Python"` et d'adresse `"https://fr.wikipedia.org/wiki/Python"` ;
- la variable `p2`, page de titre `"Documentation"` et d'adresse `"https://docs.python.org/3/"`.

**Question 3** (1 pt) — Écrire la méthode `__repr__(self)` qui renvoie le titre de la page. Donner ce qu'affichent `print(p1)` et `print(p2)`.

**Question 4** (1,5 pt) — Le **nom de domaine** d'une page est la partie de son adresse située entre `//` et le `/` suivant (ou la fin de l'adresse). Par exemple, le domaine de `"https://fr.wikipedia.org/wiki/Python"` est `"fr.wikipedia.org"`.

On rappelle que `chaine.split("/")` renvoie la liste des morceaux de `chaine` séparés par le caractère `/` :

```python
>>> "https://docs.python.org/3/".split("/")
['https:', '', 'docs.python.org', '3', '']
```

Écrire la méthode `domaine(self)` de la classe `Page`. Donner la valeur renvoyée par `p2.domaine()`.

### 1.2 La classe `Historique`

Un historique est une **pile** de pages. Il est représenté par la classe `Historique` qui possède un seul attribut, `pages`, une liste Python. Le **sommet** de la pile est le **dernier élément** de la liste.

L'interface de la classe `Historique` est la suivante :

- `Historique()` : crée et renvoie un historique vide ;
- `est_vide(self)` : renvoie `True` si l'historique ne contient aucune page, `False` sinon ;
- `empiler(self, page)` : place `page` au sommet de l'historique ;
- `depiler(self)` : retire et renvoie la page située au sommet (l'historique ne doit pas être vide) ;
- `sommet(self)` : renvoie la page située au sommet, sans la retirer (l'historique ne doit pas être vide).

**Question 5** (1 pt) — Écrire le constructeur `__init__(self)` de la classe `Historique`.

**Question 6** (2 pts) — Écrire les méthodes `est_vide`, `empiler`, `depiler` et `sommet` de la classe `Historique`.

**Question 7** (0,5 pt) — On exécute les instructions suivantes :

```python
h = Historique()
h.empiler(p1)
h.empiler(p2)
x = h.depiler()
```

Donner la valeur de `x`, puis le contenu de la liste `h.pages`.

**Question 8** (1 pt) — Pourquoi la structure de **pile** est-elle adaptée pour mémoriser les pages précédemment visitées ? Une file conviendrait-elle ?

**Question 9** (1,5 pt)

- a) Que se passe-t-il si on exécute `Historique().depiler()` ? Comment un programmeur peut-il éviter ce problème ?
- b) Dans un programme extérieur à la classe, pourquoi vaut-il mieux écrire `h.depiler()` plutôt que `h.pages.pop()` ?

---

## Partie 2 — Application : le navigateur (10 points)

Un navigateur est modélisé par la classe `Navigateur`, dont les attributs sont :

- `courante` : la page actuellement affichée (`None` tant qu'aucune page n'a été visitée) ;
- `precedentes` : un `Historique` contenant les pages visitées avant la page courante (la dernière page quittée est au sommet) ;
- `suivantes` : un `Historique` contenant les pages « devant » la page courante, c'est-à-dire celles que l'on vient de quitter en reculant (la plus proche est au sommet).

Il possède les méthodes suivantes :

- `visiter(self, page)` : si une page courante existe, elle est empilée dans `precedentes` ; `page` devient la page courante ; l'historique `suivantes` est **vidé** (on repart sur un nouveau parcours) ;
- `reculer(self)` : si `precedentes` n'est pas vide, la page courante est empilée dans `suivantes`, puis la page au sommet de `precedentes` est dépilée et devient la page courante ; sinon, rien ne se passe ;
- `avancer(self)` : même principe que `reculer` en échangeant les rôles de `precedentes` et de `suivantes`.

**Squelette fourni :**

```python
class Navigateur:
    def __init__(self):
        """Crée un navigateur sans page affichée, avec des historiques vides."""
        ...

    def visiter(self, page):
        """Ouvre une nouvelle page : l'ancienne page courante est mémorisée
        et les pages suivantes sont oubliées."""
        ...

    def reculer(self):
        """Revient à la page précédente ; ne fait rien s'il n'y en a pas."""
        ...

    def avancer(self):
        """Revient à la page suivante ; ne fait rien s'il n'y en a pas."""
        ...

    def retour_accueil(self):
        """Revient à la toute première page visitée."""
        ...
```

**Question 10** (1 pt) — Écrire le constructeur `__init__(self)` de la classe `Navigateur`.

**Question 11** (1,5 pt) — Écrire la méthode `visiter(self, page)`.

**Question 12** (1,5 pt) — Écrire la méthode `reculer(self)`.

**Question 13** (1 pt) — Écrire la méthode `avancer(self)`.

**Question 14** (2 pts) — On considère les pages suivantes :

```python
moteur = Page("https://www.moteur.fr/", "Moteur")
python = Page("https://fr.wikipedia.org/wiki/Python", "Python")
pile = Page("https://fr.wikipedia.org/wiki/Pile_(informatique)", "Pile")
docs = Page("https://docs.python.org/3/", "Docs")
```

On exécute successivement les instructions du tableau ci-dessous. Recopier et compléter ce tableau en donnant, après chaque instruction, la page courante et le contenu des deux historiques (écrits **du fond vers le sommet**).

| Instruction | `courante` | `precedentes` | `suivantes` |
|---|:---:|:---:|:---:|
| `nav = Navigateur()` | None | [ ] | [ ] |
| `nav.visiter(moteur)` | Moteur | [ ] | [ ] |
| `nav.visiter(python)` | ... | ... | ... |
| `nav.visiter(pile)` | ... | ... | ... |
| `nav.reculer()` | ... | ... | ... |
| `nav.reculer()` | ... | ... | ... |
| `nav.avancer()` | ... | ... | ... |
| `nav.visiter(docs)` | ... | ... | ... |
| `nav.avancer()` | ... | ... | ... |
| `nav.reculer()` | ... | ... | ... |

**Question 15** (1 pt) — Écrire la méthode `retour_accueil(self)` qui ramène le navigateur à la première page visitée, en utilisant la méthode `reculer`. Donner l'état du navigateur (page courante, `precedentes`, `suivantes`) si on appelle `nav.retour_accueil()` à la fin de la simulation de la question 14.

**Question 16** (2 pts) — On ajoute à la classe `Historique` une méthode `titres(self)` qui renvoie la liste des titres des pages de l'historique, **du sommet vers le fond**, en laissant l'historique **inchangé** à la fin de l'appel. On n'utilisera que les méthodes `est_vide`, `empiler`, `depiler` et `sommet` (pas d'accès direct à `self.pages`), et un historique auxiliaire.

- a) Écrire la méthode `titres`.
- b) Donner la valeur renvoyée par `nav.precedentes.titres()` juste après l'instruction `nav.visiter(pile)` de la question 14, puis le contenu de `nav.precedentes` après cet appel.

<!-- ===================== ÉNONCÉ : FIN ===================== -->

---
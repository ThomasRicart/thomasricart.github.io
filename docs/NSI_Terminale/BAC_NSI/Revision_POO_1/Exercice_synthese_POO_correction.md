<!-- ===================== CORRIGÉ : DÉBUT ===================== -->

# <span style="color:red">SYNTHÈSE POO — Le navigateur web</span> : corrigé

## Partie 1 — Les classes `Page` et `Historique`

### 1.1 La classe `Page`

**Question 1**

```python
class Page:
    def __init__(self, url, titre):
        """Crée une page web d'adresse url et de titre donnés."""
        self.url = url
        self.titre = titre
```

**Question 2**

```python
p1 = Page("https://fr.wikipedia.org/wiki/Python", "Python")
p2 = Page("https://docs.python.org/3/", "Documentation")
```

**Question 3**

```python
    def __repr__(self):
        """Renvoie le titre de la page."""
        return self.titre
```

`print(p1)` affiche `Python` et `print(p2)` affiche `Documentation`. La fonction `print` utilise la méthode `__repr__` : sans elle, on verrait l'adresse mémoire de l'objet (`<__main__.Page object at 0x...>`).

**Question 4**

```python
    def domaine(self):
        """Renvoie le nom de domaine de la page, par exemple 'fr.wikipedia.org'
        pour 'https://fr.wikipedia.org/wiki/Python'."""
        return self.url.split("/")[2]
```

Pour `"https://docs.python.org/3/"`, `split("/")` donne `['https:', '', 'docs.python.org', '3', '']`. L'élément d'indice 2 est le domaine : `p2.domaine()` renvoie `'docs.python.org'`.

### 1.2 La classe `Historique`

**Question 5**

```python
class Historique:
    def __init__(self):
        """Crée un historique (pile de pages) vide."""
        self.pages = []     # le sommet de la pile est le dernier élément
```

**Question 6**

```python
    def est_vide(self):
        """Renvoie True si l'historique ne contient aucune page, False sinon."""
        return self.pages == []

    def empiler(self, page):
        """Place la page au sommet de l'historique."""
        self.pages.append(page)

    def depiler(self):
        """Retire et renvoie la page au sommet (l'historique ne doit pas être vide)."""
        return self.pages.pop()

    def sommet(self):
        """Renvoie la page au sommet, sans la retirer (l'historique ne doit pas être vide)."""
        return self.pages[-1]
```

**Remarque.** Le sommet est placé **à la fin** de la liste, car `append` et `pop()` sont des opérations en coût constant. Avec le sommet au début de la liste, il faudrait utiliser `insert(0, ...)` et `pop(0)`, qui décalent tous les éléments (coût proportionnel à la taille).

**Question 7**

`x` vaut la page `p2` (qui s'affiche `Documentation`), car c'est la dernière page empilée. Ensuite `h.pages` contient `[Python]`, c'est-à-dire `[p1]`.

**Question 8**

Le bouton « Précédent » doit ramener à la page visitée **le plus récemment** avant la page actuelle : c'est le principe du dernier entré, premier sorti (LIFO), donc une **pile**. Une file (FIFO) ramènerait à la page la plus **ancienne**, ce qui ne correspond pas au comportement attendu.

**Question 9**

- a) Dépiler une pile vide déclenche une erreur : `IndexError: pop from empty list`. Le programmeur doit tester `not h.est_vide()` avant d'appeler `h.depiler()` (c'est la **précondition** de la méthode).
- b) Utiliser l'interface (`depiler`) plutôt que l'attribut `pages` permet de **cacher l'implémentation** : on peut changer la représentation interne de la pile (par exemple mettre le sommet au début de la liste, ou utiliser une autre structure) sans modifier les programmes qui utilisent la classe. Cela évite aussi qu'un programme extérieur casse la logique de pile en modifiant la liste directement.

---

## Partie 2 — Application : le navigateur

**Question 10**

```python
class Navigateur:
    def __init__(self):
        """Crée un navigateur sans page affichée, avec des historiques vides."""
        self.courante = None
        self.precedentes = Historique()
        self.suivantes = Historique()
```

**Question 11**

```python
    def visiter(self, page):
        """Ouvre une nouvelle page : l'ancienne page courante est mémorisée
        et les pages suivantes sont oubliées."""
        if self.courante is not None:
            self.precedentes.empiler(self.courante)
        self.courante = page
        self.suivantes = Historique()      # nouvel historique vide : on oublie les pages suivantes
```

Le test `self.courante is not None` évite d'empiler `None` lors de la toute première visite.

**Question 12**

```python
    def reculer(self):
        """Revient à la page précédente ; ne fait rien s'il n'y en a pas."""
        if not self.precedentes.est_vide():
            self.suivantes.empiler(self.courante)
            self.courante = self.precedentes.depiler()
```

**Question 13**

```python
    def avancer(self):
        """Revient à la page suivante ; ne fait rien s'il n'y en a pas."""
        if not self.suivantes.est_vide():
            self.precedentes.empiler(self.courante)
            self.courante = self.suivantes.depiler()
```

**Question 14**

| Instruction | `courante` | `precedentes` | `suivantes` |
|---|:---:|:---:|:---:|
| `nav = Navigateur()` | None | [ ] | [ ] |
| `nav.visiter(moteur)` | Moteur | [ ] | [ ] |
| `nav.visiter(python)` | Python | [Moteur] | [ ] |
| `nav.visiter(pile)` | Pile | [Moteur, Python] | [ ] |
| `nav.reculer()` | Python | [Moteur] | [Pile] |
| `nav.reculer()` | Moteur | [ ] | [Pile, Python] |
| `nav.avancer()` | Python | [Moteur] | [Pile] |
| `nav.visiter(docs)` | Docs | [Moteur, Python] | [ ] |
| `nav.avancer()` | Docs | [Moteur, Python] | [ ] |
| `nav.reculer()` | Python | [Moteur] | [Docs] |

Points d'attention :

- À l'instruction `nav.visiter(docs)`, la page `Pile` est **oubliée** : l'historique `suivantes` est vidé.
- L'instruction `nav.avancer()` qui suit n'a **aucun effet**, car `suivantes` est vide.

**Question 15**

```python
    def retour_accueil(self):
        """Revient à la toute première page visitée."""
        while not self.precedentes.est_vide():
            self.reculer()
```

À la fin de la simulation (page courante `Python`, `precedentes` = [Moteur], `suivantes` = [Docs]), un seul appel à `reculer` suffit : le navigateur est dans l'état suivant.

| `courante` | `precedentes` | `suivantes` |
|:---:|:---:|:---:|
| Moteur | [ ] | [Docs, Python] |

**Question 16**

a)

```python
    def titres(self):
        """Renvoie la liste des titres des pages de l'historique, du sommet vers le fond,
        en laissant l'historique inchangé."""
        resultat = []
        auxiliaire = Historique()
        while not self.est_vide():
            page = self.depiler()
            resultat.append(page.titre)
            auxiliaire.empiler(page)         # on met la page de côté
        while not auxiliaire.est_vide():
            self.empiler(auxiliaire.depiler())   # on remet les pages dans leur ordre d'origine
        return resultat
```

La première boucle vide l'historique en inversant l'ordre des pages dans `auxiliaire` ; la seconde boucle inverse à nouveau cet ordre en les remettant : l'historique retrouve exactement son état initial.

b) Après `nav.visiter(pile)`, `nav.precedentes` contient `[Moteur, Python]` (du fond au sommet). Donc :

- `nav.precedentes.titres()` renvoie `['Python', 'Moteur']` (du sommet vers le fond) ;
- `nav.precedentes` contient toujours `[Moteur, Python]` après l'appel.

### Pour tester sur machine (facultatif)

```python
moteur = Page("https://www.moteur.fr/", "Moteur")
python = Page("https://fr.wikipedia.org/wiki/Python", "Python")
pile = Page("https://fr.wikipedia.org/wiki/Pile_(informatique)", "Pile")
docs = Page("https://docs.python.org/3/", "Docs")

nav = Navigateur()
nav.visiter(moteur)
nav.visiter(python)
nav.visiter(pile)
assert nav.precedentes.titres() == ["Python", "Moteur"]
assert nav.precedentes.pages == [moteur, python]      # l'historique est inchangé
nav.reculer()
nav.reculer()
nav.avancer()
nav.visiter(docs)
nav.avancer()
nav.reculer()
assert nav.courante is python
assert nav.precedentes.pages == [moteur]
assert nav.suivantes.pages == [docs]
nav.retour_accueil()
assert nav.courante is moteur
assert nav.precedentes.pages == []
assert nav.suivantes.pages == [docs, python]
print("tous les tests passent")
```

### Erreurs fréquentes à surveiller

- Oublier de **vider `suivantes`** dans `visiter` : on pourrait alors « avancer » vers une page d'un ancien parcours.
- Oublier d'empiler la page courante dans l'**autre** pile lors d'un `reculer` ou d'un `avancer` : la page courante est alors perdue.
- Dépiler sans tester `est_vide()` (erreur `IndexError`), ou empiler `None` lors de la première visite.
- Dans `titres`, ne pas remettre les pages dans l'historique, ou les remettre dans l'ordre inverse.
- Accéder directement à `self.precedentes.pages` depuis la classe `Navigateur` au lieu d'utiliser les méthodes de l'interface.

<!-- ===================== CORRIGÉ : FIN ===================== -->
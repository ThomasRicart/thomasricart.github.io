from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Table, TableStyle, HRFlowable,
                                 PageBreak, Preformatted)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT

OUTPUT = r"D:\--- LYCEE ---\ENSEIGNEMENT_G\docs\NSI_Terminale\26-BAC NSI\Epreuve Ecrite\2026\26CE1-NSIJ1G11-Centre Etranger J1\correction_NSI_bac_2026_G11_new.pdf"

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

# ── Styles ─────────────────────────────────────────────────────────────────
title_style = ParagraphStyle('MainTitle', parent=styles['Title'],
    fontSize=16, spaceAfter=4, textColor=colors.HexColor('#1a237e'))

exo_style = ParagraphStyle('Exo', parent=styles['Heading1'],
    fontSize=13, spaceAfter=4, spaceBefore=14,
    textColor=colors.white,
    backColor=colors.HexColor('#1a237e'),
    borderPad=5)

partie_style = ParagraphStyle('Partie', parent=styles['Heading2'],
    fontSize=11, spaceAfter=3, spaceBefore=10,
    textColor=colors.HexColor('#1a237e'))

q_style = ParagraphStyle('Question', parent=styles['Heading3'],
    fontSize=10, spaceAfter=3, spaceBefore=8,
    textColor=colors.HexColor('#1565c0'))

body = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=10, spaceAfter=4, leading=14)

italic_body = ParagraphStyle('ItalicBody', parent=styles['Normal'],
    fontSize=10, spaceAfter=4, leading=14, fontName='Helvetica-Oblique')

code_style = ParagraphStyle('Code', parent=styles['Normal'],
    fontSize=9, fontName='Courier',
    backColor=colors.HexColor('#f5f5f5'),
    borderColor=colors.HexColor('#aaaaaa'),
    borderWidth=0.8,
    borderPad=7,
    spaceAfter=6, spaceBefore=4,
    leading=13)

note_style = ParagraphStyle('Note', parent=styles['Normal'],
    fontSize=9, textColor=colors.HexColor('#b71c1c'),
    leftIndent=12, spaceAfter=4, leading=13)

bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'],
    fontSize=10, spaceAfter=3, leading=14, leftIndent=20)

sub_bullet_style = ParagraphStyle('SubBullet', parent=styles['Normal'],
    fontSize=10, spaceAfter=3, leading=14, leftIndent=40)

# ── Helpers ────────────────────────────────────────────────────────────────
def code(text):
    """Bloc de code avec indentation et encadré, via Preformatted."""
    return Preformatted(text, code_style)

def q(num, text):
    return Paragraph(f"<b>Question {num}.</b>&nbsp;&nbsp;{text}", q_style)

def bull(text):
    return Paragraph(f"• &nbsp;{text}", bullet_style)

def subbull(text):
    return Paragraph(f"– &nbsp;{text}", sub_bullet_style)

def table_style_base(t):
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1565c0')),
        ('TEXTCOLOR',  (0, 0), (-1, 0), colors.white),
        ('FONTSIZE',   (0, 0), (-1, -1), 9),
        ('GRID',       (0, 0), (-1, -1), 0.5, colors.grey),
        ('ALIGN',      (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN',     (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTNAME',   (0, 1), (-1, -1), 'Helvetica'),
    ]))
    return t

# ══════════════════════════════════════════════════════════════════════════
story = []

# ── Titre ──────────────────────────────────────────────────────────────────
story.append(Paragraph("Correction — Baccalauréat NSI 2026", title_style))
story.append(Paragraph("Sujet 26-NSIJ1G11",
    ParagraphStyle('sub', parent=styles['Normal'],
        fontSize=11, textColor=colors.grey, spaceAfter=4)))
story.append(HRFlowable(width="100%", thickness=1.5,
    color=colors.HexColor('#1a237e'), spaceAfter=12))

# ══════════════════════════════════════════════════════════════════════════
# EXERCICE 1
# ══════════════════════════════════════════════════════════════════════════
story.append(Paragraph("Exercice 1 — Algorithmes de tri et arbre binaire de recherche  (6 points)", exo_style))
story.append(Spacer(1, 6))

# ── Partie A ───────────────────────────────────────────────────────────────
story.append(Paragraph("Partie A : Dictionnaire et tri", partie_style))

story.append(q("1", "Calcul du score d'Alex"))
story.append(Paragraph("Formules de calcul :", body))
story.append(bull("100 m : (20 − 13,0) × 10 = <b>70 points</b>"))
story.append(bull("Saut en longueur : 5,2 × 20 = <b>104 points</b>"))
story.append(bull("Lancer de poids : 9,0 × 10 = <b>90 points</b>"))
story.append(bull("1500 m : (500 − 310,0) × 1 = <b>190 points</b>"))
story.append(Paragraph("<b>Score total d'Alex = 70 + 104 + 90 + 190 = 454 points</b>", body))

story.append(q("2", "Compléter la fonction <b>nb_points</b> (lignes 6, 8, 10, 11)"))
story.append(code(
"def nb_points(epreuve, valeur):\n"
"    points = 0\n"
"    if epreuve == '100m':\n"
"        points = (20 - valeur) * 10\n"
"    elif epreuve == 'longueur':       # ligne 6\n"
"        points = valeur * 20\n"
"    elif epreuve == 'poids':          # ligne 8\n"
"        points = valeur * 10\n"
"    elif epreuve == '1500m':          # ligne 10\n"
"        points = (500 - valeur) * 1\n"
"    return points                     # ligne 11"
))

story.append(q("3", "Compléter la fonction <b>score</b> (lignes 3, 5, 6)"))
story.append(code(
"def score(athlete):\n"
"    total = 0\n"
"    performances = athlete['performances']          # ligne 3\n"
"    for epreuve in performances:\n"
"        valeur = performances[epreuve]              # ligne 5\n"
"        total += nb_points(epreuve, valeur)         # ligne 6\n"
"    athlete['score'] = total"
))

story.append(q("4", "Compléter la ligne 6 de la fonction <b>classer</b>"))
story.append(code(
"def classer(l):\n"
"    n = len(l)\n"
"    for i in range(n):\n"
"        max_index = i\n"
"        for j in range(i + 1, n):\n"
"            if l[j]['score'] > l[max_index]['score']:    # ligne 6\n"
"                max_index = j\n"
"        temp = l[i]\n"
"        l[i] = l[max_index]\n"
"        l[max_index] = temp"
))

story.append(q("5", "Type de tri effectué par <b>classer</b>"))
story.append(Paragraph(
    "Il s'agit d'un <b>tri par sélection</b>. À chaque itération de la boucle externe, "
    "on recherche le maximum parmi les éléments restants et on le place à la bonne position.", body))

story.append(q("6", "Coût de la fonction <b>classer</b>"))
story.append(Paragraph(
    "Pour une liste de taille n, la boucle externe s'exécute n fois et la boucle interne "
    "effectue respectivement n−1, n−2, …, 1 comparaisons.", body))
story.append(Paragraph(
    "Nombre total de comparaisons = (n−1) + (n−2) + … + 1 = <b>n(n−1)/2</b>", body))
story.append(Paragraph(
    "Le coût est donc <b>O(n²)</b> (quadratique), quelle que soit la configuration initiale.", body))

# ── Partie B ───────────────────────────────────────────────────────────────
story.append(Paragraph("Partie B : Arbre binaire de recherche", partie_style))

story.append(q("7", "Créer l'objet <b>alex</b>"))
story.append(code(
"alex = Athlete('Alex', 13.0, 5.2, 9.0, 310.0)"
))

story.append(q("8", "Écrire la méthode <b>calculer_score</b>"))
story.append(code(
"def calculer_score(self):\n"
"    points_100m    = (20 - self.m100)    * 10\n"
"    points_longueur = self.longueur      * 20\n"
"    points_poids    = self.poids         * 10\n"
"    points_1500m   = (500 - self.m1500) * 1\n"
"    return points_100m + points_longueur + points_poids + points_1500m"
))

story.append(q("9", "Dessiner l'arbre obtenu après insertion des six athlètes"))
story.append(Paragraph("Ordre d'insertion et scores : Martin(354), Lena(351), Rayan(350), Yanis(355), Ninon(351), Ana(356)", body))
story.append(Paragraph("Construction pas à pas :", body))
story.append(bull("Insertion Martin(354) → racine"))
story.append(bull("Insertion Lena(351) → 351 < 354 → gauche de Martin"))
story.append(bull("Insertion Rayan(350) → 350 < 354 → gauche ; 350 < 351 → gauche de Lena"))
story.append(bull("Insertion Yanis(355) → 355 >= 354 → droite de Martin"))
story.append(bull("Insertion Ninon(351) → 351 < 354 → gauche ; 351 >= 351 → droite de Lena"))
story.append(bull("Insertion Ana(356) → 356 >= 354 → droite ; 356 >= 355 → droite de Yanis"))
story.append(Spacer(1, 4))

# Arbre sous forme de tableau texte
arbre_data = [
    ['', '', 'Martin (354)', '', ''],
    ['Lena (351)', '', '', '', 'Yanis (355)'],
    ['Rayan (350)', 'Ninon (351)', '', '', 'Ana (356)'],
]
t_arbre = Table(arbre_data, colWidths=[3.3*cm]*5)
t_arbre.setStyle(TableStyle([
    ('ALIGN',    (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',   (0,0), (-1,-1), 'MIDDLE'),
    ('FONTSIZE', (0,0), (-1,-1), 9),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('BACKGROUND', (2,0), (2,0), colors.HexColor('#bbdefb')),
    ('BACKGROUND', (0,1), (0,1), colors.HexColor('#c8e6c9')),
    ('BACKGROUND', (4,1), (4,1), colors.HexColor('#c8e6c9')),
    ('BACKGROUND', (0,2), (0,2), colors.HexColor('#fff9c4')),
    ('BACKGROUND', (1,2), (1,2), colors.HexColor('#fff9c4')),
    ('BACKGROUND', (4,2), (4,2), colors.HexColor('#fff9c4')),
    ('BOX', (2,0),(2,0), 0.8, colors.black),
    ('BOX', (0,1),(0,1), 0.8, colors.black),
    ('BOX', (4,1),(4,1), 0.8, colors.black),
    ('BOX', (0,2),(0,2), 0.8, colors.black),
    ('BOX', (1,2),(1,2), 0.8, colors.black),
    ('BOX', (4,2),(4,2), 0.8, colors.black),
]))
story.append(t_arbre)
story.append(Paragraph(
    "Structure : Martin est la racine. Lena est son fils gauche (Rayan à sa gauche, "
    "Ninon à sa droite). Yanis est le fils droit de Martin (Ana à sa droite).", note_style))

story.append(q("10", "Compléter la méthode <b>inserer</b>"))
story.append(code(
"def inserer(self, athlete):\n"
"    if athlete.score < self.valeur.score:\n"
"        if self.gauche == None:           # ligne 9\n"
"            self.gauche = Noeud(athlete)\n"
"        else:\n"
"            self.gauche.inserer(athlete)  # ligne 12\n"
"    else:\n"
"        if self.droite == None:           # ligne 14\n"
"            self.droite = Noeud(athlete)\n"
"        else:\n"
"            self.droite.inserer(athlete)  # ligne 17"
))

story.append(q("11", "Type de parcours de la méthode <b>classer</b>"))
story.append(Paragraph(
    "Il s'agit d'un <b>parcours infixe (in-order)</b> mais exploré dans l'ordre "
    "<b>droite → racine → gauche</b> (ordre infixe inversé).", body))
story.append(Paragraph(
    "La méthode visite d'abord le sous-arbre droit (scores plus grands), puis ajoute "
    "le nœud courant, puis visite le sous-arbre gauche (scores plus petits). "
    "Cela produit une liste triée du score le plus grand au plus petit, ce qui correspond "
    "au classement décroissant souhaité.", body))

story.append(q("12", "Avantages et inconvénients des deux approches"))
t12_data = [
    ['Approche', 'Avantage', 'Inconvénient'],
    ['Dictionnaires + tri',
     'Simple à implémenter et comprendre. \n Tri facile à adapter.',
     'Tri en O(n²) : lent pour de grandes listes. \n Le tri recrée tout le classement à \n chaque ajout.'],
    ['Arbre binaire de recherche\n (POO)',
     "Insertion et classement efficaces : \n O(log n) en moyenne. Le classement \n est automatique à l'insertion.",
     "Plus complexe à implémenter. \n Peut dégénérer en O(n) si l'arbre \n est déséquilibré."],
]
t12 = Table(t12_data, colWidths=[4*cm, 5.5*cm, 6.5*cm])
t12.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1565c0')),
    ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
    ('FONTSIZE',   (0,0), (-1,-1), 9),
    ('GRID',       (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN',      (0,0), (-1,-1), 'LEFT'),
    ('VALIGN',     (0,0), (-1,-1), 'TOP'),
    ('FONTNAME',   (0,0), (-1,0), 'Helvetica-Bold'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f5f5f5')]),
]))
story.append(t12)

# ══════════════════════════════════════════════════════════════════════════
# EXERCICE 2
# ══════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("Exercice 2 — Chiffrement de Polybe  (6 points)", exo_style))
story.append(Spacer(1, 6))

# Grille de référence
story.append(Paragraph("Grille de référence (exercice) :", body))
grille_ref = [
    ['', '1', '2', '3', '4', '5', '6'],
    ['1', 'Q', '7', 'A', 'X', '2', 'J'],
    ['2', '9', 'E', 'H', '0', 'R', 'M'],
    ['3', 'L', 'Z', '4', 'W', 'D', 'O'],
    ['4', '6', 'V', 'N', 'B', '8', 'K'],
    ['5', 'P', 'Y', '1', 'S', 'T', 'F'],
    ['6', 'G', 'C', '3', 'I', 'U', '5'],
]
tg = Table(grille_ref, colWidths=[1.1*cm]*7, rowHeights=[0.7*cm]*7)
tg.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#455a64')),
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#455a64')),
    ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
    ('TEXTCOLOR',  (0,0), (0,-1), colors.white),
    ('GRID',       (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
    ('FONTSIZE',   (0,0), (-1,-1), 9),
    ('FONTNAME',   (0,0), (-1,-1), 'Helvetica-Bold'),
]))
story.append(tg)
story.append(Spacer(1, 6))

story.append(q("1", "Déchiffrer (6,2) (3,6) (3,5) (2,2)"))
story.append(Paragraph(
    "On lit la grille ligne par colonne :", body))
story.append(bull("(6,2) → ligne 6, colonne 2 → <b>C</b>"))
story.append(bull("(3,6) → ligne 3, colonne 6 → <b>O</b>"))
story.append(bull("(3,5) → ligne 3, colonne 5 → <b>D</b>"))
story.append(bull("(2,2) → ligne 2, colonne 2 → <b>E</b>"))
story.append(Paragraph("Message déchiffré : <b>CODE</b>", body))

story.append(q("2", "Chiffrer BAC avec la clé SECURITY1024"))
story.append(Paragraph(
    "Ordre d'insertion avec la clé SECURITY1024 :<br/>"
    "SECURITY1024ABDFGHJKLMNOPQVWXYZ356789<br/>"
    "La grille est :", body))
grille_sec = [
    ['', '1', '2', '3', '4', '5', '6'],
    ['1', 'S', 'E', 'C', 'U', 'R', 'I'],
    ['2', 'T', 'Y', '1', '0', '2', '4'],
    ['3', 'A', 'B', 'D', 'F', 'G', 'H'],
    ['4', 'J', 'K', 'L', 'M', 'N', 'O'],
    ['5', 'P', 'Q', 'V', 'W', 'X', 'Z'],
    ['6', '3', '5', '6', '7', '8', '9'],
]
tgs = Table(grille_sec, colWidths=[1.1*cm]*7, rowHeights=[0.7*cm]*7)
tgs.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#455a64')),
    ('BACKGROUND', (0,0), (0,-1), colors.HexColor('#455a64')),
    ('TEXTCOLOR',  (0,0), (-1,0), colors.white),
    ('TEXTCOLOR',  (0,0), (0,-1), colors.white),
    ('GRID',       (0,0), (-1,-1), 0.5, colors.grey),
    ('ALIGN',      (0,0), (-1,-1), 'CENTER'),
    ('VALIGN',     (0,0), (-1,-1), 'MIDDLE'),
    ('FONTSIZE',   (0,0), (-1,-1), 9),
    ('FONTNAME',   (0,0), (-1,-1), 'Helvetica-Bold'),
]))
story.append(tgs)
story.append(Spacer(1, 4))
story.append(bull("B → ligne 3, colonne 2 → <b>(3,2)</b>"))
story.append(bull("A → ligne 3, colonne 1 → <b>(3,1)</b>"))
story.append(bull("C → ligne 1, colonne 3 → <b>(1,3)</b>"))
story.append(Paragraph("Message chiffré : <b>(3,2) (3,1) (1,3)</b>", body))

story.append(q("3", "Pourquoi le chiffrement de Polybe est-il symétrique ?"))
story.append(Paragraph(
    "Le chiffrement est <b>symétrique</b> car la même clé (et donc la même grille) sert "
    "à la fois à chiffrer et à déchiffrer. Il n'y a pas de clé publique et de clé privée "
    "distinctes : quiconque possède la clé peut indifféremment chiffrer ou déchiffrer.", body))

story.append(q("4", "Résultat de generer_ordre('AXU7')"))
story.append(Paragraph(
    "La fonction part de 'AXU7' puis ajoute toutes les lettres/chiffres absents dans "
    "l'ordre de la chaîne de référence :", body))
story.append(code(
"'AXU7BCDEFGHIJKLMNOPQRSTVWYZ0123456789'"
))
story.append(Paragraph(
    "(A, X, U, 7 déjà présents → ignorés lors du parcours de l'alphabet)", note_style))

story.append(q("5", "Coder la fonction <b>grille_vide(n)</b>"))
story.append(code(
"def grille_vide(n):\n"
"    return [['' for _ in range(n)] for _ in range(n)]"
))

story.append(q("6", "Compléter <b>generer_grille</b> (lignes 5, 6, 7)"))
story.append(code(
"def generer_grille(cle):\n"
"    ordre_insertion = generer_ordre(cle)\n"
"    grille = grille_vide(6)\n"
"    indice = 0\n"
"    for i in range(6):                          # ligne 5\n"
"        for j in range(6):                      # ligne 6\n"
"            grille[i][j] = ordre_insertion[indice]  # ligne 7\n"
"            indice = indice + 1\n"
"    return grille"
))

story.append(q("7", "Compléter <b>dechiffrer</b> (ligne 5)"))
story.append(code(
"def dechiffrer(cle, message):\n"
"    resultat = ''\n"
"    grille = generer_grille(cle)\n"
"    for t in message:\n"
"        resultat = resultat + grille[t[0]-1][t[1]-1]  # ligne 5\n"
"    return resultat"
))
story.append(Paragraph(
    "Les indices du tuple sont 1-indexés dans l'énoncé, d'où le −1 pour accéder à la liste Python (0-indexée).", note_style))

story.append(q("8", "Écrire la fonction <b>generer_dico</b>"))
story.append(code(
"def generer_dico(cle):\n"
"    grille = generer_grille(cle)\n"
"    dico = {}\n"
"    for i in range(6):\n"
"        for j in range(6):\n"
"            caractere = grille[i][j]\n"
"            dico[caractere] = (i + 1, j + 1)  # positions 1-indexées\n"
"    return dico"
))

story.append(q("9", "Écrire la fonction <b>chiffrer</b>"))
story.append(code(
"def chiffrer(cle, message):\n"
"    dico = generer_dico(cle)\n"
"    resultat = []\n"
"    for caractere in message:\n"
"        resultat.append(dico[caractere])\n"
"    return resultat"
))

story.append(q("10", "Différence entre chiffrement symétrique et asymétrique"))
story.append(Paragraph(
    "<b>Chiffrement symétrique :</b> la même clé est utilisée pour chiffrer et déchiffrer. "
    "Il est rapide mais nécessite un échange sécurisé de la clé entre les deux parties "
    "avant toute communication (ex. : AES, chiffrement de Polybe).", body))
story.append(Paragraph(
    "<b>Chiffrement asymétrique :</b> on utilise une paire de clés : une clé publique "
    "(connue de tous, sert à chiffrer) et une clé privée (connue du seul destinataire, "
    "sert à déchiffrer). Il résout le problème de l'échange de clé mais est plus lent "
    "(ex. : RSA).", body))
story.append(Paragraph(
    "Alice et Bob ont raison de vouloir utiliser un algorithme asymétrique pour s'échanger "
    "leur clé Polybe quotidienne : cela évite de devoir se retrouver physiquement ou "
    "d'utiliser un canal non sécurisé.", body))

# ══════════════════════════════════════════════════════════════════════════
# EXERCICE 3
# ══════════════════════════════════════════════════════════════════════════
story.append(PageBreak())
story.append(Paragraph("Exercice 3 — Démineur : POO, récursivité et bases de données  (8 points)", exo_style))
story.append(Spacer(1, 6))

story.append(Paragraph("Partie A : La classe Demineur", partie_style))

story.append(q("1", "Compléter l'assertion (ligne 7)"))
story.append(code(
"assert 0.10 <= pourcentage_mines <= 0.30, \\\n"
"    'Le pourcentage de mines doit être compris entre 10% et 30%.'"
))

story.append(q("2", "Compléter les lignes 8, 9 et 10 (attributs d'instance)"))
story.append(code(
"self.hauteur           = hauteur             # ligne 8\n"
"self.largeur           = largeur             # ligne 9\n"
"self.pourcentage_mines = pourcentage_mines   # ligne 10"
))

story.append(q("3", "Créer l'instance <b>demineur_intermediaire</b>"))
story.append(code(
"demineur_intermediaire = Demineur(16, 16, 0.156)"
))

story.append(Paragraph("Partie B : Création de la grille", partie_style))

story.append(q("4", "Compléter <b>grille_demineur_vide</b>"))
story.append(code(
"def grille_demineur_vide(self):\n"
"    return [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]"
))

story.append(q("5", "Compléter <b>placer_mines</b> (lignes 14 à 17)"))
story.append(code(
"def placer_mines(self):\n"
"    compteur_mines = 0\n"
"    nombre_bombes = self.largeur * self.hauteur * self.pourcentage_mines\n"
"    while compteur_mines < nombre_bombes:\n"
"        ligne   = randint(0, self.hauteur - 1)\n"
"        colonne = randint(0, self.largeur - 1)                     # ligne 14\n"
"        if self.grille_demineur[ligne][colonne] == 0:              # ligne 15\n"
"            self.grille_demineur[ligne][colonne] = -1              # ligne 16\n"
"            compteur_mines = compteur_mines + 1                    # ligne 17"
))

story.append(q("6", "Écrire <b>nombre_voisines_avec_mines</b>"))
story.append(code(
"def nombre_voisines_avec_mines(self, coordonnees_case):\n"
"    liste_voisines = self.voisines(coordonnees_case)\n"
"    compteur = 0\n"
"    for voisine in liste_voisines:\n"
"        ligne, colonne = voisine\n"
"        if self.grille_demineur[ligne][colonne] == -1:\n"
"            compteur += 1\n"
"    return compteur"
))

story.append(q("7", "Écrire <b>generer_demineur</b>"))
story.append(code(
"def generer_demineur(self):\n"
"    for ligne in range(self.hauteur):\n"
"        for colonne in range(self.largeur):\n"
"            if self.grille_demineur[ligne][colonne] != -1:\n"
"                self.grille_demineur[ligne][colonne] = \\\n"
"                    self.nombre_voisines_avec_mines((ligne, colonne))"
))

story.append(Paragraph("Partie C : Interface utilisateur", partie_style))

story.append(q("8", "Écrire la méthode <b>visibilite</b> (avec récursivité)"))
story.append(Paragraph(
    "Principe : si la case choisie contient une mine (−1), on dévoile toute la grille. "
    "Sinon, on dévoile la case courante. Si elle vaut 0 (aucune mine voisine), "
    "on appelle récursivement la méthode sur toutes ses voisines encore cachées.", body))
story.append(code(
"def visibilite(self, coordonnees_case):\n"
"    ligne, colonne = coordonnees_case\n"
"    valeur = self.grille_demineur[ligne][colonne]\n"
"\n"
"    # Cas mine : on dévoile toute la grille\n"
"    if valeur == -1:\n"
"        for i in range(self.hauteur):\n"
"            for j in range(self.largeur):\n"
"                self.grille_visibilite[i][j] = True\n"
"        return\n"
"\n"
"    # On dévoile la case courante\n"
"    if self.grille_visibilite[ligne][colonne]:\n"
"        return  # déjà visible, on arrête la récursion\n"
"    self.grille_visibilite[ligne][colonne] = True\n"
"\n"
"    # Si la case est 0 (aucune mine voisine), on propage\n"
"    if valeur == 0:\n"
"        for voisine in self.voisines(coordonnees_case):\n"
"            self.visibilite(voisine)"
))

story.append(Paragraph("Partie D : Jouer en ligne — SQL", partie_style))

story.append(q("9", "Clés étrangères de la table <b>Meilleur_score</b>"))
story.append(Paragraph(
    "La table <b>Meilleur_score</b> possède deux clés étrangères :", body))
story.append(bull(
    "<b>joueur</b> fait référence à la clé primaire <b>id_joueur</b> de la table <b>Joueur</b>."))
story.append(bull(
    "<b>niveau</b> fait référence à la clé primaire <b>niveau</b> de la table <b>Demineur</b>."))

story.append(q("10", "Requête pour obtenir le tableau niveau / meilleur score"))
story.append(code(
"SELECT niveau, score\n"
"FROM Meilleur_score\n"
"ORDER BY score DESC;"
))
story.append(Paragraph(
    "Si on veut uniquement le meilleur score par niveau (en éliminant les doublons) :", note_style))
story.append(code(
"SELECT niveau, MAX(score) AS score\n"
"FROM Meilleur_score\n"
"GROUP BY niveau\n"
"ORDER BY score DESC;"
))

story.append(q("11", "Mise à jour du mot de passe de Kirna"))
story.append(code(
"UPDATE Joueur\n"
"SET mot_de_passe = 'cGhhxDE4'\n"
"WHERE pseudo = 'Kirna';"
))

story.append(q("12", "Résultat de la requête JOIN"))
story.append(Paragraph(
    "La requête sélectionne les pseudos des joueurs ayant un score au niveau 'expert' "
    "supérieur à 1000 et un temps inférieur à 400.", body))
story.append(Paragraph(
    "Dans la table Meilleur_score, seule la ligne joueur=2, niveau='expert', score=1196, temps=366 "
    "satisfait toutes les conditions (366 < 400 et 1196 > 1000). Le joueur d'id 2 est <b>Raptor</b>.", body))
story.append(Paragraph("Résultat : <b>Raptor</b>", body))

story.append(q("13", "Corriger 'facile' en 'débutant' dans la table Demineur"))
story.append(Paragraph(
    "Il faut d'abord mettre à jour les références dans Meilleur_score, puis la table Demineur :", body))
story.append(code(
"UPDATE Meilleur_score\n"
"SET niveau = 'debutant'\n"
"WHERE niveau = 'facile';\n"
"\n"
"UPDATE Demineur\n"
"SET niveau = 'debutant'\n"
"WHERE niveau = 'facile';"
))

# ── Pied de page ───────────────────────────────────────────────────────────
story.append(Spacer(1, 14))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceAfter=6))
story.append(Paragraph(
    "Correction rédigée pour le baccalauréat NSI 2026 — 26-NSIJ1G11",
    ParagraphStyle('footer', parent=styles['Normal'],
        fontSize=8, textColor=colors.grey, alignment=TA_CENTER)))

doc.build(story)
print("PDF généré :", OUTPUT)

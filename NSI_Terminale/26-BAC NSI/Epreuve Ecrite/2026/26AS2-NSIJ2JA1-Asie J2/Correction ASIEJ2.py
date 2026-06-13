from reportlab.lib.pagesizes import A4
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                 Table, TableStyle, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER

OUTPUT = "C:\\Users\\thoma\\Desktop\\ASIEJ2\\correction_NSI_bac_2026_3.pdf"

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    rightMargin=2*cm, leftMargin=2*cm,
    topMargin=2*cm, bottomMargin=2*cm
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('MainTitle', parent=styles['Title'],
    fontSize=16, spaceAfter=6, textColor=colors.HexColor('#1a237e'))
exo_style = ParagraphStyle('Exo', parent=styles['Heading1'],
    fontSize=13, spaceAfter=4, spaceBefore=14,
    textColor=colors.white, backColor=colors.HexColor('#1a237e'), borderPad=5)
q_style = ParagraphStyle('Question', parent=styles['Heading2'],
    fontSize=11, spaceAfter=3, spaceBefore=8,
    textColor=colors.HexColor('#1565c0'))
body = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=10, spaceAfter=4, leading=14)
code_style = ParagraphStyle('Code', parent=styles['Normal'],
    fontSize=9, fontName='Courier',
    backColor=colors.HexColor('#f5f5f5'),
    borderColor=colors.HexColor('#cccccc'),
    borderWidth=0.5, borderPad=6,
    spaceAfter=6, spaceBefore=4, leading=13)
note_style = ParagraphStyle('Note', parent=styles['Normal'],
    fontSize=9, textColor=colors.HexColor('#b71c1c'),
    leftIndent=12, spaceAfter=4, leading=13)
sub_style = ParagraphStyle('Sub', parent=styles['Heading3'],
    fontSize=10, spaceAfter=3, spaceBefore=6,
    textColor=colors.HexColor('#37474f'))

def code(text):
    """Convertit un bloc de code en Paragraph avec sauts de ligne."""
    lines = text.split('\n')
    # Échapper les caractères XML et remplacer les espaces par des espaces insécables
    escaped = []
    for line in lines:
        line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        # Préserver l'indentation avec des espaces insécables
        stripped = line.lstrip(' ')
        n_spaces = len(line) - len(stripped)
        line = '&nbsp;' * n_spaces + stripped
        escaped.append(line)
    html = '<br/>'.join(escaped)
    return Paragraph(html, code_style)

story = []

# TITRE
story.append(Paragraph("Correction — Baccalauréat NSI 2026", title_style))
story.append(Paragraph("Sujet 26-NSIJ2JA1", ParagraphStyle('sub', parent=styles['Normal'],
    fontSize=11, textColor=colors.grey, spaceAfter=4)))
story.append(HRFlowable(width="100%", thickness=1.5,
    color=colors.HexColor('#1a237e'), spaceAfter=12))

# ══════════════════════════════════════════════════════════════════
# EXERCICE 1
# ══════════════════════════════════════════════════════════════════
story.append(Paragraph("Exercice 1 — Le Taquin  (6 points)", exo_style))
story.append(Spacer(1, 6))

story.append(Paragraph("Question 1", q_style))
story.append(Paragraph(
    "tab = [5, 3, 8, 0, 1, 2, 7, 6, 4]<br/>"
    "La case numéro 2 est à l'indice <b>5</b> (tab[5] = 2).", body))
story.append(Paragraph("Après exécution de tab[3] = tab[4] puis tab[4] = 0 :", body))
story.append(code("tab = [5, 3, 8, 1, 0, 2, 7, 6, 4]"))
story.append(Paragraph("Grille obtenue :", body))
data = [['5','3','8'],['1','','2'],['7','6','4']]
t = Table(data, colWidths=[1.2*cm]*3, rowHeights=[1.0*cm]*3)
t.setStyle(TableStyle([
    ('GRID',(0,0),(-1,-1),1,colors.black),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('FONTSIZE',(0,0),(-1,-1),11),
    ('BACKGROUND',(1,1),(1,1),colors.HexColor('#e3f2fd')),
]))
story.append(t)
story.append(Spacer(1, 6))

story.append(Paragraph("Question 3 — Expression booléenne « position gagnante »", q_style))
story.append(code("tab == [0, 1, 2, 3, 4, 5, 6, 7, 8]"))

story.append(Paragraph("Question 4 — Méthode est_gagnant", q_style))
story.append(code(
"def est_gagnant(self):\n"
"    return self.tab == [0, 1, 2, 3, 4, 5, 6, 7, 8]"))

story.append(Paragraph("Question 5 — Compléter indice (lignes 3 et 5)", q_style))
story.append(code(
"def indice(self, numero):\n"
"    assert type(numero) == int, 'numero doit être entier'\n"
"    assert 0 <= numero <= 8, 'numero de case non valide'   # ligne 3\n"
"    i = 0\n"
"    while self.tab[i] != numero:                           # ligne 5\n"
"        i = i + 1\n"
"    return i"))

story.append(Paragraph("Question 6 — Compléter jouer (lignes 2 à 6)", q_style))
story.append(code(
"def jouer(self, numero):\n"
"    if self.est_possible(numero):    # ligne 2\n"
"        i = self.indice(numero)\n"
"        j = self.indice(0)\n"
"        self.tab[j] = numero         # ligne 5\n"
"        self.tab[i] = 0              # ligne 6"))

story.append(Paragraph("Question 7 — Compléter melanger (lignes 4, 5, 6, 9)", q_style))
story.append(code(
"def melanger(self, n):\n"
"    precedent = None\n"
"    i = 0\n"
"    while i < n:                                 # ligne 4\n"
"        possibilites = self.coups_possibles()    # ligne 5\n"
"        choix = random.choice(possibilites)      # ligne 6\n"
"        if choix != precedent:\n"
"            self.jouer(choix)\n"
"            precedent = choix                    # ligne 9\n"
"            i = i + 1"))
story.append(Paragraph(
    "⚠ L'incrément de i doit être à l'intérieur du if, "
    "afin que le compteur n'avance que lorsqu'un coup est effectivement joué.", note_style))

story.append(Paragraph("Question 8 — Résolution automatique : ordre des coups", q_style))
story.append(Paragraph(
    "Pile après mélange + coup joueur (bottom → top) : 1, 4, 5, 2.<br/>"
    "La résolution dépile en ordre LIFO :", body))
data8 = [['Étape','Coup joué','État de la pile (top → bottom)'],
         ['Départ','—','[2, 5, 4, 1]  (top = 2)'],
         ['1','2','[5, 4, 1]'],
         ['2','5','[4, 1]'],
         ['3','4','[1]'],
         ['4','1','[ ]  → pile vide, position gagnante ✓']]
t8 = Table(data8, colWidths=[2*cm, 2.5*cm, 9*cm])
t8.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1565c0')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('FONTSIZE',(0,0),(-1,-1),9),
    ('GRID',(0,0),(-1,-1),0.5,colors.grey),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
]))
story.append(t8)
story.append(Spacer(1,4))

story.append(Paragraph("Question 9 — Méthode resoudre", q_style))
story.append(code(
"def resoudre(self):\n"
"    self.mode_resolution = True\n"
"    while not self.est_gagnant():\n"
"        coup = self.pile.depiler()\n"
"        print(coup)\n"
"        self.jouer(coup)"))

story.append(Paragraph("Question 10 — Pourquoi l'oubli de mode_resolution cause une non-terminaison", q_style))
story.append(Paragraph(
    "Sans passer en mode résolution, chaque appel à jouer() réempile le coup dans la pile. "
    "On dépile un coup, on le rejoue, il se réempile aussitôt : "
    "la pile ne se vide jamais et la boucle <i>while not self.est_gagnant()</i> tourne indéfiniment.", body))

story.append(Paragraph("Question 11 — Optimisation de jouer à partir de la ligne 8", q_style))
story.append(code(
"if not self.mode_resolution:\n"
"    if not self.pile.est_vide():\n"
"        sommet = self.pile.depiler()\n"
"        if sommet != numero:\n"
"            self.pile.empiler(sommet)\n"
"            self.pile.empiler(numero)\n"
"        # sinon les deux coups s'annulent, on n'empile rien\n"
"    else:\n"
"        self.pile.empiler(numero)"))

# ══════════════════════════════════════════════════════════════════
# EXERCICE 2
# ══════════════════════════════════════════════════════════════════
story.append(Paragraph("Exercice 2 — Bases de données et graphes  (6 points)", exo_style))
story.append(Spacer(1, 6))

story.append(Paragraph("Partie A — SQL", sub_style))

story.append(Paragraph("Question 1", q_style))
story.append(Paragraph(
    "id_pers est une clé étrangère dans la table <b>participation</b>.", body))

story.append(Paragraph("Question 2", q_style))
story.append(Paragraph(
    "id_partie ne peut pas être clé primaire de participation car plusieurs joueurs "
    "participent à la même partie : id_partie n'est donc pas unique dans cette table. "
    "La clé primaire est le couple <b>(id_partie, id_pers)</b>.", body))

story.append(Paragraph("Question 3", q_style))
story.append(code(
"INSERT INTO personne (id_pers, pseudo_pers, date_pers)\n"
"VALUES (42, 'theorie', '2022-12-14');"))

story.append(Paragraph("Question 4", q_style))
story.append(code(
"SELECT participation.id_partie\n"
"FROM participation\n"
"JOIN personne ON participation.id_pers = personne.id_pers\n"
"WHERE personne.pseudo_pers = 'test';"))

story.append(Paragraph("Question 5", q_style))
story.append(Paragraph(
    "Il faut d'abord supprimer les participations pour respecter l'intégrité référentielle :", body))
story.append(code(
"DELETE FROM participation\n"
"WHERE id_pers = 8;\n"
"DELETE FROM personne \n"
"WHERE id_pers = 8;"))

story.append(Paragraph("Partie B — Graphe et ordre alphabétique", sub_style))

story.append(Paragraph("Question 6 — Compléter indice (lignes 3 et 4)", q_style))
story.append(code(
"def indice(lettre, ordre):\n"
"    for i in range(len(ordre)):\n"
"        if ordre[i] == lettre:    # ligne 3\n"
"            return i              # ligne 4"))

story.append(Paragraph("Question 7 — Compléter comparer (lignes 7, 9, 11)", q_style))
story.append(code(
"# ligne 7  (i1 < i2 : mot1 avant mot2)\n"
"return True\n"
"# ligne 9  (i1 > i2 : mot1 après mot2)\n"
"return False\n"
"# ligne 11 (boucle terminée sans différence : mot1 est préfixe de mot2)\n"
"return len(mot1) <= len(mot2)"))

story.append(Paragraph("Question 8 — premiere_diff", q_style))
story.append(code(
"def premiere_diff(mot1, mot2):\n"
"    i = 0\n"
"    while i < len(mot1) and i < len(mot2) and mot1[i] == mot2[i]:\n"
"        i += 1\n"
"    return i"))
story.append(Paragraph(
    "Vérification : premiere_diff(\"oou\", \"ooai\") = 2 ✓  |  "
    "premiere_diff(\"aio\", \"aioiee\") = 3 ✓", note_style))

story.append(Paragraph("Question 9 — dico_adj(mots_exemple)", q_style))
story.append(code(
"{\n"
"  'u': ['a', 'y'],\n"
"  'y': ['i', 'a'],\n"
"  'a': ['i'],\n"
"  'o': ['u'],\n"
"  'e': ['a']\n"
"}"))

story.append(Paragraph("Question 10 — Type de parcours", q_style))
story.append(Paragraph(
    "C'est un <b>parcours en profondeur (DFS)</b>. La fonction s'appelle récursivement "
    "sur chaque voisin avant d'ajouter le sommet courant à tri, ce qui est caractéristique "
    "d'un tri topologique par DFS.", body))

story.append(Paragraph("Question 11 — Fonction trier", q_style))
story.append(code(
"def trier(mots):\n"
"    adj = dico_adj(mots)\n"
"    tri = []\n"
"    deja_vus = []\n"
"    voyelles = ['a', 'e', 'i', 'o', 'u', 'y']\n"
"    for v in voyelles:\n"
"        if v not in deja_vus:\n"
"            deja_vus.append(v)\n"
"            parcours(adj, v, deja_vus, tri)\n"
"    tri.reverse()\n"
"    return tri"))

# ══════════════════════════════════════════════════════════════════
# EXERCICE 3
# ══════════════════════════════════════════════════════════════════
story.append(Paragraph("Exercice 3 — Robots et routage RIP  (8 points)", exo_style))
story.append(Spacer(1, 6))

story.append(Paragraph("Partie A — Gestion des déplacements", sub_style))

story.append(Paragraph("Question 1 — Parcours pour '4(AG)'", q_style))
story.append(Paragraph(
    "'4(AG)' = répéter 4 fois le bloc AG = AGAGAGAG.<br/>"
    "Le robot trace un <b>carré</b> dans le sens antihoraire et revient à sa position initiale.", body))

story.append(Paragraph("Question 2 — caracteres_valides, ligne 4", q_style))
story.append(code("return intrus == []"))

story.append(Paragraph("Question 3 — entiers_valides, lignes 4, 8, 9", q_style))
story.append(code(
"def entiers_valides(chaine):\n"
"    chiffres = '0123456789'\n"
"    if chaine[len(chaine)-1] in chiffres:   # fin de chaîne = chiffre\n"
"        return False                         # ligne 4\n"
"    for indice in range(1, len(chaine)):\n"
"        if chaine[indice] == ')':\n"
"            if chaine[indice - 1] in chiffres:\n"
"                return False                 # lignes 8-9\n"
"    return True"))

story.append(Paragraph("Question 4 — parenthesage_correct", q_style))
story.append(code(
"def parenthesage_correct(chaine):\n"
"    parenthese = 0\n"
"    for c in chaine:\n"
"        if c == '(':\n"
"            parenthese += 1\n"
"        elif c == ')':\n"
"            parenthese -= 1\n"
"        if parenthese < 0:\n"
"            return False\n"
"    return parenthese == 0"))

story.append(Paragraph("Question 5 — lire_nombre('AD179AGA', 2) : itérations", q_style))
data5 = [['Itération','nombre','indice'],
         ['1',"'1'",'3'],
         ['2',"'17'",'4'],
         ['3',"'179'",'5']]
t5 = Table(data5, colWidths=[3*cm, 5*cm, 5*cm])
t5.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1565c0')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('FONTSIZE',(0,0),(-1,-1),9),
    ('GRID',(0,0),(-1,-1),0.5,colors.grey),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME',(1,1),(-1,-1),'Courier'),
]))
story.append(t5)
story.append(Paragraph("Retourne (179, 4) ✓", note_style))

story.append(Paragraph("Question 6 — lire_bloc, lignes 7, 8, 9", q_style))
story.append(code(
"bloc = bloc + caractere      # ligne 7\n"
"indice = indice + 1          # ligne 8\n"
"caractere = chaine[indice]   # ligne 9"))

story.append(Paragraph("Question 7 — lire_parcours, lignes 12, 16, 20", q_style))
story.append(code(
"t = lire_nombre(chaine, indice)   # ligne 12 (cas répétition)\n"
"t = lire_bloc(chaine, indice)     # ligne 16 (cas début de bloc)\n"
"lire_parcours(bloc)               # ligne 20 (exécuter le bloc nombre fois)"))

story.append(Paragraph("Partie B — Routage RIP", sub_style))

story.append(Paragraph("Question 8 — Modifications après ajout du lien 4 ↔ 46", q_style))
story.append(Paragraph(
    "Le robot 4 est désormais voisin direct de 46. Pour le robot 91, "
    "atteindre 46 via 4 ne prend plus que <b>2 sauts</b> (au lieu de 3).<br/>"
    "Modification : destination 46 → prochain = 4, distance = 2.", body))

story.append(Paragraph("Question 9 — Modifications après arrivée du robot 87", q_style))
story.append(Paragraph("Le robot 87 contacte 91 et lui communique sa table :", body))
data9 = [['destination','prochain robot','distance'],
         ['87','87','1'],['63','87','2'],['36','87','3']]
t9 = Table(data9, colWidths=[4*cm,5*cm,4.5*cm])
t9.setStyle(TableStyle([
    ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#1565c0')),
    ('TEXTCOLOR',(0,0),(-1,0),colors.white),
    ('FONTSIZE',(0,0),(-1,-1),9),
    ('GRID',(0,0),(-1,-1),0.5,colors.grey),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
]))
story.append(t9)
story.append(Spacer(1,4))

story.append(Paragraph("Partie C — Programmation du routage", sub_style))

story.append(Paragraph("Question 10 — ajouter_voisin", q_style))
story.append(code(
"def ajouter_voisin(self, id_voisin):\n"
"    self.table_routage[id_voisin] = {\"prochain\": id_voisin, \"distance\": 1}"))

story.append(Paragraph("Question 11 — nombre_sauts, ligne 5", q_style))
story.append(code(
"return self.table_routage[identifiant][\"distance\"]"))

story.append(Paragraph("Question 12 — voisins", q_style))
story.append(code(
"def voisins(self):\n"
"    return [dest for dest in self.table_routage\n"
"            if self.table_routage[dest][\"prochain\"] == dest\n"
"            and self.table_routage[dest][\"distance\"] == 1]"))

story.append(Paragraph("Question 13 — communiquer_extrait_table", q_style))
story.append(code(
"def communiquer_extrait_table(self, voisin):\n"
"    extrait = {}\n"
"    for dest, info in self.table_routage.items():\n"
"        if info[\"prochain\"] != voisin:\n"
"            extrait[dest] = info\n"
"    return extrait"))

# FIN
story.append(Spacer(1, 12))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceAfter=6))
story.append(Paragraph(
    "Correction rédigée pour le baccalauréat NSI 2026 — 26-NSIJ2JA1",
    ParagraphStyle('footer', parent=styles['Normal'],
        fontSize=8, textColor=colors.grey, alignment=TA_CENTER)))

doc.build(story)
print("PDF généré :", OUTPUT)
# 🐍 LP01 : Constructions Élémentaires

<div class="subtitle" style="font-size: 1.2em; color: #546e7a; margin-bottom: 25px; font-style: italic;">
Introduction aux bases du langage Python : variables, types de données et logique booléenne.
</div>

---

[![COURS](../_graphics/icones/icons8-pdf-30.png)](./C106-Primitives/C106-Primitives.pdf)

## 📂 Ressources du Chapitre

Accédez ici à l'ensemble des documents de cours et aux outils de révision interactive.

| Support | Description | Lien de consultation |
| :--- | :--- | :--- |
| 📕 **Cours** | Le support de cours complet en version PDF. | [![COURS](../../../_graphics/icones/icons8-pdf-30.png)](./LP01_Constructions_elementaires.pdf) |
| 💡 **Synthèse** | Fiche récapitulative des concepts clés (HTML). | [:octicons-zap-24: Voir la synthèse](html/LP01_synthese.html){:target="_blank"} |
| 🎴 **Flashcards** | Cartes de mémorisation pour réviser les notions. | [:octicons-id-card-24: Lancer l'activité](html/LP01_flashcards.html){:target="_blank"} |
| 📝 **Quiz** | Auto-évaluation rapide sur le chapitre. | [:octicons-checklist-24: Faire le quiz](html/LP01_quiz.html){:target="_blank"} |

---

## 💻 Activités de Programmation

!!! abstract "Activité 1 : Découverte des types et variables"
    Dans cette activité, vous apprendrez à manipuler les nombres, les textes et à comprendre comment Python stocke les informations.
    
    * **Fichier source :** [:octicons-download-24: LP01-ACT1.ipynb](files/LP01-ACT1.ipynb)
    * **Exécution interactive :** [![Binder](https://mybinder.org/v2/badge_logo.svg)](https://mybinder.org/v2/gh/thomasricart/ENSEIGNEMENT_G/main?filepath=docs/NSI_Premiere/LP_Langage_Programmation/LP01_Constructions_elementaires/LP01-ACT1.ipynb)

### 🧩 Concepts illustrés
```python
# 1. Affectation et calcul
largeur = 10
hauteur = 5
aire = largeur * hauteur  # 50

# 2. Manipulation de texte (Slicing)
sujet = "Informatique"
print(sujet[0:4])  # Affiche "Info"

# 3. Logique
est_majeur = True
a_permis = False
peut_conduire = est_majeur and a_permis # False
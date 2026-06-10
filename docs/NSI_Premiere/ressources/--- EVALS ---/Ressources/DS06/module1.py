notes = [10,13,8,8]
coeff = [3,2,1,2]

def verif_nb_notes(notes):
    if len(notes) > 2:
        return True
    return False

def enleve_note_min(notes,coeff):
    note_min = notes[0]
    for i in range(len(notes)):
        if notes[i] < note_min:
            note_min = notes[i]
            coeff_note_min = i
    del notes[coeff_note_min]
    del coeff[coeff_note_min]

def moyenne(notes,coeff):
    somme_valeurs = 0
    somme_coeffs = 0
    for i in range(len(notes)):
        somme_valeurs = somme_valeurs + notes[i]
        somme_coeffs = somme_coeffs + coeff[i]
    moyenne_ponderee = somme_valeurs / somme_coeffs
    return moyenne_ponderee

def calcule_moyenne(notes,coeff):
    if verif_nb_notes(notes) == False:
        enleve_note_min(notes,coeff)
    moyenne_ponderee = moyenne(notes,coeff)
    return(moyenne_ponderee)
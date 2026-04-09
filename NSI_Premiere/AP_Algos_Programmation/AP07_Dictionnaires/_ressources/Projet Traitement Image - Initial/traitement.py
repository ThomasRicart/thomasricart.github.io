# -*- coding:Utf-8 -*-
#------------------------------------------------------------------------------
# Author:  M. SALVA
# Name:    main.py
# Purpose: Logiciel de traitement d'image au format PBM, PGM ou PPM
# Created: 25/11/2020
# Python:  3.4.5
# Modules: traitement, support
# Licence: Creative Commons BY NC SA
#-------------------------------------------------------------------------------

from support import *

def symHori(img):
    """
    Symétrie axe horizontale
    :param img : Dict : {"meta" : {"titre" : "titre", ...},
                         "pix" : [[(255, 255, 255), (253, 0, 34), (233, 0, 0), ...]}
    :return: img
    """
    col = img["meta"]["col"]
    lig = img["meta"]["lig"]
    pix = img["pix"]

    newpix = []
    for y in range(lig-1, -1, -1):
        newpix.append(pix[y])

    img["pix"] = newpix
    # img["meta"]["mod"]="Symétrie horizontale"
    # print("Symétrie horizontale")
    return img

def symVert(img):
    """
    Symétrie axe VERTICAL
    :param img : Dict : {"meta" : {"titre" : "titre", ...},
                         "pix" : [[(255, 255, 255), (253, 0, 34), (233, 0, 0), ...]}
    :return: img
    """
    lig = img["meta"]["lig"]
    pix = img["pix"]

    newpix = []
    for i in range(lig):
        for p in pix[i]:
            r, v, b = p
            # à compléter ......................

    # img["meta"]["mod"]="Symétrie horizontale"
    # print("Symétrie horizontale")
    return img


def rotation180(img):
    # à compléter ......................

    return img


#-------------------------------------------------------------------------------
if __name__ == '__main__':
    img = ouvrir("images/salva.ppm")
    img2 = symHori(img)
    sauver(img2)

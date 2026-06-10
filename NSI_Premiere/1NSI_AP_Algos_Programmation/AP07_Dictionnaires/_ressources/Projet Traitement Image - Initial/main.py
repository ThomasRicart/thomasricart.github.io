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

from traitement import *
from support import *
from copy import deepcopy

# -*- coding:Utf-8 -*-
from tkinter import *

#Programme principal
def fen_ouvrir_1():
    img = ouvrir("images/" + chemin_1.get())
    afficher(img)

def fen_ouvrir_2():
    img = ouvrir("images/" + chemin_2.get())
    afficher(img)

def fen_comparer():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = ouvrir("images/" + chemin_2.get())
    comparer(img1, img2)

def fen_symHori():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = symHori(deepcopy(img1))
    comparer(img1, img2)

def fen_symVert():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = symVert(deepcopy(img1))
    comparer(img1, img2)

def fen_rotation180():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = rotation180(deepcopy(img1))
    comparer(img1, img2)

def fen_rotation90():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = rotation90(deepcopy(img1))
    comparer(img1, img2)

def fen_gris():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = gris(deepcopy(img1))
    comparer(img1, img2)

def fen_noir():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = noir(deepcopy(img1))
    comparer(img1, img2)

def fen_luminosite():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = luminosite(deepcopy(img1), int(lum.get())/100)
    comparer(img1, img2)

def fen_saturation():
    img1 = ouvrir("images/" + chemin_1.get())
    img2 = saturation(deepcopy(img1), int(sat.get())/100)
    comparer(img1, img2)

#Creation de la fenetre
fen = Tk()
fen.title("Editeur d'images")

#Creation du bouton
Label(fen, text="Quelle image du dossier 'images'\nsouhaitez-vous afficher ou comparer ?").grid(row=0,column=0, columnspan=4)
chemin_1 = StringVar()
chemin_1.set("salva.ppm")
Label(fen, text="image n°1 :").grid(row=1,column=0)
Entry(fen, textvariable=chemin_1, width=30).grid(row=1,column=1)
Button(fen,text='Afficher',command=fen_ouvrir_1).grid(row=1,column=2)
chemin_2 = StringVar()
Label(fen, text="image n°2 :").grid(row=2,column=0)
Entry(fen, textvariable=chemin_2, width=30).grid(row=2,column=1)
Button(fen,text='Afficher',command=fen_ouvrir_2).grid(row=2,column=2)
Button(fen,text='Comparer',command=fen_comparer).grid(row=1,column=3,rowspan=2)
Label(fen, text="Apliquer une transformation à l'image n°1 :").grid(row=3,column=0, columnspan=4)
Button(fen,text='Symétrie Horizontale',command=fen_symHori).grid(row=4,column=1)
Button(fen,text='Symétrie Verticale',command=fen_symVert).grid(row=5,column=1)
Button(fen,text='Rotation de 180°',command=fen_rotation180).grid(row=6,column=1)
Button(fen,text='Rotation de 90°',command=fen_rotation90).grid(row=7,column=1)
Button(fen,text='Convertir en niveau de gris',command=fen_gris).grid(row=8,column=1)
Button(fen,text='Convertir en noir et blanc',command=fen_noir).grid(row=9,column=1)
lum = StringVar()
Entry(fen, textvariable=lum, width=5).grid(row=10,column=2)
Button(fen,text="Modifier la luminosité (+/- %)",command=fen_luminosite).grid(row=10,column=1)
sat = StringVar()
Entry(fen, textvariable=sat, width=5).grid(row=11,column=2)
Button(fen,text="Modifier la saturation (+/- %)",command=fen_saturation).grid(row=11,column=1)

fen.mainloop()
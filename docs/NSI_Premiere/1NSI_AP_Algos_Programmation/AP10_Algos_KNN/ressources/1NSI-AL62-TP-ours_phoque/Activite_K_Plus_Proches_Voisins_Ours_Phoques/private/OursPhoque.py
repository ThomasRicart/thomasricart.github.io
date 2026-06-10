#-------------------------------------------------------------------------------
# Name: Les ours et les phoques
# Author:      Boissac Frédéric
# Created:     version 1.0 : 25/10/2019 ; version 2.0 : 17/04/2024
# Copyright:   (c) Boissac 2019
# Version : 2.0
# Licence:     licence extraterrestre certifiée NSA free (pour une utilisation non commerciale et éducative)
#-------------------------------------------------------------------------------



import  tkinter as Tki


from threading import Thread

import sys
sys.path.append("..")  # Ajoute le répertoire parent au chemin de recherche des modules


from Activite_K_Plus_Proches_voisins import *

from tkinter.messagebox import *
#creation des variables globales
largeur = 800
hauteur = 500
carre=[0] * largeur
Pixel = [[[]] *hauteur  for _ in range(largeur)]

valeur_K =3 #valeur par defaut




def InitialiseVar():
    global Pixel,n_thread_ouvert,n_thread_ferme,animal,ListAnimaux,zoneDiffusion,lancementCalcul,N_ours,N_phoque,Inconnu,ListDicoAnimaux,valeur_K
    TypeDeZonePixel=[]
    for x in range(0,largeur):
       for y in range(0,hauteur):
          Pixel[x][y]=[0]*7

    n_thread_ouvert,n_thread_ferme=0,0
    animal=1 #ours -1 pour lephoque
    N_ours=0
    N_phoque=0
    ListAnimaux=[]
    ListDicoAnimaux=[]
    zoneDiffusion = [[0] * hauteur for _ in range(largeur)] # rappel de lordre : A = [[0] *colonnes  for _ in range(lignes)]  #A[lignes][colonnes]
    lancementCalcul=[]
    valeur_K =3
    Inconnu={'X':-1,'Y':-1,'nom':'ours'}





class  ThreadCalcul(Thread):



    def __init__(self,nbre_animaux,X,Y,Lanimal):
        Thread.__init__(self)
        self.nbre=nbre_animaux
        self.x=X
        self.y=Y


        if titre[94:98]!="oiss":return
        self.Lanimal=Lanimal



    def run(self):
        """Code à exécuter pendant l'exécution du thread."""
        global n_thread_ouvert,n_thread_ferme
        n_thread_ouvert+=1
        #print("lancement du thread ",self.nbre, "Le nbre de threads ouvert est : ",n_thread_ouvert)
        miseAjourDesZonesDiffusionetZonesKprochesVoisins(self.x,self.y,self.Lanimal)
        n_thread_ferme+=1
        #print("fin du thread ",self.nbre ," Le nbre de threads fermé est : ",n_thread_ferme, ' il en reste ',n_thread_ouvert-n_thread_ferme, ' à fermer')









def InitialiseCarre():
    for i in range(largeur):
        carre[i]=i*i

def CalculValeurPixel(x,y,d):
    """ chaque pixel est associé a un tableau de 7 valeurs,ds lesquels on entre les 7 animaux les plus proches, on tri au fur et a mesure qu on entre un animal avec sa distance
    """

    for i in range(7):
        if Pixel[x][y][i]==0 : #cas ou on a pas encore rempli les 7 voisins, on rempli
           Pixel[x][y][i]=d

           if i==6 :
            Pixel[x][y].sort()
           return


    if d<Pixel[x][y][6] : #la distance est plus petite que la plus grande distance on integre donc ds les 7 premiers
         Pixel[x][y][6]=d
         if d<Pixel[x][y][5] :
            Pixel[x][y].sort()




def ValeurDuPixelAvecAlgoKvoisins(k,i,j):
    """
      retourne la valeur du pixel ds l algo des k plus proches voisins : 1 pour ours et -1 pour phoque
    """
    valeur=0

    """
    pour chaque pixel on regarde ds la liste des 7 distances associées les K premières pour voir si ce sont des ours (valeurs paires)
    ou des phoques (valeurs de d impairs)
    """
    for n in range(k) :
        if Pixel[i][j][n]&1!=0 :
            valeur+=1
        else :
           valeur-=1
    return valeur

def ChoixDuCalcul(x):
    if n_thread_ouvert!=n_thread_ferme:
        showinfo('Calcul en cours','Merci de patienter, les calculs de zones ne sont pas terminés')
        #print('threads non fermés')
        return



    if N_phoque<4 or N_ours<4 :
        showinfo('Base de données insuffisante','Une évaluation IA des zones nécessite un minimum de 4 ours et 4 phoques')

        return

    if x==1 :
        calculEtAfficheZones(zoneDiffusion)
        TypeDeZonePixel=zoneDiffusion

        return

    zoneKPlusProchesVoisins = [[0] * hauteur for _ in range(largeur)] # rappel de lordre : A = [[0] *colonnes  for _ in range(lignes)]  #A[lignes][colonnes]



    #pour chaque pixel je regarde s il a plus d ours ou de phoques
    """
              pour chaque pixel on regarde ds la liste des 7 distances associées les K premières pour voir si ce sont des ours (valeurs paires)
              ou des phoques (valeurs de d impairs)
    """
    global valeur_K
    valeur_K=x

    for i in range(largeur):

        for j in range(hauteur):
            zoneKPlusProchesVoisins[i][j]=ValeurDuPixelAvecAlgoKvoisins(x,i,j)
            """

            for n in range(x) :
                        if Pixel[i][j][n]&1!=0 :
                            zoneKPlusProchesVoisins[i][j]+=1
                        else :
                            zoneKPlusProchesVoisins[i][j]-=1
            """

    calculEtAfficheZones(zoneKPlusProchesVoisins)




def calculEtAfficheZones(zonepixel):

  test = [[0] * hauteur for _ in range(largeur)]


  for y1 in range(hauteur-1):
        for x1 in range (largeur-1):
            if test[x1][y1]==0 :
              xmax=x1
              if zonepixel[x1][y1]>0:

                 while xmax<largeur and zonepixel[xmax][y1]>0 and test[xmax][y1]==0  :
                    test[xmax][y1]=1
                    xmax+=1
                 Canevas.create_line(x1, y1, xmax+1, y1+1, width=2, fill='green')
              elif zonepixel[x1][y1]<0:
                 while xmax<largeur and zonepixel[xmax][y1]<0 and test[xmax][y1]==0 :
                    test[xmax][y1]=1
                    xmax+=1

                 Canevas.create_line(x1, y1, xmax+1, y1+1, width=2, fill='blue')

  for pos in ListAnimaux :
     if pos[0]==1 :
       Canevas.create_image(pos[1],pos[2],anchor = Tki.NW, image=photoours)

     else:
       Canevas.create_image(pos[1],pos[2],anchor = Tki.NW, image=photophoque)
  global ListDicoAnimaux,Inconnu
  if Inconnu["X"]!=-1 :
     Canevas.create_image(Inconnu["X"],Inconnu["Y"],anchor = Tki.NW, image=photopoint)
     List=ListDicoAnimaux[:]
     Canevas.create_text(Inconnu["X"]+15,Inconnu["Y"]+45, text=Prediction(List,Inconnu,valeur_K), font="Arial 15 bold", fill="red")
  Canevas.update()




def miseAjourDesZonesDiffusionetZonesKprochesVoisins (x,y,Lanimal):
    carreY=[]


    for i in range(largeur):
        #carreX=(i-x)**2
        carreX=carre[abs(i-x)]
        for j in range(hauteur):
            if i==0 : carreY.append(carre[abs(j-y)])#carreY.append((j-y)**2)

            """
              calcul pour chaque pixel de la distance d qui sépare ce pixel de l anima qu on vient de poser
              (en fait on prend d**2 ce qui ne change rien mais est plus rapide
            """
            # d=math.sqrt(carreX+carreY[j])
            d=(carreX+carreY[j]) #inutile de prendre la racine, si la distance est grande son carré aussi...

            if Lanimal>0 : #astuce pour differencier les ours des phoques on arrondit d à sa valeur pair ou impair suivant le cas
                if d&1==0 : d+=1
            else :
                if d&1!=0 : d+=1



            """
            K plus proches voisins : pour chaque pixel on associe un tableau de 7 distances triées par ordre croissant. si la nouvelle distance est plus petite que la 7eme elle entre ds ce tableau
            Une astuce d arrondi auchiffre pair superieur fait que sid est pair on sait que c est un ours sinon c est un phoque

            """
            CalculValeurPixel(i,j,d)

            """
            zoneDiffusion :pour l algo de diffusion, chaque pixel reçoit un quotapositifi ou négatif suivant ours ou phoque
            qui decroit lorsque la distance anima_pixel augmente
            Apres positionnement si c est >0 c est sous influence ours sinon sous infuence phoque
            """
            ajout=Lanimal/(1+d) #propagation par diffusion
            zoneDiffusion[i][j]+=ajout

#gere le cmlic de souris sur le canvas et genere un nouveau calcul
def clic(event):
    global N_phoque,N_ours,ListDicoAnimaux,Inconnu
    # position du pointeur ,de la souris
    X = event.x
    Y = event.y

    if animal==2 :
        Canevas.create_image(X-20,Y-15,anchor = Tki.NW, image=photopoint)
        Inconnu["X"],Inconnu["Y"]=X-20,Y-15
        List=ListDicoAnimaux[:]
        PredictionEleve=Prediction(List,Inconnu,valeur_K)
        Canevas.create_text(Inconnu["X"]+15,Inconnu["Y"]+45, text=PredictionEleve, font="Arial 15 bold", fill="red")
        Valeur=ValeurDuPixelAvecAlgoKvoisins(valeur_K,Inconnu["X"]+20,Inconnu["Y"]+15)

        if PredictionEleve=="Ours":
            if Valeur>=0 :showinfo("Prediction",'Prédiction Correcte'+'\n'+"Calcul avec l'Algo des "+str(valeur_K)+" plus proches voisins")
            else : showinfo("Prediction",'Prédiction Incorrecte'+'\n'+"Calcul avec l'Algo des "+str(valeur_K)+" plus proches voisins")
        else :
            if Valeur<=0 :showinfo("Prediction",'Prédiction Correcte'+'\n'+"Calcul avec l'Algo des "+str(valeur_K)+" plus proches voisins")
            else : showinfo("Prediction",'Prédiction Incorrecte'+'\n'+"Calcul avec l'Algo des "+str(valeur_K)+" plus proches voisins")

        return


    if animal==1 :
     Canevas.create_oval(X-20,Y-20,X+20,Y+20, fill="green",outline="green")
     Canevas.create_image(X-20,Y-15,anchor = Tki.NW, image=photoours)
     ListAnimaux.append([1,X-20,Y-15])
     ListDicoAnimaux.append({'X':X-20,'Y':Y-20,'nom':'ours'})
     N_ours+=1

    else :
     Canevas.create_oval(X-20,Y-20,X+20,Y+20, fill="blue",outline="blue")
     Canevas.create_image(X-20,Y-20,anchor = Tki.NW, image=photophoque)
     ListDicoAnimaux.append({'X':X-20,'Y':Y-20,'nom':'phoque'})
     ListAnimaux.append([-1,X-20,Y-20])
     N_phoque+=1


    nbre_animaux=len(ListAnimaux)

    #on cree un nouveau thread de calcul

    lancementCalcul.append(ThreadCalcul(nbre_animaux,X,Y,animal))

    lancementCalcul[nbre_animaux-1].start()


   # miseAjourZoneDiffusion(X,Y,animal)

def choisirlanimal(x):
    global animal
    animal=x

def affiche():
 global largeur,hauteur,Rectangle

 Rectangle=Canevas.create_rectangle(0,0,largeur,hauteur, fill="pink")##pas comme en java ce sont les veritables coordonnees des 2 extremites du rect




 Canevas.create_text(largeur-200,hauteur-35, text="Place des ours et des phoques !", font="Arial 15 bold", fill="blue")
 Canevas.create_text(largeur-200,hauteur-20, text="(Au minimum  4 ours et 4 phoques) ", font="Arial 10 bold", fill="blue")


 Canevas.create_window(70,hauteur-30,window=boutonchoixcalcul)

 Canevas.create_window(200,hauteur-30,window=boutonchoixanimal)

 Canevas.create_window(330,hauteur-30,window=boutonRecommencer)


def Initialise():
    InitialiseVar()
    affiche()


#Debut de l'algorithme principal


Mafenetre = Tki.Tk()
titre="Où sont les ours et les phoques ?                             Version 2.0 2019/2024 Freeware Boissac Frédéric"

Mafenetre.title(titre)

InitialiseVar()

#creation des images qu on va utiliser
photophoque = Tki.PhotoImage(file="private/phoque.png")
photoours = Tki.PhotoImage(file="private/ours.png")
photopoint = Tki.PhotoImage(file="private/petitpoint.png")

InitialiseCarre()


Canevas = Tki.Canvas(Mafenetre,width=largeur,height=hauteur,bg ='green')



boutonchoixcalcul=Tki.Menubutton(Canevas, text="Calcul des zones",font="Arial 9 bold",relief='raised',bd=5,width=15,height=2)#mon boutton est l esclave de Canevas
boutonchoixcalcul.menu = Tki.Menu(boutonchoixcalcul, tearoff=0,font="Arial 9 bold",selectcolor='red',relief='raised',bd=5)
boutonchoixcalcul['menu'] = boutonchoixcalcul.menu

boutonchoixcalcul.menu.add_command(label='Par 3 plus proches voisins',command = lambda x=3:ChoixDuCalcul(x))
boutonchoixcalcul.menu.add_command(label='Par 5 plus proches voisins',command = lambda x=5:ChoixDuCalcul(x))
boutonchoixcalcul.menu.add_command(label='Par 7 plus proches voisins',command = lambda x=7:ChoixDuCalcul(x))
boutonchoixcalcul.menu.add_command(label='Algo amélioré : Propagation par diffusion',command = lambda x=1:ChoixDuCalcul(x))

boutonchoixanimal = Tki.Menubutton(Canevas, text='Ours ou phoque?',relief='raised',font="Arial 9 bold",bd=5,width=15,height=2)
boutonchoixanimal.menu = Tki.Menu(boutonchoixanimal, tearoff=0,font="Arial 9 bold",selectcolor='red',relief='raised',bd=5)
boutonchoixanimal['menu'] = boutonchoixanimal.menu
boutonchoixanimal.menu.add_command(label='Ours',command = lambda x=1:choisirlanimal(x))
boutonchoixanimal.menu.add_command(label='Phoque',command = lambda x=-1:choisirlanimal(x))
boutonchoixanimal.menu.add_command(label='Inconnu',command = lambda x=2:choisirlanimal(x))



boutonRecommencer=Tki.Button(Canevas, text="Recommencer",font="Arial 9 bold",relief='raised',bd=5,width=15,height=2,command = Initialise)#mon boutton est l esclave de Canevas



affiche()


Canevas.bind('<Button-1>', clic) # évévement clic gauche (press)


Canevas.focus_set()


Canevas.pack(padx=10,pady=10)



Canevas.mainloop()


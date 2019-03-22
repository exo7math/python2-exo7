
##############################
# Lyapunov
##############################


##############################
# Activité 1 - Suite logistique
##############################

from math import *

##############################
## Question 1 ##

def liste_suite(r,Nmin,Nmax):
    """ Liste des termes de la suite logistique (u_n) 
    pour n entre Nmin et Nmax """
    k = 0
    u =  1/2   # terme initial
    liste = [u]
    while k < Nmax-1:
        u = r*u*(1-u)
        liste += [u]
        k += 1
    return liste[Nmin:]

# Test
print("--- Suite logistique ---")
print("r=0.5")
print(liste_suite(0.5,0,10))
print("r=1.5")
print(liste_suite(1.5,0,10))
print("r=3.2")
print(liste_suite(3.2,0,20))
print("r=3.5")
print(liste_suite(3.5,0,10))

##############################
## Question 2 ##


def bifurcation(Nmin=100,Nmax=200,epsilon=0.01):
    """ Liste de points de l'ensemble de bifurcation (r,u_n)
    avec n entre Nmin et Nmax
    et r qui varie entre 0 et 4.0 par pas de longueur epsilon """
    u0 = 0.5 # terme initial
    r = 0 # r initial
    mespoints = []

    while r <= 4.0:
        liste_u = liste_suite(r,Nmin,Nmax) # On calcule la suite
        for u in liste_u:
            mespoints = mespoints + [(r,u)]
        r = r + epsilon

    return mespoints



# Test
print("--- Points d'accumulation ---")
# fixer epsilon = 1 pour test
print(bifurcation(Nmin=0,Nmax=5,epsilon=1))


##############################
## Question 3 ##


# Constante pour fenêtre réelle et écran
xmin, xmax = 0, 4
ymin, ymax = 0, 1

# Zoom 
# xmin, xmax = 3.4, 3.9
# ymin, ymax = 0.6, 1

Nx = 1000   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 


def xy_vers_ij(x,y):
    """ Passage des coordonnées réelles (x,y)
    aux coordonnées graphiques (i,j) """
    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny

    i = round((x-xmin)/pasx)
    j = round(Ny-(y-ymin)/pasy)

    return i,j

##############################
# Allumer un pixel

def afficher_pixel(i,j,couleur):
    """ Affiche un pixel """
    canvas.create_rectangle(i,j,i+1,j+1,fill=couleur,outline=couleur,width=1)
    # canvas.create_line(i,j,i+1,j+1,fill=couleur,width=1)
    return


def afficher_axes():
    """ Dessine les axes """
    i,j = xy_vers_ij(xmin,0)
    ii,jj = xy_vers_ij(xmax,0)
    canvas.create_line(i,j,ii,jj,fill='black',width=2)
    i,j = xy_vers_ij(xmin,ymin)
    ii,jj = xy_vers_ij(xmin,ymax)
    canvas.create_line(i+4,j,ii+4,jj,fill='black',width=2)
    for x in range(0,xmax+1):
       i,j = xy_vers_ij(x,0)
       canvas.create_line(i,j+5,i,j-5,fill='black',width=2)
       canvas.create_text(i+4,j-15,text=str(x),fill='black')

# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

afficher_axes()

for x,y in bifurcation():
    i,j = xy_vers_ij(x,y)
    afficher_pixel(i,j,'blue')


root.mainloop()


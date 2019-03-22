
##############################
# Lyapunov
##############################


##############################
# Rappels - Activité 1 - Suite logistique
##############################

from math import *

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
    canvas.create_line(i,j,(i+1),j,fill=couleur,width=1)
    return

def afficher_ligne(i,j,ii,jj,couleur):
    canvas.create_line(i,j,ii,jj,fill=couleur,width=1)
    return 


def afficher_axes():
    i,j = xy_vers_ij(xmin,0)
    ii,jj = xy_vers_ij(xmax,0)
    canvas.create_line(i,j,ii,jj,fill='black',width=2)
    i,j = xy_vers_ij(xmin,ymin)
    ii,jj = xy_vers_ij(xmin,ymax)
    canvas.create_line(i+4,j,ii+4,jj,fill='black',width=2)
    for x in range(0,ceil(xmax)+1):
       i,j = xy_vers_ij(x,0)
       canvas.create_line(i,j+5,i,j-5,fill='black',width=2)
       canvas.create_text(i+4,j-15,text=str(x),fill='black')
    for y in range(floor(ymin),ceil(ymax)+1):
       i,j = xy_vers_ij(xmin,y)
       canvas.create_line(i-5,j,i+5,j,fill='black',width=2)
       canvas.create_text(i+15,j+4,text=str(y),fill='black')     

##############################
# Activité 2 - Exposant de Lyapunov
##############################

##############################
## Question 1 ##

def exposant_lyapunov(liste_u,r):
    """ Calcul de l'exposant de Lyapunov d'une suite de termes """
    lyap = 0
    n = len(liste_u)
    for u in liste_u:
        if u != 0.5:
            lyap = lyap + log(abs(r - 2*r*u))
    return lyap/n  

# Test 
print("---Exposant de Lyapunov ---")  
r = 0.5
print("r =",r)
print(exposant_lyapunov(liste_suite(r,0,10),r))
r = 0.5
print("r =",r)
print(exposant_lyapunov(liste_suite(r,100,200),r))
r = 3
print("r =",r)
print(exposant_lyapunov(liste_suite(r,100,200),r))
r = 3.2
print("r =",r)
print(exposant_lyapunov(liste_suite(r,100,200),r))
r = 3.7
print("r =",r)
print(exposant_lyapunov(liste_suite(r,100,200),r))
########################################


##############################
## Question 2 ##

# Constante pour fenêtre réelle et écran
xmin, xmax = 0.1, 4   # pour r
ymin, ymax = -1.3, 1.1  # pour u et l'exposant

Nx = 700   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 


def bifurcation_lyapunov():
    """ Affichage de l'ensemble de bifurcation 
    et du graphe des exposants de Lyapunov """
    Nmin = 600 # On oublie Nmin premiers termes
    Nmax = 1000 # On conserve les termes entre Nmin et Nmax
    u0 = 0.5 # terme initial
    r = xmin
    pasx = (xmax-xmin)/Nx


    for i in range(Nx):
        # 1. La suite pour r fixé
        liste_u = liste_suite(r,Nmin,Nmax) # On calcule la suite
        
        # 2. On affiche les points
        for u in liste_u:
            i,j = xy_vers_ij(r,u)
            afficher_pixel(i,j,'blue')        
        
        # 3. Exposant de Lyapunov
        if i>0:
            old_lyap = lyap
            old_i,old_j = xy_vers_ij(r,old_lyap)
        
        lyap = exposant_lyapunov(liste_u,r)
        i,j = xy_vers_ij(r,lyap)

        if i>0:
            afficher_ligne(old_i,old_j,i,j,'black')        
        
        # 4. On décale r d'un cran
        r = r + pasx

    return




# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

afficher_axes()
bifurcation_lyapunov()

root.mainloop()



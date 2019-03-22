
##############################
# Lyapunov
##############################


##############################
# Rappels - Activité 1 - Suite logistique
##############################

from math import *

def xy_vers_ij(x,y):
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




##############################
# Activité 3 - Fracatale de Lyapunov
##############################

##############################
## Question 1 ##

##############################
# Lettre dans motif

def A_ou_B(motif,n):
    """ Renvoie lettre A ou B selon le rang dans le motif répété """
    p = len(motif)
    lettre = motif[n % p]
    return lettre

# Test
print("--- A ou B d'après motif---")
print(A_ou_B('AB',10))
print(A_ou_B('AAABBB',123))


##############################
## Question 2 ##

# Suite d'après un motif
def liste_suite_motif(r1,r2,motif,Nmin,Nmax):
    """ Suite logistique en choisissant r1 ou r2 
    d'après la lettre A ou B e motif répété """
    # Pour la suite
    u =  0.5
    liste = [u]
    n = 0
   
    while n < Nmax-1:

        # Choix de la lettre
        if A_ou_B(motif,n) == 'A':
            r = r1
        else:
            r = r2

        # Terme de la suite
        u = r*u*(1-u)
        liste += [u]
     
        n += 1
    return liste[Nmin:]

# Test
print("--- Suite logistique suivant un motif ---")
r1, r2 = 0.5, 3.5
motif = 'AB'
print(liste_suite_motif(r1,r2,motif,0,10))


##############################
## Question 3 ##

def exposant_lyapunov_motif(r1,r2,motif,Nmin,Nmax):
    """ Exposant de Lyapunov de la suite logistique suivant un motif """
    # Pour la suite
    u =  0.5
    liste = [u]
    n = 0

    # Pour l'exposant
    lyap = 0
    N = Nmax - Nmin
    
    while n < Nmax-1:

        # Choix de la lettre
        if A_ou_B(motif,n) == 'A':
            r = r1
        else:
            r = r2

        # Terme de la suite
        u = r*u*(1-u)
        liste += [u]

        # Terme de l'exposant
        if u != 0.5:
            lyap = lyap + log(abs(r - 2*r*u))
     
        n += 1
    return lyap/N

# Test
print("--- Exposant de Lyapunov d'une suite suivant un motif ---")
r1, r2 = 0.5, 3.5
motif = 'AB'
print(exposant_lyapunov_motif(r1,r2,motif,0,10))
print(exposant_lyapunov_motif(r1,r2,motif,100,200))

##############################
## Question 4 ##


##############################
# Choix d'une couleur

def choix_couleur(l):
    """ Choix d'une couleur selon un entier """
    i = round(150*l)

    R,V,B = i,0,0            # Nuances de rouge
    # R,V,B = 255-i,255-i,255-i   # Pour impression n&b

    couleur = '#%02x%02x%02x' % (R%256, V%256, B%256)

    return couleur

# Constante pour fenêtre réelle et écran
xmin, xmax = 2, 3  # pour r1
ymin, ymax = 3, 4  # pour r2

Nx = 201   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 


def fractale_lyapunov(motif):
    """ Affichage de la fractale de Lyapunov suivant un motif
    Motif de base 'AB' """
    
    Nmin = 200 # On oublie Nmin premiers termes
    Nmax = 300 # On conserve les termes entre Nmin et Nmax
    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny


    r1 = xmin
    for i in range(Nx):
        r2 = ymin
        for j in range(Ny):
           
            # 1. Exposant de Lyapunov
            lyap = exposant_lyapunov_motif(r1,r2,motif,Nmin,Nmax)

            # 2. Choix d'une couleur
            couleur = choix_couleur(lyap) 

            # 3. On affiche le point
            afficher_pixel(i,j,couleur)        
        
      
            r2 = r2 + pasy
        r1 = r1 + pasx

    return



# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

motif = 'AB'
# motif = 'BBBBBBAAAAAA'
fractale_lyapunov(motif)

root.mainloop()



##############################
# Lyapunov
##############################


##############################
# Activité 1 - Suite logistique
##############################

from math import *

def f(x,r):
    return r*x*(1-x)


def liste_suite(u0,r,Nmin,Nmax):
    liste = [u0]
    k = 0
    u =  u0
    while k < Nmax-1:
        u = f(u,r)
        liste += [u]
        k += 1
    return liste[Nmin:]

# Test
# print(liste_suite(0.5,1,0,10))
# print(liste_suite(0.5,1,5,10))



def bifurcation():
    Nmin = 100 # On oublie Nmin premiers termes
    Nmax = 200 # On conserve les termes entre Nmin et Nmax
    epsilon = 0.05 # On fait varier r de epsilon à chaque pas
    u0 = 0.5 # terme initial
    r = 0 # r initial
    mespoints = []

    while r <= 4.0:
        liste_u = liste_suite(u0,r,Nmin,Nmax) # On calcule la suite
        for u in liste_u:
            mespoints = mespoints + [(r,u)]
        r = r + epsilon

    return mespoints

# Constante pour fenêtre réelle et écran
xmin, xmax = 0, 4
ymin, ymax = -2, 1

Nx = 600   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 


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

def afficher_ligne(i,j,ii,jj,couleur):
    canvas.create_line(i,j,ii,jj,fill=couleur,width=1)
    return    


# Fenêtre tkinter
# from tkinter import *
# root = Tk()      
# canvas = Canvas(root, width=Nx, height=Ny, background="white")
# canvas.pack(side=LEFT, padx=5, pady=5)

# for x,y in bifurcation():
#     i,j = xy_vers_ij(x,y)
#     afficher_pixel(i,j,'blue')

# root.mainloop()





##############################
# Activité 2 - Exposant de Lyapunov
##############################




def exposant_lyapunov(liste_u,r):
    lyap = 0
    n = len(liste_u)
    for u in liste_u:
        if (u!= 0) and (u != 0.5):
            lyap = lyap + log(abs(r - 2*r*u))
    return lyap/n  

# Test    
# r = 1.5
# print(exposant_lyapunov(liste_suite(0.5,r,100,200),r))


########################################


# Constante pour fenêtre réelle et écran
xmin, xmax = 2.5, 4   # pour r
ymin, ymax = -2, 1  # pour u et l'exposant

Nx = 1200   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 


def bifurcation_lyapunov():
    Nmin = 100 # On oublie Nmin premiers termes
    Nmax = 200 # On conserve les termes entre Nmin et Nmax
    u0 = 0.5 # terme initial
    r = xmin
    pasx = (xmax-xmin)/Nx


    for i in range(Nx):
        # 1. La suite pour r fixé
        liste_u = liste_suite(u0,r,Nmin,Nmax) # On calcule la suite
        
        # 2. On affiche les points
        for u in liste_u:
            i,j = xy_vers_ij(r,u)
            afficher_pixel(i,j,'red')        
        
        # 3. Exposant de Lyapunov
        if i>0:
            old_lyap = lyap
            old_i,old_j = xy_vers_ij(r,old_lyap)
        
        lyap = exposant_lyapunov(liste_u,r)
        i,j = xy_vers_ij(r,lyap)

        if i>0:
            afficher_ligne(old_i,old_j,i,j,'blue')        
        
        # 4. On décale r d'un cran
        r = r + pasx

    return




# Fenêtre tkinter
# from tkinter import *
# root = Tk()      
# canvas = Canvas(root, width=Nx, height=Ny, background="white")
# canvas.pack(side=LEFT, padx=5, pady=5)

# bifurcation_lyapunov()

# root.mainloop()


##############################
# Activité 3 - Fracatale de Lyapunov
##############################


##############################
# Lettre dans motif

def A_ou_B(motif,k):
    n = len(motif)
    lettre = motif[k % n]
    return lettre

# Test
# print(A_ou_B('AB',11))


##############################
# Lettre dans motif
def liste__suite_motif(u0,r1,r2,motif,Nmin,Nmax):
    # Pour la suite
    liste = [u0]
    k = 0
    u =  u0
   
    while k < Nmax-1:

        # Choix de la lettre
        if A_ou_B(motif,k) == 'A':
            r = r1
        else:
            r = r2

        # Terme de la suite
        u = f(u,r)
        liste += [u]
     
        k += 1
    return liste[Nmin:]

##############################
# Lettre dans motif

def exposant_lyapunov_motif(u0,r1,r2,motif,Nmin,Nmax):
    # Pour la suite
    liste = [u0]
    k = 0
    u =  u0

    # Pour l'exposant
    lyap = 0
    n = Nmax - Nmin
    
    while k < Nmax-1:

        # Choix de la lettre
        if A_ou_B(motif,k) == 'A':
            r = r1
        else:
            r = r2

        # Terme de la suite
        u = f(u,r)
        liste += [u]

        # Terme de l'exposant
        if (u!= 0) and (u != 0.5):
            lyap = lyap + log(abs(r - 2*r*u))
     
        k += 1
    return lyap/n


##############################
# Choix d'une couleur

def choix_couleur(l):

    i = round(150*l)

    R,V,B = i,0,00            # Nuances de rouge
    # R,V,B = 255-i,255,255            # Pour impression n&b

    couleur = '#%02x%02x%02x' % (R%256, V%256, B%256)

    return couleur

# Constante pour fenêtre réelle et écran
xmin, xmax = 0, 4   # pour r1
ymin, ymax = 0, 4  # pour r2

Nx = 201   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 


def fractale_lyapunov(motif):
    Nmin = 100 # On oublie Nmin premiers termes
    Nmax = 200 # On conserve les termes entre Nmin et Nmax
    u0 = 0.5 # terme initial
    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny


    r1 = xmin
    for i in range(Nx):
        r2 = ymin
        for j in range(Ny):
           
            # 1. Exposant de Lyapunov
            lyap = exposant_lyapunov_motif(u0,r1,r2,motif,Nmin,Nmax)

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
fractale_lyapunov(motif)

root.mainloop()


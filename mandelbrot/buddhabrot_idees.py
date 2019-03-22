
##############################
# Mandelbrot
##############################

from math import *

##############################
# Activité  - Buddhabrot
##############################

##############################
## Question 1 ##

def iterer(c,Max_iter=100):
    z = 0
    i = 1
    liste_z = []
    while (i < Max_iter) and (abs(z) <= 2):
        z = z**z + c
        liste_z = liste_z + [z] 
        i = i + 1

    if i >= Max_iter:       # La suite converge
        return 0, []        # On oublie les points parcourus
    else:                   # La suite s'échappe à partir du rang i
        return i, liste_z   # On renvoie tous les points parcourus


# print(iterer(0.33+0.2j))
# print(iterer(-2.2-1.2j,Max_iter=4))


##############################
## Question 2 ##

def choix_couleur(i):
    R = i%256
    coul = '#%02x%02x%02x' % (R, R, R)
    return coul

##############################
def afficher_pixel(i,j,couleur):
    canvas.create_line(i,j,(i+1),(j+1),fill=couleur,width=1)
    return


##############################
## Question 3 ##

def buddhabrot(xmin,xmax,ymin,ymax,NN=400,Max_iter=100,pas=1):

    Nx = NN  # Nb de pixel pour les x
    Ny = round( (ymin-ymax)/(xmin-xmax) * NN )

    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny

    a = xmin
    b = ymin

    buddha = [[0 for j in range(Ny)] for i in range(Nx)]

    # Calcul des parcours pour certains points
    for i in range(0,Nx,pas):
        for j in range(0,Ny,pas):

            c = a+b*1j  # c = complex(a,b)

            vitesse,liste_z = iterer(c,Max_iter)

            # print(i,j,liste_z)

            for z in liste_z:
                x, y = z.real, z.imag
                ii = floor( (x-xmin)/pasx )
                jj = floor( (y-ymin)/pasy )
                
                if (0 <= ii < Nx) and (0 <= jj < Ny):
                    buddha[ii][jj] += 1 

            b = b + pasy

        b  = ymin
        a = a + pasx

    # Une couleur pour chaque point en fonction 
    # du nb de fois où il est atteint
    max_atteint = 0
    for i in range(Nx):
        for j in range(Ny):
            atteint = buddha[i][j]
            if atteint > 1:
                couleur = choix_couleur(40*atteint)
            else:
                couleur = choix_couleur(0)
            afficher_pixel(i,j,couleur)
    # print(buddha)   
    print(max_atteint)
    return

##############################

xmin, xmax = -2.2, 1
ymin, ymax = -1.2, 1.2


Max_iter = 100 

NN = 600

Nx = NN  # Nb de pixel pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * NN ) 

# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

buddhabrot(xmin,xmax,ymin,ymax,NN=NN,Max_iter=Max_iter,pas=1)

root.mainloop()
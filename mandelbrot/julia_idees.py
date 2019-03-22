
##############################
# Mandelbrot
##############################


# A faire :
# * avec complex z <- z^2 + c
# * Julia
# * Buddhabrot


##############################
# Activité 1 - Mandelbrot
##############################

##############################
## Question 1 ##


def f(z,c):   
    """ z <- z^2 + c """
    zz = z*z + c
    return zz



##############################
## Question 2 ##


def iterer(z0,c,Max_iter=100):
    z = z0
    i = 1
    while (i < Max_iter) and (abs(z) <= 2):
        z = f(z,c)
        i = i + 1

    if i >= Max_iter: # La suite converge
        return 0
    else:           # La suite s'échappe à partir du rang i
        return i


##############################
## Question 3 ##

def choix_couleur(i):
    if i == 0:
        R,V,B = 0,0,0
    else: 
        R,V,B = 50 + 2*i,0,0

    coul = '#%02x%02x%02x' % (R, V, B)

    return coul


##############################
def afficher_pixel(i,j,couleur):
    #canvas.create_rectangle(i*taille,j*taille,(i+1)*taille,(j+1)*taille,outline=couleur,fill=couleur)
    canvas.create_line(i,j,(i+1),(j+1),fill=couleur,width=1)
    return


##############################
## Question 4 ##




def julia(c,xmin,xmax,ymin,ymax,NN=400,Max_iter=100):

    Nx = NN  # Nb de pixel pour les x
    Ny = round( (ymin-ymax)/(xmin-xmax) * NN )

    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny

    a = xmin
    b = ymin

    for i in range(Nx):
        for j in range(Ny):
            z = complex(a,b)
            vitesse = iterer(z,c,Max_iter)
            couleur = choix_couleur(vitesse)
            afficher_pixel(i,j,couleur)
            b = b + pasy

        b  = ymin
        a = a + pasx
        
    return

##############################

xmin, xmax = -1.5, 1.5
ymin, ymax = -1.5, 1.5


Max_iter = 100 

NN = 400

Nx = NN  # Nb de pixel pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * NN ) 

# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# c = complex(0.3,0.55)   
c = 0.3+0.55j 
julia(c,xmin,xmax,ymin,ymax,NN=NN)


root.mainloop()

##############################
# Mandelbrot(version réelle)
##############################


##############################
# Activité 1 - Mandelbrot (version complexe)
##############################

##############################
## Question 1 ##

def f(z,c):   
    """ z <- z^2 + c """
    return z*z + c


##############################
## Question 2 ##

Max_iter = 100


def iterer(c):
    """ Calcul du nb d'itérations avant que la suite 
    ne s'échappe à l'infini. 
    C'est la répétition de cette opération qui prend beaucoup de temps """

    z = 0     # Point initial
    i = 1
    while (i < Max_iter) and (abs(z) <= 2):
        z = f(z,c)
        i = i + 1

    if i >= Max_iter: # La suite converge
        return 0
    else:             # La suite s'échappe à partir du rang i
        return i

# Test
# print(iterer(1.5+1.5j))


##############################
## Question 3 ##

##############################
# Allumer un pixel

def afficher_pixel(i,j,couleur):
    canvas.create_line(i,j,(i+1),(j+1),fill=couleur,width=1)
    return


##############################
# Choix d'une couleur

def choix_couleur(i):
    """ Choix d'une couleur en fonction de la vitesse i d'échapemment """
    if i == 0:
        R,V,B = 0,0,0
    else: 
        R,V,B = 50 + 2*i,0,0

    couleur = '#%02x%02x%02x' % (R, V, B)

    return couleur


##############################
# Fenêtre 

xmin, xmax = -2.2, 1
ymin, ymax = -1.2, 1.2

Nx = 400   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 


##############################
## Question 4 ##

def mandelbrot():
    """ Fonction principale : affichage pixel par pixel
    de l'ensemble de Mandelbrot dans la fenêtre demandée """
    
    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny

    a = xmin
    b = ymin

    for i in range(Nx):
        for j in range(Ny):
            c = a + b*1j
            vitesse = iterer(c)
            couleur = choix_couleur(vitesse)
            afficher_pixel(i,j,couleur)
            b = b + pasy

        b  = ymin
        a = a + pasx
        
    return

##############################



# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

mandelbrot()

root.mainloop()
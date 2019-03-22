
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


def f(x,y,a,b):   
    """ z <- z^2 + c """

    xx = x*x - y*y + a
    yy = 2*x*y + b

    return xx, yy



##############################
## Question 2 ##


def iterer_1(a,b,Max_iter=100):
    x, y = 0, 0
    i = 1
    while (i < Max_iter) and (x*x + y*y <= 4):
        x, y = f(x,y,a,b)
        i = i + 1

    if i >= Max_iter: # La suite converge
        return 0
    else:           # La suite s'échappe à partir du rang i
        return i

# Test
# print(iterer(1.5,1.5))



##############################
## Question 2 (optimisé) ##

Max_iter = 50

def iterer_2(a,b,Max_iter=100):
    x, y = 0, 0
    x2, y2 = x*x, y*y
    i = 1
    while (i < Max_iter) and (x2 + y2 <= 4):
        x, y = x2 - y2 + a, (x+y)*(x+y) - x2-y2 + b
        x2, y2 = x*x, y*y
        i = i + 1

    if i >= Max_iter: # La suite converge
        return 0
    else:           # La suite s'échappe à partir du rang i
        return i

# Test
# print(iterer(1.5,1.5))

def iterer(a,b,Max_iter=100):
    return iterer_2(a,b,Max_iter)

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




def mandelbrot(xmin,xmax,ymin,ymax,NN=400,Max_iter=100):

    Nx = NN  # Nb de pixel pour les x
    Ny = round( (ymin-ymax)/(xmin-xmax) * NN )

    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny

    a = xmin
    b = ymin

    for i in range(Nx):
        for j in range(Ny):
            vitesse = iterer(a,b,Max_iter)
            couleur = choix_couleur(vitesse)
            afficher_pixel(i,j,couleur)
            b = b + pasy

        b  = ymin
        a = a + pasx
        
    return

##############################

xmin, xmax = -2.2, 1
ymin, ymax = -1.2, 1.2


Max_iter = 100 

NN = 400

Nx = NN  # Nb de pixel pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * NN ) 

# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

mandelbrot(xmin,xmax,ymin,ymax)

# mandelbrot(0.3,0.5,0.3,0.5,NN=NN)

root.mainloop()
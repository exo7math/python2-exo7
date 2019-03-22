
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

    xx = x*x - y*y + a
    yy = 2*x*y + b

    return xx, yy



##############################


def iterer(x0,y0,a,b,Max_iter=100):
    x, y = x0, y0
    i = 1
    while (i < Max_iter) and (x*x + y*y <= 4):
        x,y = f(x,y,a,b)
        i = i + 1

    if i >= Max_iter: # La suite converge
        return 0
    else:           # La suite s'échappe à partir du rang i
        return i


##############################

def choix_couleur(i):
    if (i ==0):
        R,V,B = 0,0,0
    else: 
        # R,V,B = 50 + 2*i,0,0
        # R,V,B = 255-2*i,255-2*i,255-2*i           # Pour impression n&b
        R,V,B = 255-2*i,255,255    # Couleurs
        #R,V,B = 50+2*i,50+2*i,50+2*i  # Gris
    coul = '#%02x%02x%02x' % (R, V, B)

    return coul


##############################
def afficher_pixel(i,j,couleur):
    #canvas.create_rectangle(i*taille,j*taille,(i+1)*taille,(j+1)*taille,outline=couleur,fill=couleur)
    canvas.create_line(i,j,(i+1),(j+1),fill=couleur,width=1)
    return



##############################
# Fenêtre 


xmin, xmax = -2, 2 
ymin, ymax = -1.5, 1.5


Nx = 800   # Nb de pixels pour les x
Ny = round( (ymin-ymax)/(xmin-xmax) * Nx ) 

def julia(cx,cy):

    pasx = (xmax-xmin)/Nx
    pasy = (ymax-ymin)/Ny

    x0 = xmin
    y0 = ymin

    for i in range(Nx):
        for j in range(Ny):
            vitesse = iterer(x0,y0,a,b,Max_iter)
            couleur = choix_couleur(vitesse)
            afficher_pixel(i,j,couleur)
            y0 = y0 + pasy

        y0  = ymin
        x0 = x0 + pasx
        
    return

##############################

Max_iter = 100 

# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=Nx, height=Ny, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# c = complex(0.3,0.55)  

# Julia 1
# xmin, xmax = -1.5, 1.5 
# ymin, ymax = -1.5, 1.5
# a, b = 0.3, 0.55

# Julia 2
# xmin, xmax = -0.25, 0.25 
# ymin, ymax = -0.75, -0.25
# a, b = 0.3, 0.55

# Julia 3
# xmin, xmax = -2, 2 
# ymin, ymax = -1, 1
a, b = -1.31, 0

# Julia 4
# a, b = -0.101, 0.956

julia(a,b)


root.mainloop()

##############################
# Mandelbrot
##############################


##############################
# Activité 2 - Mandelbrot (version réelle)
##############################

##############################
## Question 1 ##

def f(x,y,a,b):   

    xx = x*x - y*y + a
    yy = 2*x*y + b

    return xx, yy


##############################
## Question 2 ##

Max_iter = 100

def iterer(a,b):
    """ Calcul du nb d'itérations avant que la suite 
    ne s'échappe à l'infini. 
    C'est la répétition de cette opération qui prend beaucoup de temps """

    x, y = 0, 0  # Point initial
    i = 1
    while (i < Max_iter) and (x*x + y*y <= 4):
        x, y = f(x,y,a,b)
        i = i + 1

    if i >= Max_iter: # La suite converge
        return 0
    else:             # La suite s'échappe à partir du rang i
        return i

# Test
# print(iterer(1.5,1.5))



##############################
## Question 5  ##


def iterer_opt(a,b):
    """ Version un peu optimisée de iterer() """

    x, y = 0, 0   # Point initial
    x2, y2 = x*x, y*y    # Carrés

    i = 1
    while (i < Max_iter) and (x2 + y2 <= 4):
        x, y = x2 - y2 + a, (x+y)*(x+y) - x2-y2 + b
        x2, y2 = x*x, y*y
        i = i + 1

    if i >= Max_iter: # La suite converge
        return 0
    else:             # La suite s'échappe à partir du rang i
        return i

# Test
# print(iterer_opt(1.5,1.5))


##############################
## Question 3 ##

##############################
# Allumer un pixel

def afficher_pixel(i,j,couleur):
    canvas.create_line(i,j,(i+1),j,fill=couleur,width=1)
    return


##############################
# Choix d'une couleur

def choix_couleur(i):
    """ Choix d'une couleur en fonction de la vitesse i d'échapemment """    
    if i == 0:
        R,V,B = 0,0,0
    else: 
        R,V,B = 50+2*i,0,00            # Nuances de rouge
        R,V,B = 255-3*i,255,255            # Pour impression n&b
        # R,V,B = 50+2*i,150+i,100-i    # Couleurs
        # R,V,B = 50+2*i,50+2*i,50+2*i  # Gris

    couleur = '#%02x%02x%02x' % (R%256, V%256, B%256)

    return couleur




##############################
# Fenêtre 

# Tout Mandelbrot
xmin, xmax = -2.2, 1
ymin, ymax = -1.2, 1.2

# Petit zoom
# xmin, xmax = 0.3, 0.5
# ymin, ymax = 0.3, 0.45

# Moyen zoom
# xmin, xmax = 0.4414, 0.4418
# ymin, ymax = 0.3765, 0.3768
# Max_iter = 200

Nx = 1200   # Nb de pixels pour les x
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
            vitesse = iterer(a,b)
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
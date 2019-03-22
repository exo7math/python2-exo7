
##############################
# Complexes II
##############################


from math import *

##############################
# Rappels

def polaire_vers_cartesien(module,argument):
    x = module*cos(argument)
    y = module*sin(argument)
    z = x + 1j*y
    return z

def cartesien_vers_polaire(z):
    x = z.real
    y = z.imag
    print(x)
    print(y)   
    module = sqrt(x**2 + y**2)
    argument = atan2(y,x)
    return (module,argument)


##############################
# Activité 4 - Cercles et droites 
##############################

import matplotlib.pyplot as plt


##############################
## Question 1 ##

def affiche_liste(zliste,couleur='blue',taille=10):
    """ Trace des points à partir d'une liste d'affixes """
    for z in zliste:
        x = z.real
        y = z.imag
        plt.scatter(x,y,color=couleur,s=taille)
    return


##############################
## Question 2 ##

def trace_cercle(z0,r,numpoints=100):
    """ Trace (les points d') un cercle à partir d'un centre et un rayon """
    zliste = []
    for k in range(numpoints):
        theta = 2*pi*k/numpoints
        z = z0 + polaire_vers_cartesien(r,theta)
        zliste.append(z)
    return zliste


##############################
## Question 3 ##

def trace_segment(z0,z1,numpoints=100):
    """ Trace (les points d') un segemnt entre deux points donnés """
    zliste = []
    for k in range(numpoints):
        t = k/numpoints
        z = (1-t)*z0+t*z1
        zliste.append(z)
    return zliste


# Test
plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y

zliste = trace_cercle(2+3j,sqrt(2))
affiche_liste(zliste)

zliste = trace_segment(-2-1j,-1+3j)
affiche_liste(zliste)

plt.show()


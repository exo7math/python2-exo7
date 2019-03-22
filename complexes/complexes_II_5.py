
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
# Rappels - Activité 4 
##############################

import matplotlib.pyplot as plt


##############################
## Question 1 ##

def affiche_liste(zliste,couleur='blue',taille=10):
    for z in zliste:
        x = z.real
        y = z.imag
        plt.scatter(x,y,color=couleur,s=taille)
    return


##############################
## Question 2 ##

def trace_cercle(z0,r,numpoints=100):
    zliste = []
    for k in range(numpoints):
        theta = 2*pi*k/numpoints
        z = z0 + polaire_vers_cartesien(r,theta)
        zliste.append(z)
    return zliste


##############################
## Question 3 ##

def trace_segment(z0,z1,numpoints=100):
    zliste = []
    for k in range(numpoints):
        t = k/numpoints
        z = (1-t)*z0+t*z1
        zliste.append(z)
    return zliste



##############################
# Activité 5 - Transformations complexes
##############################

##############################
## Question 1 ##

def translation(zliste,v):
    """ Ajoute v à chaque complexe z de la liste """
    new_zliste = []
    for z in zliste:
        new_zliste.append(z+v) 
    return new_zliste


def homothetie(zliste,k):
    """ Multiplie chaque complexe z de la liste par k """
    new_zliste = []
    for z in zliste:
        new_zliste.append(k*z) 
    return new_zliste    


def rotation(zliste,theta):
    """ Multiplie chaque complexe z de la liste par exp(i theta) """
    new_zliste = []
    for z in zliste:
        w = polaire_vers_cartesien(1,theta)    
        new_zliste.append(z*w) 
    return new_zliste    

def symetrie(zliste):
    """ Chaque z est conjugué """
    new_zliste = []
    for z in zliste:
        new_zliste.append(z.conjugate()) 
    return new_zliste   
  


##############################
## Question 2 ##

cercle = trace_cercle(2+2j,1)
carre = trace_segment(0,1) + trace_segment(1,1+1j) + trace_segment(1+1j,1j) + trace_segment(1j,0)
ensemble = cercle + carre
ensemble_transforme = translation(ensemble,2-1j)
ensemble_transforme = homothetie(ensemble,1.5)
ensemble_transforme = symetrie(ensemble)
ensemble_transforme = rotation(ensemble,pi/3)

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

affiche_liste(ensemble,couleur="blue")
affiche_liste(ensemble_transforme,couleur="red")

# plt.show()


##############################
## Question 3 ##


def inversion(zliste):
    """ Chaque z devient 1/z """
    new_zliste = []
    for z in zliste:
        if z != 0:
            new_zliste.append(1/z.conjugate()) 
    return new_zliste  

# Cercles et droites
cercle = trace_cercle(-2+1.5j,1)
carre = trace_segment(1+0.5j,2+0.5j) + trace_segment(2+0.5j,2+1.5j) + trace_segment(2+1.5j,1+1.5j) + trace_segment(1+1.5j,1+0.5j)
ensemble = cercle + carre
ensemble_transforme = inversion(ensemble)

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

affiche_liste(ensemble,couleur="blue")
affiche_liste(ensemble_transforme,couleur="red")

# plt.show()


# Grille
# n = 5
# lignes_verticales = []
# lignes_horizontales = []
# for k in range(1,n):
#     lignes_verticales += trace_segment(k/2-n*1j,k/2+n*1j,numpoints=50)
#     lignes_horizontales += trace_segment(-n+k/2*1j,n+k/2*1j,numpoints=50)

# ensemble = lignes_verticales + lignes_horizontales
# ensemble_transforme = inversion(ensemble)

# plt.clf()
# plt.axes().set_aspect('equal')
# plt.axhline(y=0, color='r', linestyle='-')
# plt.axvline(x=0, color='r', linestyle='-')

# affiche_liste(ensemble,couleur="blue",taille=5)
# affiche_liste(ensemble_transforme,couleur="red",taille=1)

# plt.show()

##############################
## Question 4 ##

def au_carre(zliste):
    """ Chaque z devient z^2 """
    new_zliste = []
    for z in zliste:
        new_zliste.append(z**2) 
    return new_zliste  

# Cercles et droites
cercle = trace_cercle(2+1j,1.5)
carre = trace_segment(1+0.5j,2+0.5j) + trace_segment(2+0.5j,2+1.5j) + trace_segment(2+1.5j,1+1.5j) + trace_segment(1+1.5j,1+0.5j)
ensemble = cercle + carre
ensemble_transforme = au_carre(ensemble)

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

affiche_liste(ensemble,couleur="blue")
affiche_liste(ensemble_transforme,couleur="red")

plt.show()


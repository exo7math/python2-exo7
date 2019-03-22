
##############################
# Complexes II
##############################

##############################
# Activité 1 - Module/argument
##############################

##############################
## Question 1 ##

import cmath  # ne pas faire "from cmath import *" car conflit sqrt
from math import *

z = 1+3j

module = abs(z)
argument = cmath.phase(z)

print("Module :", module)
print("Argument :", argument)

# z = complex(1+1j)
z = 1+1j
print("Module, Argument :", cmath.polar(z))

##############################
## Question 2 ##

z = cmath.rect(2,pi/3)
print(z)

z = cmath.rect(3,5*pi/6)
print(z)


##############################
## Question 3 ##

import matplotlib.pyplot as plt

plt.clf()  # Efface tout
plt.axes().set_aspect('equal')  # Repère orthonormé
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y


z = cmath.rect(2,pi/3)
x = z.real
y = z.imag

plt.scatter(x,y,color='red',s=100)
plt.scatter(0,0,color='red',s=100)

# plt.show()

##############################
## Question 4 ##

def dessine_polygone(n):
    omega = cmath.rect(1,2*pi/n)
    listex = []
    listey = []
    for k in range(n):
        z = omega ** k
        x = z.real
        y = z.imag
        plt.scatter(x,y,color='blue',s=100)
        listex.append(x)
        listey.append(y)
    listex.append(listex[0])
    listey.append(listey[0])    
    plt.plot(listex,listey,color='black')
    return

plt.clf()  # Efface tout
plt.axes().set_aspect('equal')  # Repère orthonormé
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y

# dessine_polygone(5)

# plt.show()


##############################
# Activité 2 - Passage polaire/cartésienne
##############################

##############################
## Question 1 ##

def polaire_vers_cartesien(module,argument):
    x = module*cos(argument)
    y = module*sin(argument)
    z = x + 1j*y
    return z

# Test
print("--- Polaire vers cartésien ---")
z1 = polaire_vers_cartesien(3,pi/6)
z2 = cmath.rect(3,pi/6)
print(z1)
print(z2)

##############################
## Question 2 ##

def cartesien_vers_polaire(z):
    x = z.real
    y = z.imag
    print(x)
    print(y)   
    module = sqrt(x**2 + y**2)
    argument = atan2(y,x)
    return (module,argument)

# Test
print("--- Cartésien vers polaire ---")
mod_arg_1 = cartesien_vers_polaire(-2+5j)
mod_arg_2 = cmath.polar(-2+5j)
print(mod_arg_1)
print(mod_arg_2)


##############################
## Question 3 ##

def argument_dans_intervalle(angle):
    k = floor(angle/(2*pi))
    print(k)
    new_angle = angle - 2*k*pi
    if new_angle > pi:
        new_angle += -2*pi
    return new_angle

# Test
print("--- Argument dans intervalle ---")
print(argument_dans_intervalle(-pi/2+12*pi))



##############################
# Activité 3 - Formule d'Euler / de Moivre / Gauss
##############################

##############################
## Question 1 ##

def cosinus(t):
    eplus = polaire_vers_cartesien(1,t)
    emoins = polaire_vers_cartesien(1,-t)
    cos_complexe = (eplus+emoins)/2
    cos_reel = cos_complexe.real
    return cos_reel


def sinus(t):
    eplus = polaire_vers_cartesien(1,t)
    emoins = polaire_vers_cartesien(1,-t)
    sin_complexe = (eplus-emoins)/(2*1j)
    sin_reel = sin_complexe.real
    return sin_reel    

# Test
print("--- Formules d'Euler ---")

t = pi/6
print(cosinus(t))
print(cos(t))
print(sinus(t))
print(sin(t))


##############################
## Question 2 ##

def puissance_bis(z,n):
    r,theta = cartesien_vers_polaire(z)
    r_n = r ** n
    theta_n = n*theta
    z_n = polaire_vers_cartesien(r_n,theta_n)
    return z_n

# Test
print("--- Formule de De Moivre ---")
z = 2-3j
n = 10
print(puissance_bis(z,n))
print(z**n)


##############################
## Question 3 ##

def multiplication(a,b,c,d):
    return (a*c-b*d,a*d+b*c)

def multiplication_bis(a,b,c,d):
    r = a*c
    s = b*d
    t = (a+b)*(c+d)
    return r-s, t-r-s

def multiplication_ter(a,b,c,d):
    r = c*(a+b)
    s = a*(d-c)
    t = b*(c+d)
    return r-t, r+s

# Test
print("--- Formules de Gauss ---")
print(multiplication(2,5,3,-2))
print(multiplication_bis(2,5,3,-2))
print(multiplication_ter(2,5,3,-2))



##############################
# Activité 4 - Cercles et droites 
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


# Test
plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y

zliste = trace_cercle(2+3j,sqrt(2))
affiche_liste(zliste)

zliste = trace_segment(-2-1j,-1+3j)
affiche_liste(zliste)

# plt.show()



##############################
# Activité 4 - Transformations complexes
##############################

##############################
## Question 1 ##

def translation(zliste,v):
    new_zliste = []
    for z in zliste:
        new_zliste.append(z+v) 
    return new_zliste


def homothetie(zliste,k):
    new_zliste = []
    for z in zliste:
        new_zliste.append(k*z) 
    return new_zliste    


def rotation(zliste,theta):
    new_zliste = []
    for z in zliste:
        w = polaire_vers_cartesien(1,theta)    
        new_zliste.append(z*w) 
    return new_zliste    

def symetrie(zliste):
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



##############################
# Complexes I
##############################


##############################
# Rappels activité 1
##############################

def addition(a,b,aa,bb):
    return (a+aa,b+bb)

def multiplication(a,b,aa,bb):
    return (a*aa-b*bb,a*bb+b*aa)

def conjugue(a,b):
    return (a,-b)

def module(a,b):
    return sqrt(a**2 + b**2)
    
def inverse(a,b):
    if a != 0 and b !=0:
        r2 = a**2 + b**2
        return (a/r2,-b/r2)
    else:
        return None

def puissance(a,b,n):
    if n == 0:
        return (1,0)
    aa = a
    bb = b
    for __ in range(n):
        aa,bb = multiplication(a,b,aa,bb)
    return (aa,bb)


##############################
##############################
# Cours : visualisation

import matplotlib.pyplot as plt

plt.clf()  # Efface tout
plt.axes().set_aspect('equal')  # Repère orthonormé
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y

x = 2
y = 1

plt.scatter(x,y,color='blue',s=80)  # Un point
# plt.show()  # Lancement de la fenêtre

##############################
# Activité 2 - Visualisation
##############################

from math import *

import matplotlib.pyplot as plt

##############################
## Question 1 ##

# fig,ax = plt.subplots()
z = -2+3j
x = z.real
y = z.imag

plt.clf() # Efface tout
plt.axes().set_aspect('equal') # Repère orthonormé
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y

plt.scatter(x,y,color='red',s=20)
plt.scatter(1,0,color='green',s=20)
plt.scatter(0,1,color='blue',s=20)

# plt.show()

##############################
## Question 2 ##

z0 = 3-2j
x0 = z0.real
y0 = z0.imag

x1,y1 = multiplication(x0,y0,2,0)
x2,y2 = multiplication(x0,y0,0,-1)

xx3,yy3 = puissance(x0,y0,2)
r = module(x0,y0)
x3,y3 = xx3/r, yy3/r

x4,y4 = conjugue(x0,y0)
x5,y5 = inverse(x0,y0)

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

plt.scatter(x0,y0,color='red',s=20)
plt.scatter(x1,y1,color='green',s=20)
plt.scatter(x2,y2,color='blue',s=20)
plt.scatter(x3,y3,color='brown',s=20)
plt.scatter(x4,y4,color='orange',s=20)
plt.scatter(x5,y5,color='purple',s=20)

# plt.show()


##############################
## Question 3 ##

def affiche_triangle(z1,z2,z3):
    """ Trace un triangle à partir des affixes donnés """
    x1,y1 = z1.real,z1.imag
    x2,y2 = z2.real,z2.imag
    x3,y3 = z3.real,z3.imag

    plt.scatter(x1,y1,color='red',s=50)
    plt.scatter(x2,y2,color='green',s=50)
    plt.scatter(x3,y3,color='blue',s=50)    

    plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],color='black')

    return

plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

# Test
# affiche_triangle(2+1j,1-1j,-2+1.5j)

z = 1+2j
# affiche_triangle(z,2*z,(1+2j)*z)  # Triangle rectangle

z = 1+2j
omega = -1/2+sqrt(3)/2*1j
affiche_triangle(z,omega*z,omega*omega*z)  # Triangle isocèle

plt.show()



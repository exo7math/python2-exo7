
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
print("z =",z)

z = cmath.rect(3,5*pi/6)
print("z = ",z)


##############################
## Question 3 ##

import matplotlib.pyplot as plt

plt.clf()  # Efface tout
plt.axes().set_aspect('equal')  # Repère orthonormé
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y


z = cmath.rect(sqrt(2),pi/6)
x = z.real
y = z.imag

plt.scatter(x,y,color='red',s=100)

plt.show()


##############################
## Question 4 ##

def dessine_polygone(n):
    """ Trace un polygone régulier à n côtés 
    en utilisant les nombres complexes """

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

dessine_polygone(5)

plt.show()


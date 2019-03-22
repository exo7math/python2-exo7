
##############################
# Complexes I
##############################

##############################
# Rappels 
##############################

from math import *

def solution_trinome(a,b,c):
    """ Solutions de ax^2 + bx + c = 0 avec a,b,c réels """

    Delta = b**2 - 4*a*c

    if Delta == 0:
        sol = [-b/(2*a),-b/(2*a)]

    if Delta > 0:
        d = sqrt(Delta)
        sol = [(-b-d)/(2*a), (-b+d)/(2*a)]

    if Delta < 0:
        d = 1j*sqrt(-Delta)
        sol = [(-b-d)/(2*a), (-b+d)/(2*a)]

    return sol

##############################
# Activité 5 - Famille de racines
##############################

import matplotlib.pyplot as plt

##############################
## Question 1 ##

def affiche_racines(a,b,c,couleur='red'):
    """ Trace les solutions d'une équation du second degré """
    z1,z2 = solution_trinome(a,b,c)     
    x,y = z1.real, z1.imag
    plt.scatter(x,y,color=couleur,s=40) 
    x,y = z2.real, z2.imag
    plt.scatter(x,y,color=couleur,s=40)
    return

# Test
print("--- Test affiche racines ---")
plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

sol = solution_trinome(1,-2,1)  
affiche_racines(1,-2,1,couleur='red') # x^2 - 2x + 1, Delta = 0
affiche_racines(1,1,-1,couleur='blue') # x^2 + x - 1, Delta > 0
affiche_racines(1,1,1,couleur='green')   # x^2 + x + 1, Delta < 0
# plt.show()

##############################
## Question 2 ##

def affiche_famille(b0,c0,b1,c1,n=100):
    """ Trace les solutions d'une famille
    d'équations u second degré """

    for k in range(n):
        t = k/n
        b = (1-t)*b0 + t*b1
        c = (1-t)*c0 + t*c1
        affiche_racines(1,b,c,couleur='blue')

    affiche_racines(1,b0,c0,couleur='red')
    affiche_racines(1,b1,c1,couleur='green')
        
    return    

# Test
print("--- Test famille de racines ---")
plt.clf()
plt.axes().set_aspect('equal')
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')

affiche_famille(-2,2,3,12/5,n=4)
plt.show()

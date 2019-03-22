
##############################
# Images 3D
##############################

##############################
# Activité  - Surface z = f(x,y)
##############################

from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##############################
## Question 1 ##

# Constantes globales
xmin, xmax = -1, 1
ymin, ymax = -1, 1

nbpoints=10

# Fonction à tracer

# Bol
def f(x,y):
    val = x**2 + y**2
    return val

# Goutte qui tombe dans l'eau
# def f(x,y):
#     r = 20*(x**2 + y**2)
#     val = sin(r)/r
#     return val

# Boîte d'oeuf
# def f(x,y):
#     val = sin(10*x)+cos(10*y)
#     return val 

# Selle de cheval
# def f(x,y):
#     val = x**2-y**2
#     return val 

# Un sommet et un col à franchir
# xmin, xmax = -2, 3
# ymin, ymax = -2.5, 2.5
# def f(x,y):
#     val = exp(-1/3*x**3 + x - y**2)
#     return val 


##############################
## Question 2 ##

def liste_points_xcst(x):
    """ Une liste de points de la surface avec x imposé """
    y = ymin
    h = (ymax-ymin)/nbpoints

    liste_points= []
    for k in range(nbpoints+1):
        P = (x,y,f(x,y))
        liste_points.append(P)
        y = y + h

    return liste_points

# Test
print("--- Liste de points ---")
x = 0
print("Liste :",liste_points_xcst(x))


def liste_points_ycst(y):
    """ Une liste de points de la surface avec y imposé """
    x = xmin
    h = (xmax-xmin)/nbpoints
    
    liste_points= []
    for k in range(nbpoints+1):
        P = (x,y,f(x,y))
        liste_points.append(P)
        x = x + h

    return liste_points

##############################
## Question 3 ##


def trace_ligne(liste_points,couleur='gray'):
    """ Tracé d'une suite de segments reliant des points """
    listex = [x for x,y,z in liste_points]
    listey = [y for x,y,z in liste_points]
    listez = [z for x,y,z in liste_points]

    ax.plot(listex,listey,listez,color=couleur)
    return


def trace_surface():
    """ Tracé d'une surface en affichant des lignes à x constants, 
    puis à y constants """
    
    # Lignes à x = cst
    x = xmin
    h = (xmax-xmin)/nbpoints
    
    for k in range(nbpoints+1):
        ligne = liste_points_xcst(x)
        trace_ligne(ligne,couleur='blue')
        x = x + h

    # Lignes à y = cst
    y = ymin
    h = (ymax-ymin)/nbpoints
    
    for k in range(nbpoints+1):
        ligne = liste_points_ycst(y)
        trace_ligne(ligne,couleur='red')
        y = y + h

    return


# Test
print("--- Trace surface ---")
fig = plt.figure()
ax = fig.gca(projection='3d',proj_type = 'ortho')
# trace_ligne([(0,0,0),(2,0,1),(1,2,3)])
# ligne = [(0, -1, 1), (0, -0.6, 0.36), (0, -0.2, 0.04), (0, 0.2, 0.04), (0, 0.6, 0.36), (0, 1.0, 1.0)]
# trace_ligne(ligne,couleur='blue')
trace_surface()
plt.show()


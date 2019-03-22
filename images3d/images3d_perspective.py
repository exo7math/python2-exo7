
##############################
# Images 3D
##############################

##############################
# Activité - Perspective
##############################


cube  = [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]

##############################
## Question 1 ##

from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def affiche_cube_3d(cube):
    """ Affichage d'un cube en 3d en reliant les sommets """

    P0,P1,P2,P3,P4,P5,P6,P7 = cube

    # Première face
    ax.plot([P0[0],P1[0],P2[0],P3[0],P0[0]],[P0[1],P1[1],P2[1],P3[1],P0[1]],[P0[2],P1[2],P2[2],P3[2],P0[2]],color='red')

    # Seconde face
    ax.plot([P4[0],P5[0],P6[0],P7[0],P4[0]],[P4[1],P5[1],P6[1],P7[1],P4[1]],[P4[2],P5[2],P6[2],P7[2],P4[2]],color='red')

    # Arète joignant les faces
    ax.plot([P0[0],P4[0]],[P0[1],P4[1]],[P0[2],P4[2]],color='red')    
    ax.plot([P1[0],P5[0]],[P1[1],P5[1]],[P1[2],P5[2]],color='red')
    ax.plot([P2[0],P6[0]],[P2[1],P6[1]],[P2[2],P6[2]],color='red')
    ax.plot([P3[0],P7[0]],[P3[1],P7[1]],[P3[2],P7[2]],color='red')

    return

# Test
# print("--- Trace cube 3d ---")
# fig = plt.figure()
# ax = fig.gca(projection='3d',proj_type = 'ortho')

# affiche_cube_3d(cube)

# plt.show()



##############################
## Question 2 ##

def perspective_cavaliere(P,alpha=pi/4,k=0.5):
    """ Calcul des coordonnées la projection 2d d'un point 3d  """
    x,y,z = P
    X = x + k*cos(alpha)*y
    Y =     k*sin(alpha)*y + z
    return (X,Y)


def affiche_cube_2d(cube2d):
    """ Tracé dans le plan de la projection d'un cube en reliant les sommets projetés """

    P0,P1,P2,P3,P4,P5,P6,P7 = cube2d

    # Première face
    plt.plot([P0[0],P1[0],P2[0],P3[0],P0[0]],[P0[1],P1[1],P2[1],P3[1],P0[1]],color='blue')

    # Seconde face
    plt.plot([P4[0],P5[0],P6[0],P7[0],P4[0]],[P4[1],P5[1],P6[1],P7[1],P4[1]],color='blue')

    # Arète joignant les faces
    plt.plot([P0[0],P4[0]],[P0[1],P4[1]],color='blue')    
    plt.plot([P1[0],P5[0]],[P1[1],P5[1]],color='blue')
    plt.plot([P2[0],P6[0]],[P2[1],P6[1]],color='blue')
    plt.plot([P3[0],P7[0]],[P3[1],P7[1]],color='blue')

    return

# Test
print("--- Trace cube 2d : perspective cavalière ---")

# plt.axes().set_aspect('equal')
# # cube2d = [perspective_cavaliere(P,alpha=pi/4,k=0.5) for P in cube]
# cube2d = [perspective_cavaliere(P,alpha=pi/6,k=0.7) for P in cube]
# affiche_cube_2d(cube2d)
# plt.show()



##############################
## Question 3 ##

def perspective_axonometrique(P,alpha=acos(sqrt(2/3)),omega=pi/4):
    """ Calcul des coordonnées la projection 2d d'un point 3d  """
    x,y,z = P
    X = cos(omega)*x - sin(omega)*y
    Y = -sin(omega)*sin(alpha)*x -cos(omega)*sin(alpha)*y + cos(alpha)*z
    return (X,Y)

# Test
print("--- Trace cube 2d : perspective axonométrique ---")

plt.axes().set_aspect('equal')

# Perspective isométrique
# alpha = 0.6154797086703874 # = acos(sqrt(2/3))
# cube2d = [perspective_axonometrique(P,alpha=acos(sqrt(2/3)),omega=pi/4) for P in cube]

# alpha = -10 degrés, omega = 30 degrés
# cube2d = [perspective_axonometrique(P,alpha=-10*2*pi/360,omega=40*2*pi/360) for P in cube]

# affiche_cube_2d(cube2d)
# plt.show()


##############################
## Question 4 ##

def perspective_conique(P,f=5):
    """ Calcul des coordonnées la projection 2d d'un point 3d  """
    
    x,y,z = P
    k = f/(y+f)
    X = k*x
    Y = k*z
    return (X,Y)

# Test
# print("--- Trace cube 2d : perspective conique ---")

plt.axes().set_aspect('equal')

cube  = [(1,1,-1),(2,1,-1),(2,2,-1),(1,2,-1),(1,1,-2),(2,1,-2),(2,2,-2),(1,2,-2)]
cube2d = [perspective_conique(P,f=10) for P in cube]

affiche_cube_2d(cube2d)
plt.show()

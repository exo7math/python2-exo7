
##############################
# Images 3D
##############################


##############################
# Activité  - Coordonnées sphèriques
##############################

from math import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##############################
## Question 1 ##

# r rayon,
# phi : latitude
# lamb : longitude

def latlong_vers_xyz(r,phi,lamb):
    """ (r,phi,lamb) -> (x,y,z) """
    x = r*cos(phi)*cos(lamb)
    y = r*cos(phi)*sin(lamb)
    z = r*sin(phi)
    return x,y,z



# Test
print("--- Coordonnées xyz d'après latitude/longitude ---")
r,phi,lamb = 1,45*2*pi/360,30*2*pi/360
P = latlong_vers_xyz(r,phi,lamb)
print("(x,y,z) =", P)


##############################
## Question 2 ##

def xyz_vers_latlong(x,y,z):
    """ (x,y,z) -> (r,phi,lamb) """
    r = sqrt(x**2+y**2+z**2)
    phi = asin(z/r)
    lamb = asin(y/(r*cos(phi)))
    return r,phi,lamb

# Test
print("--- Coordonnées latitude/longitude d'après xyz ---")
x,y,z = (1,2,3)
S = xyz_vers_latlong(x,y,z)
print("(r,phi,lamb) =", S)

print("--- Vérification ---")
P = latlong_vers_xyz(*S)
print("(x,y,z) =", P)


##############################
## Question 3 ##


def trace_meridien(r,lamb,nbpoints=100,couleur='red'):
    """ Tracé d'un méridien connaissant sa longitude """
    phi = 0
    h = 2*pi/nbpoints
    liste_points = []
    for k in range(nbpoints+1):
        P = latlong_vers_xyz(r,phi,lamb)
        liste_points.append(P)
        phi = phi + h

    listex = [x for x,y,z in liste_points]
    listey = [y for x,y,z in liste_points]
    listez = [z for x,y,z in liste_points]

    ax.plot(listex,listey,listez,color=couleur)
    return

def trace_parallele(r,phi,nbpoints=100,couleur='blue'):
    """ Tracé d'un parallèle connaissant sa latitude """

    lamb = 0
    h = 2*pi/nbpoints
    liste_points = []
    for k in range(nbpoints+1):
        P = latlong_vers_xyz(r,phi,lamb)
        liste_points.append(P)
        lamb = lamb + h

    listex = [x for x,y,z in liste_points]
    listey = [y for x,y,z in liste_points]
    listez = [z for x,y,z in liste_points]

    ax.plot(listex,listey,listez,color=couleur)
    return

def trace_meridiens_parallelles(r,N=24):
    """ Tracé d'une série de méridiens et parallèles """
    for k in range(N):
        lamb = 2*k*pi/N
        # trace_meridien(r,lamb)
        trace_meridien(r,lamb,couleur='#C0C0C0')

    for k in range(N):
        phi = k*pi/(N//2)
        # trace_parallele(r,phi)
        trace_parallele(r,phi,couleur='#C0C0C0')
    return


def trace_point(r,phi,lamb,couleur='green'):
    """ Affichage d'un points connaissant (r,phi,lamb) """
    P = latlong_vers_xyz(r,phi,lamb)
    ax.scatter(*P,color=couleur,s=50)
    return


# Test
print("--- Trace méridien et parallèle ---")
fig = plt.figure()
ax = fig.gca(projection='3d',proj_type = 'ortho')
# trace_meridien(1,pi/6)
# trace_point(1,pi/4,0)
trace_meridiens_parallelles(r=1)
# trace_meridien(1,-pi/4)
# trace_parallele(1,pi/8)

# plt.show()


##############################
## Rappels - Activité "Vecteurs" ##

def norme(u):
    """ Norme (= longueur) d'un vecteur de l'espace """
    x,y,z = u
    n = sqrt(x**2 + y**2 + z**2)
    return n


##############################
## Question 4 ##


def trace_grand_cercle(P,Q,nbpoints=100,couleur="orange"):
    """ Calcul du grand cercle passant par deux points P et Q d'une sphère
    Idée : considérer les points comme de vecteurs u et v
    w = (cos(t) u + sin(t) v)/norme(w) pour t dans [0,2pi] """
    
    # Calcul du vecteur w
    u = latlong_vers_xyz(*P)
    v = latlong_vers_xyz(*Q)
    r = norme(u) 
    # Calcul des points du grand cercle
    t = 0
    h = 2*pi/nbpoints
    liste_points = []
    for k in range(nbpoints+1):
        x1,y1,z1 = u
        x2,y2,z2 = v
        x = cos(t)*x1 + sin(t)*x2
        y = cos(t)*y1 + sin(t)*y2
        z = cos(t)*z1 + sin(t)*z2
        rr = norme((x,y,z))
        w = (x*r/rr,y*r/rr,z*r/rr)        

        liste_points.append(w)
        t = t + h

    # Tracé
    listex = [x for x,y,z in liste_points]
    listey = [y for x,y,z in liste_points]
    listez = [z for x,y,z in liste_points]        
    ax.plot(listex,listey,listez,color=couleur,linewidth=2)
    return



# Test
print("--- Grand cercle ---")
P = (1,pi/4,pi/6)
Q = (1,pi/3,-pi/4)

trace_grand_cercle(P,Q)
trace_point(*P)
trace_point(*Q)
plt.show()

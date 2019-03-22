
##############################
# Images 3D
##############################

##############################
# Activité  - Vecteurs
##############################

from math import *

##############################
## Question 1.a ##

def produit_scalaire(u,v):
    """ Produit scalaire de deux vecteurs de l'espace """
    x,y,z = u
    xx,yy,zz = v
    p = x*xx + y*yy + z*zz
    return p

##############################
## Question 1.b ##

def norme(u):
    """ Norme d'un vecteur de l'espace """
    x,y,z = u
    n = sqrt(x**2 + y**2 + z**2)
    return n


##############################
## Question 1.c ##

def angle(u,v):
    """ Angle (en radian) entre deux vecteurs de l'espace """
    p = produit_scalaire(u,v)
    cosinus = p/(norme(u)*norme(v))
    mon_angle = acos(cosinus)
    return mon_angle

##############################
## Question 1.d ##

# Conversion angle radians/degrés

def degres_vers_radians(a):
    return 2*pi*a/360

def radians_vers_degres(a):
    return 360*a/(2*pi)


# Test
print("--- Produit scalaire ---")
u = (1,2,3)
v = (1,0,1)
print("u =", u, "   v =",v)
print("Norme de u :",norme(u))
print("Produit scalaire :",produit_scalaire(u,v))
print("Angle entre u et v (en radians) ",angle(u,v))
print("Angle entre u et v (en degrés) ",radians_vers_degres(angle(u,v)))


##############################
## Question 1.e ##

def est_visible(P,u,theta):
    """ Détermine si un point P est visible en regardant 
    selon une direction u avec un angle de vision theta """
    alpha = angle(u,P)
    return (abs(alpha) <= theta)

# Test
print("--- Application : points visibles ---")
theta_degres = 50
theta_radians = degres_vers_radians(theta_degres)
u = (1,1,1)
P1 = (1,1,2)
P2 = (-1,-1,-2) 
P3 = (80,10,0)
P4 = (85,10,0)

for P in [P1,P2,P3,P4]:
    print("Le point",P,"est-il visible ?",est_visible(P,u,theta_radians))

##############################
## Question 1.d ##

def rebond(u,n):
    """ Calcul comment une particule qui arrive selon un vecteur u 
    rebondirait sur un plan dont le vecteur normal est n.
    Le résultat est un vecteur. """
    x,y,z = u
    xn,yn,zn = n
    
    N = norme(n)
    xxn,yyn,zzn = xn/N,yn/N,zn/N
    nn = (xxn,yyn,zzn)

    p = produit_scalaire(u,nn)
    print(p)
    xx = x - 2*p*xxn
    yy = y - 2*p*yyn
    zz = z - 2*p*zzn
    v = (xx,yy,zz)
    return v

# Test
print("--- Rebond ---")
u = (1,2,-1)
n = (1,1,1)

v = rebond(u,n)
print("u =", u, "   n =",n)
print("Rebond v :",v)



##############################
## Question 2.a ##

def produit_vectoriel(u,v):
    """ Produit vectoriel de deux vecteurs de l'espace """
    x,y,z = u
    xx,yy,zz = v
    w = ( y*zz-yy*z, z*xx-zz*x, x*yy-xx*y) 
    return w

# Test
print("--- Produit vectoriel ---")
u = (1,2,3)
v = (1,0,1)
w = produit_vectoriel(u,v)
print("u =", u, "   v =",v)
print("w =", w)

print("Produit scalaire w avec u:",produit_scalaire(w,u))
print("Produit scalaire w avec v:",produit_scalaire(w,v))


##############################
## Question 2.b ##

# Test
print("--- Produit vectoriel : application au calcul d'un équation de plan ---")
u = (-1,2,5)
v = (2,0,3)
n = produit_vectoriel(u,v)
print("u =", u, "   v =",v)
print("n =", n)


##############################
## Question 2.c ##
# Application : surface d'un parallélogramme/triangle dans l'espace

# Test
print("--- Produit vectoriel : application au calcul d'une surface d'un triangle ou d'un parallélogramme ---")
u = (1,2,-5)
v = (1,-2,4)
w = produit_vectoriel(u,v)
print("u =", u, "   v =",v)
print("w =", w)
print("norme au carré :",norme(w)**2)
print("aire du parallèlogramme :",norme(w))
print("aire du triangle :",1/2*norme(w))

##############################
## Question 3.a ##

def produit_mixte(u,v,w):
    """ Produit mixte de trois vecteurs de l'espace """
    ww = produit_vectoriel(u,v)
    p = produit_scalaire(ww,w)
    return p

# Test
print("--- Produit mixte ---")
u = (1,2,3)
v = (1,0,1)
w = (4,1,0)
p = produit_mixte(u,v,w)
print("u =", u, "   v =",v, "w =", w)
print("Produit mixte:",produit_mixte(u,v,w))



##############################
## Question 3.b ##

# Application : volume parallélépipède, tétraèdre
# Test
print("--- Application : volume ---")
u = (1,0,0)
v = (1,1,0)
w = (1,1,1)
p = produit_mixte(u,v,w)
print("u =", u, "   v =",v, "w =", w)
print("Volume parallélépipède :",abs(produit_mixte(u,v,w)))
print("Volume tétraèdre :",1/6*abs(produit_mixte(u,v,w)))


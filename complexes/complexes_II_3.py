
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
# Activité 3 - Formule d'Euler / de Moivre / Gauss
##############################

##############################
## Question 1 ##

def cosinus(t):
    """ Calcule le cosinus d'un angle par la formule d'Euler """
    eplus = polaire_vers_cartesien(1,t)
    emoins = polaire_vers_cartesien(1,-t)
    cos_complexe = (eplus+emoins)/2
    cos_reel = cos_complexe.real
    return cos_reel


def sinus(t):
    """ Calcule le sinus d'un angle par la formule d'Euler """
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
    """ Calcule z à la puissance n par la formule de Moivre """
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
    """ Multiplication classique """
    return (a*c-b*d,a*d+b*c)

def multiplication_bis(a,b,c,d):
    """ Multiplication Gauss 1 """
    r = a*c
    s = b*d
    t = (a+b)*(c+d)
    return r-s, t-r-s

def multiplication_ter(a,b,c,d):
    """ Multiplication Gauss 2 """
    r = c*(a+b)
    s = a*(d-c)
    t = b*(c+d)
    return r-t, r+s

# Test
print("--- Formules de Gauss ---")
print(multiplication(2,5,3,-2))
print(multiplication_bis(2,5,3,-2))
print(multiplication_ter(2,5,3,-2))



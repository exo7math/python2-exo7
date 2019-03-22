
##############################
# Complexes II
##############################


##############################
# Activité 2 - Passage polaire/cartésien
##############################


from math import *
import cmath

##############################
## Question 1 ##

def polaire_vers_cartesien(module,argument):
    """ Passage de (r,theta) -> z = a+ib """
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
    """ Passage de z = a+ib -> (r, theta) """
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
    """ Ramène un angle dans l'intervalle ]-pi,+pi] 
    par réduction modulo 2pi """
    k = floor(angle/(2*pi))
    print(k)
    new_angle = angle - 2*k*pi
    if new_angle > pi:
        new_angle += -2*pi
    return new_angle

# Test
print("--- Argument dans intervalle ---")

theta =  -pi/2 + 12*pi
print(theta)
print(argument_dans_intervalle(theta))
print(theta % 2*pi)

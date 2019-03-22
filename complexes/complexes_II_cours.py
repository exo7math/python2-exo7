
##############################
# Complexes II
##############################

##############################
# Cours cmath
##############################


import cmath  # ne pas faire "from cmath import *" car conflit sqrt
from math import *

z = 1-1j

argument = cmath.phase(z)
module = abs(z)

print("Module :", module)
print("Argument :", argument)

# z = complex(1+1j)
z = 1-1j
print("Module, Argument :", cmath.polar(z))


z = cmath.rect(2,pi/4)
print(z)

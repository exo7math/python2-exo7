
##############################
# Complexes I
##############################

##############################
# Activité 1 - Complexes avec Python, Ecriture a + ib
##############################

##############################
## Question 1 ##

z1 = 1+2j
z2 = 3-1j

print(z1+z2)

print(z1*z2)

print(z1 ** 2)

print(abs(z1))

print(1/z1)

##############################
## Question 2 ##

z = (3-4j)**2 * (2-1j)
print(z.real)
print(z.imag)
print(z.conjugate())


##############################
## Question 3 ##


# addition
def addition(a,b,aa,bb):
    return (a+aa,b+bb)

# multiplication
def multiplication(a,b,aa,bb):
    return (a*aa-b*bb,a*bb+b*aa)

# conjugué
def conjugue(a,b):
    return (a,-b)

# module
def module(a,b):
    return sqrt(a**2 + b**2)
    
# inverse
def inverse(a,b):
    if a != 0 and b !=0:
        r2 = a**2 + b**2
        return (a/r2,-b/r2)
    else:
        return None

# puissance
def puissance(a,b,n):
    if n == 0:
        return (1,0)

    aa = a
    bb = b
    for __ in range(n):
        aa,bb = multiplication(a,b,aa,bb)

    return (aa,bb)

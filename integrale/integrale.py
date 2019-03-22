
##############################
# Analyse - Intégration
##############################


##############################
# Activité 1 - Primitive
##############################

##############################
## Question 1  ##

# Rappel de "Dérivées"

def derivee(f,a,h=0.00001):
    """ Calcul approché de f'(a) """
    taux = (f(a+h)-f(a))/h
    return taux


def verification_primitive(f,F,a,b,n=10,epsilon=0.01):
    """ Vérification expérimentale que F'(x) = f(x) """
    h = (b-a)/n
    x = a

    valide = True

    for i in range(n+1):
        ecart = f(a)-derivee(F,a)
        if abs(ecart) > epsilon:
            valide = False
            print(a,f(a),derivee(F,a))
        a = a + h

    return valide


# Test
f = lambda x: x**3
F = lambda x: 1/4*x**4

print("Primitive ok ?",verification_primitive(f,F,0,2))


##############################
## Question 2 ##

def integrale_primitive(F,a,b):
    """ Calcule int_a^b f(t) dt par la formule F(b)-F(a) """
    return F(b)-F(a)


f = lambda x: x**3
F = lambda x: 1/4*x**4

print("Intégrale connaissant la primitive :",integrale_primitive(F,0,2))


##############################
# Activité 2.1 - Méthode des rectangles
##############################

def integrale_rectangles(f,a,b,n):
    """ Calcule int_a^b f(t) dt par la méthode des rectangles """
    h = (b-a)/n
    x = a

    integrale = 0

    for i in range(n):
        integrale = integrale + f(a)*h
        a = a + h

    return integrale

f = lambda x: x**3

print("Intégrale par rectangle :",integrale_rectangles(f,0,2,n=100))



##############################
# Activité 2.2 - Méthode des trapèzes
##############################

def integrale_trapezes(f,a,b,n):
    """ Calcule int_a^b f(t) dt par la méthode des trapèzes """

    h = (b-a)/n
    x = a

    integrale = 0

    for i in range(n):
        integrale = integrale + (f(a)+f(a+h))/2*h
        a = a + h

    return integrale

f = lambda x: x**3

print("Intégrale par trapèzes :",integrale_trapezes(f,0,2,n=100))


##############################
# Activité 2.3 - Méthode de Simpson
##############################

def integrale_simpson(f,a,b,n):
    """ Calcule int_a^b f(t) dt par la méthode de Simpson """

    h = (b-a)/n
    x = a

    integrale = 0

    for i in range(n):
        integrale = integrale + (f(a)+4*f(a+h/2)+f(a+h))/6*h
        a = a + h

    return integrale

f = lambda x: x**3

print("Intégrale par Simpson :",integrale_simpson(f,0,2,n=100))

# Fonction utile pour la suite
def integrale(f,a,b,n):
    return integrale_simpson(f,a,b,n)


##############################
# Activité 3 - Intégrale de Gauss
##############################

from math import *

def integrale_gauss(x,mu,sigma2):
    """ Calcul de l'intégrale de Gauss """

    P = lambda x: 1/sqrt(2*pi*sigma2)*exp( -1/2 * (x-mu)**2 / sigma2 )
    infini = 20*sqrt(sigma2)  # une grande valeur
    p = integrale(P,-infini,x,100)
    return p

# Test
print(integrale_gauss(1,0,1))
print(integrale_gauss(0,0,1))

print('QI',integrale_gauss(115,100,225))


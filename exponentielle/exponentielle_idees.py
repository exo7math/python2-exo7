
##############################
# Exponentielle
##############################


##############################
# Activité 1 - L'exponentielle
##############################

from math import *

##############################
## Question 1 ##

# --- Grains de riz ---

##############################
## Question 1.a ##
N = 64  # Nombre de cases
n = 1
somme = 0
for k in range(N):
    somme = somme + n 
    n = 2*n

print("--- Grains de riz ---")
print("Nombre de grain de riz :",somme)

##############################
## Question 1.b ##

# 50 000 grain de riz pèse un kilogramme
masse = somme / (50000*1000)  # en tonne
print("Masse (en tonnes)",masse)


##############################
## Question 2 ##

# Enoncé : nénuphar, 
# surface mutliplié par 1.5 chaque jour
# jour 10, surface = 100
# surface au jour 15 ?
# surface au jour 1 ?
# équation S(x) = c * (1.5)**x = c * exp(1.5 *ln(x)) 
# quand surface vaut 10000 ?

##############################
## Question 2.a ##

surface_15 = 100 * 1.5**5

##############################
## Question 2.b ##

surface_0 = 100 / 1.5**10

##############################
## Question 2.c ##

def surface_nenuphar(x):
    c = 100 / 1.5**10   # Surface initiale
    S = c * exp(x*log(1.5)) 
    return S

print("--- Nénuphar ---")

print("Surface jour 15 :",surface_15)
print("Surface jour 0  :",surface_0)

##############################
## Question 2.d ##

# Trouver jour par tatonnement ou balayage
x = 21.3578
print("Jour :",x)
print("Surface :",surface_nenuphar(x))

##############################
## Question 2.e  ##

# Trouver jour par équation
def jour_nenuphar(S):
    c = 100 / 1.5**10   # Surface initiale
    x = (log(S)-log(c))/log(1.5)
    return x


print("Jour :",jour_nenuphar(10000))
    

##############################
## Question 3 ##

# Loi de refroidissement de Newton
# T(t) - Tinfini = (T(0)-Tinfini)*exp(-k*t)

# Temperature ambiante (au bout d'un temps infini) = 20
# Au départ 100 °C, au bout de 10 minutes 60 degrés
Tinfini = 25
T0 = 100 # t0 = 0
T1 = 65
t1 = 10  

##############################
## Question 3.a ##

# Calculer k
k = -1/t1 * log((T1-Tinfini)/(T0-Tinfini))

##############################
## Question 3.b ##

# Fonction + temperature au bout de 20 minutes
def temperature(t):
    T = (T0-Tinfini)*exp(-k*t) + Tinfini
    return T

print("--- Loi de refroidissement de Newton ---")
print("k =",k)
print("Température initiale ",temperature(0))
print("Température à 10 mn ",temperature(10))
print("Température à 20 mn ",temperature(20))

##############################
## Question 3.c ##

# Quand température atteint 30 °C (tatonnement, balayage, équation)
print("Temperature de 30 °C",temperature(43))


##############################
# Activité 2 - Définition de l'exponentielle
##############################


##############################
## Question 1  ##

def exponentielle_limite(x,n=10000):
    expo = (1+x/n)**n
    return expo

##############################
## Question 2  ##

def factorielle(n):
    fact = 1
    for k in range(1,n+1):
        fact = fact* k
    return fact

##############################
## Question 3  ##

def exponentielle_somme(x,n=15):
    expo = 0
    for k in range(n+1):    
        expo = expo + (x**k)/factorielle(k)
    return expo


##############################
## Question 4  ##

# Bof : pas flagrant si on part en sens inverse

def exponentielle_somme_inverse(x,n=15):
    expo = 0
    for k in reversed(range(n+1)):   
        expo = expo + (x**k)/factorielle(k)
    return expo

    
##############################
## Question 5  ##

# e^x = 1 + (x/1) (1 + (x/2) (1 + (x/3) (........) ) ) 
def exponentielle_horner(x,n=20):
    expo = 1
    for k in reversed(range(1,n+1)):   
        expo = x/k * expo + 1
    return expo

##############################
## Question 6  ##

# Exponentielle via les fractions continues
# https://en.wikipedia.org/wiki/Euler%27s_continued_fraction_formula
def exponentielle_euler(x,n=20):
    expo = 0
    for k in reversed(range(1,n+1)):   
        expo = x/(k+x-k*expo)
    expo = 1/(1-expo)
    return expo



# Test
print("--- Définition(s) de l'exponentielle ---")
x = 2
print("x =",x)
print("Valeur python :",exp(x))
print("Valeur limite :",exponentielle_limite(x))
print("Valeur somme :",exponentielle_somme(x,n=20))
print("Valeur somme inverse :",exponentielle_somme_inverse(x,n=20))
print("Valeur somme Hörner :",exponentielle_horner(x,n=20))
print("Valeur Euler :",exponentielle_euler(x,n=35))

# print(factorielle(3))




##############################
## Question 4  ##

# e = exponentielle_somme(1,n=25)

def exponentielle_astuce(x,n=15):
    e = 2.718281828459045
    n = floor(x)  # partie entière
    f = x-n       # partie fractionnaire
    expo_entier = e**n 
    expo_frac = exponentielle_somme(f,n=n)
    expo = expo_entier * expo_frac
    return expo



# Test
print("--- Définition de l'exponentielle ---")
x = 200
print("x =",x)
print("Valeur python :",exp(x))
print("Valeur limite :",exponentielle_limite(x))
print("Valeur somme :",exponentielle_somme(x,n=20))
print("Valeur astuce :",exponentielle_astuce(x,n=20))

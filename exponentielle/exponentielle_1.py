
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
N = 64 # Nombre de cases
n = 1
somme = 0
for k in range(N):
    somme = somme + n 
    n = 2*n

print("--- Grains de riz ---")
print("Nombre de grain de riz :",somme)
# print(2**N-1)

##############################
## Question 1.b ##

# 50 000 grains de riz pèse un kilogramme
masse = somme / (50000*1000)  # en tonne
print("Masse (en tonnes) :",masse)


##############################
## Question 2 ##

# Enoncé : nénuphar, 
# surface mutliplié par 1.5 chaque jour
# jour 10, surface = 100
# surface au jour 15 ?
# surface au jour 0 ?
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
    """ Surface au bout de x jours """
    S0 = 100 / 1.5**10   # Surface initiale
    S = S0 * exp(x*log(1.5)) # ou alors 
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
    """ Nb de jours pour atteindre la surface S """
    S0 = 100 / 1.5**10   # Surface initiale
    x = (log(S)-log(S0))/log(1.5)
    return x

print("Jour :",jour_nenuphar(200))
print("Jour :",jour_nenuphar(10000))
print("Jour :",surface_nenuphar(jour_nenuphar(10000)))

##############################
## Question 3 ##

# Loi de refroidissement de Newton
# T(t) - Tinfini = (T(0)-Tinfini)*exp(-k*t)

# Temperature ambiante (au bout d'un temps infini) = 25
# Au départ 100 °C, au bout de 10 minutes 65 degrés
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
    """ Temperature au bout du temps t """
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
## Question 4 ##

# Demi-vie et datation au carbone 14

##############################
## Question 4.a ##

def carbone14(t,N0=1000,T=5730):
    """ Nb d'atomes de carbone 14 au bout d'un temps t
    N0 est le nb d'atomes initial, T est la période de demi-vie """
    return N0*exp(-t*log(2)/T)

# Test
print("--- Carbone 14 ---")
t = 100
print("t =",t)
print(carbone14(t))


##############################
## Question 4.b ##
def carbone14_bis(t,N0=1000,T=5730):
     """ Variante avec exposant au lieu d'exponentielle """   
    return N0*2**(-t/T)

# Test
print(carbone14_bis(t))
t = 5730
print(carbone14_bis(t))


##############################
## Question 4.c ##
def datation14(N,N0=1000,T=5730):
    """ Temps écoulé afin qu'il reste N atomes de carbones
     N0 est le nb d'atomes initial, T est la période de demi-vie """   
    return -T/log(2)*log(N/N0)

print(datation14(500))
print(datation14(200))
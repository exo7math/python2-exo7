
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

##############################
##############################
# Cours : visualisation

import matplotlib.pyplot as plt

plt.clf()  # Efface tout
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y
plt.axes().set_aspect('equal')  # Repère orthonormé

x1 = 1
y1 = 2
plt.scatter(x1,y1,color='red',s=80)     # Un premier point

x2 = 5
y2 = 3
plt.scatter(x2,y2,color='blue',s=80)     # Un second point

# Un segment reliant les points
plt.plot([x1,x2],[y1,y2],color='green')
 
plt.show()  # Lancement de la fenêtre


##############################
# Activité 2 - Visualisation
##############################

from math import *

import matplotlib.pyplot as plt

##############################
## Question 1 ##

# fig,ax = plt.subplots()
z = -2+3j
x = z.real
y = z.imag

plt.clf() # Efface tout
plt.axhline(y=0, color='r', linestyle='-')  # Axe x
plt.axvline(x=0, color='r', linestyle='-')  # Axe y
plt.axes().set_aspect('equal') # Repère orthonormé

plt.scatter(x,y,color='red',s=20)
plt.scatter(1,0,color='green',s=20)
plt.scatter(0,1,color='blue',s=20)

# plt.show()

##############################
## Question 2 ##

z0 = 3-2j
x0 = z0.real
y0 = z0.imag

x1,y1 = multiplication(x0,y0,2,0)
x2,y2 = multiplication(x0,y0,0,-1)

xx3,yy3 = puissance(x0,y0,2)
r = module(x0,y0)
x3,y3 = xx3/r, yy3/r

x4,y4 = conjugue(x0,y0)
x5,y5 = inverse(x0,y0)

plt.clf()
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.axes().set_aspect('equal')

plt.scatter(x0,y0,color='red',s=20)
plt.scatter(x1,y1,color='green',s=20)
plt.scatter(x2,y2,color='blue',s=20)
plt.scatter(x3,y3,color='brown',s=20)
plt.scatter(x4,y4,color='orange',s=20)
plt.scatter(x5,y5,color='purple',s=20)

# plt.show()


##############################
## Question 3 ##

def affiche_triangle(z1,z2,z3):
    x1,y1 = z1.real,z1.imag
    x2,y2 = z2.real,z2.imag
    x3,y3 = z3.real,z3.imag

    plt.scatter(x1,y1,color='red',s=50)
    plt.scatter(x2,y2,color='green',s=50)
    plt.scatter(x3,y3,color='blue',s=50)    

    plt.plot([x1,x2,x3,x1],[y1,y2,y3,y1],color='black')

    return

plt.clf()
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.axes().set_aspect('equal')

# Test
# affiche_triangle(2+1j,1-1j,-2+1.5j)

z = 1+2j
# affiche_triangle(z,2*z,(1+2j)*z)  # Triangle rectangle

z = 1+2j
omega = -1/2+sqrt(3)/2*1j
#affiche_triangle(z,omega*z,omega*omega*z)  # Triangle isocèle

# plt.show()



##############################
# Activité 3 - Hack - Equation de degré 1
##############################

def solution_equation_lineaire(equation):
    """ 
    Résoud une équation linéaire réelle de degré 1
    Entrée : une chaîne de caractère sous la forme "3*(x+1) + x = 2*x+1"
    Sortie : la valeur de la solution x (par exemple ici renvoie -1)
    Remarque : utilise astucieusement les nombres complexes !
    """

    # Parties gauche et droite de l'équation 
    # Ex "3*(x+1) + x = 2*x+1" -> "3*(x+1) + x" et "2*x+1"
    eq_gd = equation.split("=")

    # On bascule tout à gauche 
    # Ex : on obtient "3*(x+1) + x - ( 2*x+1 )" (sous-entendu = 0)
    new_eq = eq_gd[0] + "- (" + eq_gd[1] + " )"  # 

    # On remplace les x par le nb complexe 1j
    # Ex :on obtient "3*(1j+1) + 1j - ( 2*1j+1 )"
    z_str = new_eq.replace("x","1j")

    # On évalue la chaîne
    # Ex : la chaîne devient le nb complexe z = 3*(1j+1) + 1j - ( 2*1j+1 )
    z = eval(z_str)

    # On récupère les parties réelle et imaginaire
    # Ex : a = 2, b = 2
    a = z.real
    b = z.imag

    # Solution de l'équation qui correspond en fait à "a + bx = 0"
    # Ex : sol = -1
    sol = -a/b

    return sol


# Test
print("--- Solution d'une équation linéaire réelle ---")
eq = "7*x+3 = 0"
# eq = "3*(x+1) + x = 2*x+1"
x = solution_equation_lineaire(eq)
print("Equation :",eq)
print("Solution :", x)



##############################
# Activité 4 - Equation du second degré
##############################

from math import *

##############################
## Question 1 ##

def solution_trinome(a,b,c):
    """ Solutions de ax^2 + bx + c = 0 avec a,b,c réels """

    Delta = b**2 - 4*a*c

    if Delta == 0:
        sol = [-b/(2*a),-b/(2*a)]

    if Delta > 0:
        d = sqrt(Delta)
        sol = [(-b-d)/(2*a), (-b+d)/(2*a)]

    if Delta < 0:
        d = 1j*sqrt(-Delta)
        sol = [(-b-d)/(2*a), (-b+d)/(2*a)]

    return sol

# Test
print("--- Solution d'une équation de degré 2 ---")
sol = solution_trinome(1,-2,1)  # x^2 - 2x + 1, Delta = 0
print("Solution :", sol)
sol = solution_trinome(1,1,-1)  # x^2 + x - 1, Delta > 0
print("Solution :", sol)
sol = solution_trinome(1,1,1)  # x^2 + x + 1, Delta < 0
print("Solution :", sol)


##############################
## Question 2 ##

def solution_somme_produit(S,P):
    return solution_trinome(1,-S,P)

# Test
print("--- Solution somme/produit ---")
x,y = solution_somme_produit(10,20)  # S = 10, P = 20
print("Solution :", x,y)
print("Vérification :", x+y, x*y)


##############################
## Question 3 ##

def solution_bicarre(a,b,c):
    """ Solutions de ax^4 + bx^2 + c = 0 avec a,b,c réels et Delta >= 0 """

    Delta = b**2 - 4*a*c

    if Delta < 0:
        print("Discriminant négatif. Je ne sais pas faire.")
        return None

    # On récupère les solution de aX^2 + bX + c
    X1, X2 = solution_trinome(a,b,c)

    sol = []
    for X in [X1,X2]:

        if X >= 0: 
            # Si Xi >= 0 on prend les racines carrées
            x1 = +sqrt(X)
            x2 = -sqrt(X)
            sol = sol + [x1,x2]

        if X < 0:
            # Si Xi < 0 on prend les racines carrées  +/- i*racine(-Xi)
            x1 = +1j*sqrt(-X)
            x2 = -1j*sqrt(-X)
            sol = sol + [x1,x2]

    return sol


# Test
print("--- Solution bicarré ---")
sol = solution_bicarre(1,-2,-3)
print(sol)



##############################
# Activité 5 - Famille de racines
##############################


##############################
## Question 1 ##

def affiche_racines(a,b,c,couleur='red'):
    z1,z2 = solution_trinome(a,b,c)     
    x,y = z1.real, z1.imag
    plt.scatter(x,y,color=couleur,s=40) 
    x,y = z2.real, z2.imag
    plt.scatter(x,y,color=couleur,s=40)
    return

# Test
print("--- Test affiche racines ---")
plt.clf()
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.axes().set_aspect('equal')
sol = solution_trinome(1,-2,1)  
affiche_racines(1,-2,1,couleur='red') # x^2 - 2x + 1, Delta = 0
affiche_racines(1,1,-1,couleur='blue') # x^2 + x - 1, Delta > 0
affiche_racines(1,1,1,couleur='green')   # x^2 + x + 1, Delta < 0
# plt.show()

##############################
## Question 2 ##

def affiche_famille(b0,c0,b1,c1,n=100):

    for k in range(n):
        t = k/n
        b = (1-t)*b0 + t*b1
        c = (1-t)*c0 + t*c1
        affiche_racines(1,b,c,couleur='blue')

    affiche_racines(1,b0,c0,couleur='red')
    affiche_racines(1,b1,c1,couleur='green')
        
    return    

# Test
print("--- Test famille de racines ---")
plt.clf()
plt.axhline(y=0, color='r', linestyle='-')
plt.axvline(x=0, color='r', linestyle='-')
plt.axes().set_aspect('equal')
affiche_famille(-2,2,3,12/5,n=4)
plt.axes().set_aspect('equal')
plt.show()

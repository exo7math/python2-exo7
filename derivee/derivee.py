
##############################
# Zéros de fonction - Dérivées
##############################

from math import *

##############################
# Cours
##############################

f = lambda x: x**2

print(f(2))

def f(x):
    return x**2

print(f(2))


def est_plus_grand(f,a,b):
    if f(a) > f(b):
        return True
    else:
        return False 

print(est_plus_grand(f,1,2))
print(est_plus_grand(lambda x:1/x,1,2))

##############################
# Activité 1 - Calcul de la dérivée en un point
##############################

##############################
## Question 1  ##

# Fonction définie comme lambda-fonction
f = lambda x: x*(1-sqrt(x))

# Evaluation
# for a in range(6):
#     print("a =",a)
#     print("f(a) =",f(a))

##############################
## Question 2  ##

def derivee(f,a,h=0.00000001):
    """ Calcul approché de la dérivée de f en a par le taux d'accroissement """
    taux = (f(a+h)-f(a))/h
    return taux

# Test
f = lambda x: x**3
for a in range(6):
    print("a =",a)
    print("f(a) =",f(a))
    print("f'(a) =",derivee(f,a))
    print("f'(a) =",3*a**2)

# f = lambda x: sqrt(x)
# for a in range(1,6):
#     print("a =",a)
#     print("f(a) =",f(a))
#     print("f'(a) =",derivee(f,a))
#     print("f'(a) =",1/(2*sqrt(a)))

##############################
# Activité 2 - Graphe d'une fonction
##############################

##############################
## Question 1  ##

def graphe(f,a,b,n):
    """ n points du graphe de f sur [a,b] """
    liste_points = []    
    h = (b-a)/n
    x = a
    for i in range(n+1):
        y = f(x)
        liste_points.append( (x,y) )
        x = x + h
    return liste_points

# Test
f = lambda x: x*x
print(graphe(f,0,2,4))


##############################
## Question 2  ##

def afficher_un_point(i,j,couleur="red",taille=5):
    canvas.create_rectangle(i-taille,j-taille,i+taille,j+taille,fill=couleur,width=1)
    return


def afficher_points(points,echelle=50):

    # Axes
    canvas.create_line(50,300,750,300,fill="blue",width=5)         
    canvas.create_line(400,550,400,50,fill="blue",width=5)         

    for p in points:
        x,y = p
        i = round(x*echelle)
        j = round(y*echelle)
        afficher_un_point(400+i,300-j,couleur="black")



    return

##############################
## Question 3  ##

def relier_points(points,echelle=50):
    # Axes
    canvas.create_line(50,300,750,300,fill="blue",width=5)         
    canvas.create_line(400,550,400,50,fill="blue",width=5)         
 
    n = len(points) - 1

    for k in range(n):
        x,y = points[k]
        xx,yy = points[k+1]
        i = round(x*echelle)
        j = round(y*echelle)
        ii = round(xx*echelle)
        jj = round(yy*echelle)
        canvas.create_line(400+i,300-j,400+ii,300-jj,fill="red",width=5)         

    return

def tracer_graphe(f,a,b,n=20,echelle=50):
    points = graphe(f,a,b,n)
    relier_points(points,echelle=echelle)

    # Axes
    canvas.create_line(50,300,750,300,fill="blue",width=5)         
    canvas.create_line(400,550,400,50,fill="blue",width=5)         

    # To do : marques
    return    

##############################
## Question 5  ##

def tracer_tangente(f,a,echelle=50):
    """ Tracer de la tangente de f en a 
    en utilisant la dérivée """
    x = a
    y = f(a)
    dx = 1
    dy = derivee(f,a)
    i = round(x*echelle)
    j = round(y*echelle)
    ii = round((x+dx)*echelle)
    jj = round((y+dy)*echelle)
    iii = round((x-dx)*echelle)
    jjj = round((y-dy)*echelle)    

    # Point
    canvas.create_rectangle(400+i-4,300-j-4,400+i+4,300-j+4,fill="gray",width=1)

    # Demi-tangentes
    canvas.create_line(400+i,300-j,400+ii,300-jj,fill="black",width=3)
    canvas.create_line(400+i,300-j,400+iii,300-jjj,fill="black",width=3)

    return

# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

f = lambda x: sqrt(x)
points = graphe(f,0,4,4)
# relier_points(points,echelle=80)
# afficher_points(points,echelle=80)
# tracer_graphe(f,0,4,echelle=80)
# tracer_tangente(f,1,echelle=80)


root.mainloop()

##############################
# Activité 3 - Dichotomie
##############################


def dichotomie(f,a,b,epsilon):
    """ Résolution approchée de f(x)=0 sur [a,b]
    Renvoie un encadrement de longueur plus petit que epsilon """

    # Vérification de l'hypothèse
    assert f(a)*f(b) <= 0

    # Boucle
    while b-a > epsilon:
        c = (a+b)/2
        if f(a)*f(c) <= 0:
            b = c
        else:   
            a = c

    return a,b   # intervalle

# Test
f = lambda x: x*x-2
print(dichotomie(f,0,2,1e-5))




##############################
# Activité 4 - Méthode de Newton
##############################

def newton(f,a,n):
    """ Résolution approchée de l'équation f(x)=0 par la méthode de Newton. 
    a est la valeur de départ, n le nombre d'itérations """
    x = a
    for i in range(n):
        x = x - f(x)/derivee(f,x)

    return x

# Test
f = lambda x: x*x-2
print(newton(f,2,5))




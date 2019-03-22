
##############################
# Récursivité
##############################

##############################
# Activité 6 - Tortue récursive 
##############################

##############################
## Question 1 ##

from turtle import *


def koch(l,n):
    """ Trace le flocon de Koch d'ordre n ('l' est une longueur) """
    if n==0:
        forward(l) 
        return

    koch(l/3,n-1)
    left(60)
    koch(l/3,n-1)
    right(120)
    koch(l/3,n-1)
    left(60)
    koch(l/3,n-1)
    
    return

# Test
# speed('fastest')
# width(2)
# up()
# goto(-400,-200)
# down()
# koch(800,4)
# exitonclick()


##############################
## Question 2 ##


def arbre(l,n):
    """ Dessine un arbre d'ordre n ('l' est une longueur) """ 
    if n==0:
        return

    P = position()
    setheading(-120)    
    forward(l)
    arbre(l/2,n-1)
    goto(P)
    setheading(-60)    
    forward(l)
    arbre(l/2,n-1)
    goto(P)

    return

# Test
# speed('fastest')
# width(3)
# up()
# goto(0,300)
# down()
# arbre(300,6)
# exitonclick()



##############################
## Question 3 ##


def triangle(l,n):
    """ Dessine le triangle de Sierpinski d'ordre n ('l' est une longueur) """
    if n==0:
        return

    for __ in range(3):
        triangle(l/2,n-1)    
        forward(l)
        left(120)

    return

# Test
speed('fastest')
hideturtle()
width(3)
up()
goto(-300,-250)
down()
triangle(600,6)
exitonclick()


##############################
## Question 4 ##

# Depuis la doc du module 'turtle'
def hilbert(angle,n):
    """ Dessine la courbe de Hilbert d'ordre n """
    if n == 0:
        return

    left(-angle)
    hilbert(-angle,n-1)
    forward(longueur)
    left(angle)
    hilbert(angle,n-1)
    forward(longueur)
    hilbert(angle,n-1)
    left(angle)
    forward(longueur)
    hilbert(-angle,n-1)
    left(-angle)

    return

from math import *

# Test
# speed('fastest')
# width(3)
# up()
# goto(-300,300)
# down()
# n = 4
# longueur = 40
# hilbert(90,n)
# exitonclick()


##############################
## Question 5 ##

def quart_cercle(pas):
    """ Trace un quart de cercle """
    for i in range(45):
        left(2)
        forward(pas)

# Test
# quart_cercle(1)
# exitonclick()

from random import *


def fractale_cercle(l,n):
    """ Dessine une fractale aléatoire à base de (quart de) cercles
    n est l'ordre de la fracatale, 'l' est un paramètre de longueur """
    if n == 0:
        return

    for __ in range(4):    
        quart_cercle(l)

        hasard = randint(0,3)
        if hasard <= 2:
            fractale_cercle(l/3,n-1)

    return


# Test
up()
goto(0,-300)
down()
speed('fastest')
width(3)
l = 11
fractale_cercle(l,4)
exitonclick()    


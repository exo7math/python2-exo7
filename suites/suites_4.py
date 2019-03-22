
##############################
# Suites
##############################


##############################
# Activité 4 - Tracer la somme d'une suite géométrique
##############################

from turtle import *

##############################
## Question 1 ##

def affiche_un_carre(longueur):
    """ Affiche un carré """

    for i in range(4):
        forward(longueur)
        left(90)
    return


##############################
## Question 2 ##

def affiche_un_rectangle(longueur):
    """ Affiche un rectangle 
    correspondant à un demi-carré """

    for i in range(2):
        forward(longueur)
        left(90)
        forward(longueur/2)
        left(90)       
    return


##############################
## Question 3 ##

def affiche_les_carres(n):
    """  Itère la construction en alternant carré/rectangle """
    
    cote  = 256
    up()
    goto(-cote//2,-cote//2)
    down()
    width(2)
    color('blue')

    k = 0
    while 2*k <= n:
        affiche_un_carre(cote / 2**k)
        if 2*k < n:
            affiche_un_rectangle(cote / 2**k)
        k = k + 1

    exitonclick()
    return

# Lancement !
affiche_les_carres(8)



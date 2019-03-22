
##############################
# Logarithme
##############################

from math import *


##############################
# Activité 3 - Le logarithme décimal - Échelle logarithmique
##############################

import matplotlib.pyplot as plt

def afficher_points_xy(points):
    for (x,y) in points:
        plt.scatter(x,y,color="red")

def afficher_points_xlogy(points):
    for (x,y) in points:
        plt.scatter(x,log(y,10),color="green")

def afficher_points_logxlogy(points):
    for (x,y) in points:
        plt.scatter(log(x,10),log(y,10),color="blue")


# Test
points1 = [ (x,1.5*x+2) for x in [2,3,5,7,11] ]      # y = ax+b a=1.5, b=-2
points2 = [ (x,10**(0.1*x+0.5)) for x in [2,3,5,7,11] ]  # y = 10**(a x + b), log10(y) = a x + b
points3 = [ (x,2*x**1.5) for x in [2,3,5,7,11] ]     # y = beta x^alpha, log10(y) = alpha*log10(x) + log10(beta) 
points = points2
print(points)
# afficher_points_xy(points)
afficher_points_xlogy(points)
# afficher_points_logxlogy(points)



plt.axes().set_aspect('equal')
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.grid()
plt.show()



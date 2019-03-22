
##############################
# Programmation objet
##############################

##############################
# Cours - Programmation objet - Vecteurs de dimension 3
##############################

from math import *

class Vecteur:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        ligne = "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
        return ligne

    def norme(self):
        N = sqrt(self.x**2 + self.y**2 + self.z**2)
        return N

    def produit_par_scalaire(self,k):
        W = Vecteur(k*self.x,k*self.y,k*self.z)
        return W

    def addition(self,other):
        W = Vecteur(self.x+other.x,self.y+other.y,self.z+other.z)
        return W

    def __add__(self,other):
        W = Vecteur(self.x+other.x,self.y+other.y,self.z+other.z)
        return W

# Test
print("--- Objet : Vecteur() ---")
V = Vecteur(1,2,3)
print(V)
print(V.x)
# V.x = 7
# print(V.x)

print("Norme :",V.norme())

V1 = Vecteur(1,2,3)
V2 = Vecteur(1,0,-4)
V3 = V1.addition(V2)
print(V3)
V4 = V1+V2
print(V4)
print(V1.__add__(V2))
print(V4)


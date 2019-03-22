
##############################
# Programmation objet
##############################

##############################
# Cours - Programmation objet
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
        V = Vecteur(k*self.x,k*self.y,k*self.z)
        return V

    def addition(self,other):
        V = Vecteur(self.x+other.x,self.y+other.y,self.z+other.z)
        return V

    def __add__(self,other):
        V = Vecteur(self.x+other.x,self.y+other.y,self.z+other.z)
        return V

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


##############################
# Activité 1 - Matrice 2x2
##############################

class Matrice:

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        ligne1 = str(self.a) + " " + str(self.b) + "\n"
        ligne2 = str(self.c) + " " + str(self.d)
        return ligne1 + ligne2

    def trace(self):
        tr = self.a + self.d
        return tr

    def determinant(self):
        det = self.a*self.d - self.b*self.c
        return det

    def produit_par_scalaire(self,k):
        M = Matrice(k*self.a,k*self.b,k*self.c,k*self.d)
        return M

    def inverse(self):
        det = self.determinant()
        if det == 0:
            return None
        else:
            M = Matrice(self.d,-self.b,-self.c,self.a)
            MM = M.produit_par_scalaire(1/det)
        return MM       

    def __add__(self,other):
        M = Matrice(self.a+other.a,self.b+other.b,self.c+other.c,self.d+other.d)
        return M

    def __mul__(self,other):
        M = Matrice(self.a*other.a + self.b*other.c,
                    self.a*other.b + self.b*other.d,
                    self.c*other.a + self.d*other.c,
                    self.c*other.b + self.d*other.d
            )
        return M

# Test
print("--- Objet : Matrice() ---")

print("- Affichage -")
M = Matrice(1,2,3,4)
print(M)
M.__str__
print("Trace :",M.trace())
print("Déterminant : ",M.determinant())

print("- Produit par scalaire -")

MM = M.produit_par_scalaire(5)
print(MM)

print("- Inverse -")

print(M.inverse())

print("- Addition -")

M1 = Matrice(4,3,2,1)
M2 = Matrice(1,0,-1,1)
M3 = M1+M2
print(M3)

print("- Multiplication -")

M4 = M1*M2
print(M4)
print(M2*M1)

print("- Verif. inverse -")
M1 = Matrice(4,3,2,1)
M5 = M1.inverse()
# print(M5)
print(M1*M5)

# Application à Fibonnacci
print("- Fibonacci -")

M = Matrice(0,1,1,1)
n = 100
Mn = M
for k in range(n-1):
    Mn = Mn * M
print("n =",n)
print("Matrice puissance n :",Mn)
print("Print coeff. Fn (donné par d) :",Mn.d)

##############################
# Activité 2 - Tortue
##############################

##############################
## Question 1  ##


class TortueBasique:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.couleur = 'red'

    def aller_a_xy(self,x,y):
        x0 = self.x  # Position actuelle
        y0 = self.y

        self.x = x  # Nouvelle position
        self.y = y

        canvas.create_line(x0,y0,x,y,fill=self.couleur,width=5)
        return

    def renvoyer_xy(self):
        return self.x, self.y

       
# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

print("--- Objet : TortueBasique() ---")

# tortue = TortueBasique()

# tortue.aller_a_xy(100,100)
# tortue.aller_a_xy(200,100)

# root.mainloop()

##############################
## Question 2 ##
    # afficher, cacher
    # plusieurs tortues


##############################
# Cours - Héritage - Ennemis
##############################

class Ennemi():
    def __init__(self,x,y,vie):
        self.x = x
        self.y = y
        self.vie = vie

    def affiche_vie(self):
        print("Vie =",self.vie)

    def perd_vie(self,n):
        self.vie = self.vie - n

# Exemple 
print("--- Objet : Héritage - Ennemi() ---")
tour = Ennemi(1,2,100)
super_tour = Ennemi(5,3,200)
tour.affiche_vie()
tour.perd_vie(50)
tour.affiche_vie()


class Zombie(Ennemi):

    def __init__(self,x,y,vie,force):
        Ennemi.__init__(self,x,y,vie)
        self.force = force

    def affiche_force(self):
        print("Force =",self.force)

# Exemple
print("--- Objet : Héritage - Zombie() ---")
mechant = Zombie(4,4,100,100)
mechant.affiche_vie()
mechant.affiche_force()

super_mechant = Zombie(7,2,200,200)
super_mechant.perd_vie(50)
super_mechant.affiche_vie()


##############################
# Activité 3 - Tortue Héritage
##############################

from math import *

##############################
## Question 1 ##

class TortueTournante(TortueBasique):

    def __init__(self):   
        TortueBasique.__init__(self)
        self.direction = 0

    def fixer_direction(self,direction):
        self.direction = direction

    def tourner(self,angle):
        self.direction = self.direction + angle

    def avancer(self,longueur):
        angle = self.direction
        dx = longueur*cos(2*pi/360*angle) 
        dy = longueur*sin(2*pi/360*angle)
        self.aller_a_xy(self.x+dx,self.y+dy)


print("--- Objet : TortueTournante() ---")

tortue = TortueTournante()


# tortue.aller_a_xy(100,100)
# tortue.avancer(100)
# tortue.tourner(90)
# tortue.avancer(100)
# print(tortue.direction)

# root.mainloop()


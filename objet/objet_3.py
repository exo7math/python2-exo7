
##############################
# Programmation objet
##############################

##############################
# Rappel de l'activité 2 - Tortue
##############################

##############################
## Question 1  ##


class TortueBasique:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.trace = True
        self.couleur = 'red'

    def renvoyer_xy(self):
        return self.x, self.y

    def aller_a_xy(self,x,y):
        x0 = self.x  # Position actuelle
        y0 = self.y

        self.x = x   # Nouvelle position
        self.y = y

        if self.trace:
            canvas.create_line(x0,y0,x,y,fill=self.couleur,width=5)
        return

    def abaisser_stylo(self):
        self.trace = True

    def relever_stylo(self):
        self.trace = False

    def changer_couleur(self,couleur):
        self.couleur = couleur


   
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

    def sorienter_vers(self,other):
        x1,y1 = self.x, self.y
        x2,y2 = other.x, other.y
        angle = 360/(2*pi)*atan2(y2-y1,x2-x1)
        self.direction = angle


# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

print("--- Objet : TortueTournante() ---")

# tortue = TortueTournante()

# tortue.aller_a_xy(100,100)
# tortue.avancer(100)
# tortue.tourner(90)
# tortue.avancer(100)
# print(tortue.direction)

tortue1 = TortueTournante()
tortue2 = TortueTournante()
tortue2.changer_couleur('blue')
tortue2.relever_stylo()
tortue2.aller_a_xy(700,1)
tortue2.abaisser_stylo()
tortue2.fixer_direction(90)

for i in range(400):
    tortue2.avancer(1)
    tortue1.sorienter_vers(tortue2)
    tortue1.avancer(2)
root.mainloop()


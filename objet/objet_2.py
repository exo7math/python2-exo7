
##############################
# Programmation objet
##############################

##############################
# Activité 2 - Tortue
##############################

##############################
## Question 1  ##

class TortueBasique:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.trace = True
        self.couleur = 'red'

    # Q1
    def renvoyer_xy(self):
        return self.x, self.y

    # Q2
    def aller_a_xy(self,x,y):
        x0 = self.x  # Position actuelle
        y0 = self.y

        self.x = x   # Nouvelle position
        self.y = y

        if self.trace:
            canvas.create_line(x0,y0,x,y,fill=self.couleur,width=5)
        return

    # Q3
    def abaisser_stylo(self):
        self.trace = True

    def relever_stylo(self):
        self.trace = False

    def changer_couleur(self,couleur):
        self.couleur = couleur

       
# Fenêtre tkinter
from tkinter import *
root = Tk()      
canvas = Canvas(root, width=800, height=600, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

tortue = TortueBasique()

tortue.aller_a_xy(100,100)
tortue.relever_stylo()
tortue.aller_a_xy(200,100)
tortue.abaisser_stylo()
tortue.aller_a_xy(100,200)

root.mainloop()

# print("--- Objet : TortueBasique() ---")
# print(tortue.renvoyer_xy())

##############################
## Question 4 ##

from math import *

tortue1 = TortueBasique()
tortue2 = TortueBasique()
tortue2.changer_couleur('blue')
tortue3 = TortueBasique()
tortue3.changer_couleur('orange')
# tortue4 = TortueBasique()
# tortue4.changer_couleur('green')

for i in range(0,400):
    tortue1.aller_a_xy(3/2*i,i)
    tortue2.aller_a_xy(i,5*sqrt(i))
    x1,y1 = tortue1.renvoyer_xy()
    x2,y2 = tortue2.renvoyer_xy()
    x3,y3 = round((x1+x2)/2), round((y1+y2)/2)
    tortue3.aller_a_xy(x3,y3)

    # if i%20 == 0:
    #     tortue4.aller_a_xy(x1,y1)
    #     tortue4.aller_a_xy(x2,y2)

root.mainloop()
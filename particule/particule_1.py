
##############################
# Particules
##############################

from math import *
from time import *


##############################
# Activité 1 - Particule
##############################

class Particule():

    def __init__(self,x,y,vx,vy,m):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.m = m

    def __str__(self):
        ligne = "("+str(self.x)+","+str(self.y)+"),("+str(self.vx)+", "+str(self.vy)+"), "+str(self.m)
        return ligne

    def action_vitesse(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

    def action_gravite(self,gravite=0.2):
        self.vy = self.vy - gravite

    def action_frottement(self,frottement=0.005,exposant=2):
        vx,vy,m = self.vx,self.vy,self.m
        vitesse = sqrt(vx**2+vy**2)
        self.vx = vx - 1/m * frottement * (vitesse**exposant) * (vx/vitesse)
        self.vy = vy - 1/m * frottement * (vitesse**exposant) * (vy/vitesse)

    def affiche(self,avec_fleche=False):
        x,y,vx,vy,m = self.x,self.y,self.vx,self.vy,self.m
        i,j = xy_vers_ij(x,y)
        
        echelle = 1
        if avec_fleche:
            fleche = canvas.create_line(i,j,i+vx*echelle,j-vy*echelle,fill="blue",arrow="last",width=4)
            
        rayon = min(max(1,2*sqrt(m)),15)
        disque = canvas.create_oval(i-rayon,j-rayon,i+rayon,j+rayon,fill="red")

    def rebondir_si_bord_atteint(self):
        x,y = self.x,self.y
        i,j = xy_vers_ij(x,y)
        if i <= 0 or i >= Largeur:
            self.vx = -self.vx
        if j <= 0 or j >= Hauteur:
            self.vy = -self.vy

    def mouvement(self):
        self.action_vitesse()
        self.action_gravite()
        self.action_frottement()
        self.rebondir_si_bord_atteint()            
        # self.affiche()



# Exemple
print("--- Objet : Particule() ---")
p1 = Particule(-100,100,10,10,1)
print(p1)



# Constantes pour l'affichage
Largeur = 800
Hauteur = 600

# Conversion de coordonnées
def xy_vers_ij(x,y):
    i = Largeur//2 + x
    j = Hauteur//2 - y
    return (i,j)

# Fenêtre tkinter
from tkinter import *

root = Tk()      
canvas = Canvas(root, width=Largeur, height=Hauteur, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Exemple 1 - Une particule fixe
p1 = Particule(-100,200,70,30,5)
print(p1)
p1.affiche(avec_fleche=True)

# Exemple 2 - Une particule fixe (sans flèche)
p2 = Particule(100,200,70,30,15)
print(p2)
p2.affiche()

# Exemple 3 - Une particule en mouvement linéaire
p = Particule(-250,50,10,5,1)
p.affiche()
for k in range(40):
    p.action_vitesse()
    p.affiche()

# Exemple 4 - Une particule sous l'action de la gravité,
# avec frottements et avec rebonds
p = Particule(-360,-107,10,15,5)
p.affiche()
for k in range(198):
    p.action_vitesse()
    p.action_gravite(gravite=1)
    p.action_frottement(frottement=0.01,exposant=1.8)
    p.affiche()
    p.rebondir_si_bord_atteint()

root.mainloop()

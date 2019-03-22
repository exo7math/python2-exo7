
##############################
# Particules
##############################

from math import *
from time import *


##############################
# Rappel - Activité 1 - Particule
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
        self.action_gravite()
        self.action_frottement()
        self.rebondir_si_bord_atteint()            
        self.action_vitesse()
        # self.affiche()



##############################
# Activité 3 - Planètes
##############################

class Planete(Particule):

    def action_attraction(self,other,G=100):
        x1, y1, vx1, vy1, m1 = self.x,self.y,self.vx,self.vy,self.m
        x2, y2, vx2, vy2, m2 = other.x,other.y,other.vx,other.vy,other.m

        x = x2-x1
        y = y2-y1
        r = sqrt(x**2+y**2)  # Distance entre les corps

        gx = G*m1*m2/(r**2) * x/r
        gy = G*m1*m2/(r**2) * y/r

        self.vx = self.vx + gx/m1
        self.vy = self.vy + gy/m1


    def mouvement(self):
        self.action_vitesse()


class TkPlanete(Planete):

    def __init__(self,x,y,vx,vy,m,couleur="red"):
        Particule.__init__(self,x,y,vx,vy,m)
        self.couleur = couleur
        # Creation de l'objet tkinter
        i,j = xy_vers_ij(x,y)
        rayon = 2*min(max(1,m),10)
        disque = canvas.create_oval(i-rayon,j-rayon,i+rayon,j+rayon,fill=self.couleur)
        self.id = disque

    def affiche(self,avec_trace=False):
        # Trace (option)
        if avec_trace:
            x,y,m = self.x, self.y, self.m
            i,j = xy_vers_ij(x,y)
            rayon = 2*min(max(2,m),10)//2
            canvas.create_oval(i-rayon,j-rayon,i+rayon,j+rayon,fill='gray')
        # Mouvement
        canvas.move(self.id,self.vx,-self.vy)




##############################  

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


# # Deux astres : Terre et Soleil
# soleil = TkPlanete(0,0,0,0,100,"yellow")
# terre = TkPlanete(-200,0,0,-5,3,"blue")

# for k in range(140):
#     terre.action_attraction(soleil)
#     terre.mouvement()
#     terre.affiche(avec_trace=True)
#     canvas.update()
#     sleep(0.01)

# root.mainloop()


# On peut remplacer la Terre par une comète
# soleil = TkPlanete(0,0,0,0,100,"yellow")
# comete = TkPlanete(-300,-200,6,0,5,"green")


# for k in range(80):
#     comete.action_attraction(soleil)
#     comete.mouvement()
#     comete.affiche(avec_trace=True)
#     canvas.update()
#     sleep(0.01)

# root.mainloop()

# Trois planètes : Terre et Soleil et Mars

soleil = TkPlanete(0,0,0,0,100,"yellow")
terre = TkPlanete(-200,0,0,-5,3,"blue")
mars = TkPlanete(-300,0,0,-5,2,"red")

for k in range(200):
    terre.action_attraction(soleil)
    terre.action_attraction(mars)
    terre.mouvement()
    terre.affiche(avec_trace=True)
    mars.action_attraction(soleil)
    mars.action_attraction(terre)
    mars.mouvement()
    mars.affiche(avec_trace=True)
    
    canvas.update()
    sleep(0.02)

root.mainloop()

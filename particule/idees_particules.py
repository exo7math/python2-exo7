
##############################
# Particules
##############################

from math import *
from random import *
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

# Test - Une particule
# p1 = Particule(-100,200,70,30,5)
# print(p1)
# p1.affiche(avec_fleche=True)

# p3 = Particule(100,200,70,30,15)
# print(p3)
# p3.affiche(avec_fleche=False)

# p = Particule(-360,-107,10,15,5)
# p.affiche(avec_fleche=False)
# for k in range(198):
#     p.action_vitesse()
#     p.action_gravite(gravite=1)
#     p.action_frottement(frottement=0.01,exposant=1.8)
#     p.affiche(avec_fleche=False)
#     p.rebondir_si_bord_atteint()

# Test - Plusieurs particules
# liste_particules = [Particule(-300,10,5,2*j,3) for j in range(-5,5)]
# for k in range(200):
#     for p in liste_particules:
#         p.mouvement()
#         p.affiche()
    
# root.mainloop()



##############################
# Activité 2 - Particules en mouvement
##############################

class TkParticule(Particule):

    def __init__(self,x,y,vx,vy,m,couleur="red"):
        Particule.__init__(self,x,y,vx,vy,m)
        self.couleur = couleur
        # Creation de l'objet tkinter
        i,j = xy_vers_ij(x,y)
        rayon = min(max(1,m),10)
        disque = canvas.create_oval(i-rayon,j-rayon,i+rayon,j+rayon,fill=self.couleur)
        self.id = disque

    def affiche(self):
        canvas.move(self.id,self.vx,-self.vy)
        






##############################
# Choix d'une couleur

def hasard_couleur():
    R,V,B = randint(0,255),randint(0,255),randint(0,255)
    couleur = '#%02x%02x%02x' % (R%256, V%256, B%256)
    return couleur


# Test - Une particule en mouvement
# p = TkParticule(-300,10,5,2,10)
# for k in range(500):
#     p.mouvement()
#     p.affiche()
#     canvas.update()
#     sleep(0.05)

# root.mainloop()

# mes_couleurs = [hasard_couleur() for j in range(10)]
# print(mes_couleurs)
mes_couleurs = ['#8963bc', '#56988b', '#3ef562', '#120cad', '#3e4b21', '#f8e328', '#c8ee51', '#c55cdd', '#1926c5', '#1f6cea']
# Test - Plusieurs particules en mouvement
liste_particules = [TkParticule(-350,0,10,j,5,couleur=mes_couleurs[j]) for j in range(10)]
for k in range(100):
    for p in liste_particules:
        p.mouvement()
        p.affiche()

    canvas.update()
    sleep(0.05)

root.mainloop()


##############################
# Activité 3 - Planete
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
        rayon = min(max(1,m),10)
        disque = canvas.create_oval(i-rayon,j-rayon,i+rayon,j+rayon,fill=self.couleur)
        self.id = disque

    def affiche(self):
        canvas.move(self.id,self.vx,-self.vy)


# Deux planètes : Terre et Soleil
soleil = TkPlanete(0,0,0,0,100,"yellow")
terre = TkPlanete(-100,0,5,-10,4,"blue")



# for k in range(200):
#     terre.action_attraction(soleil)
#     terre.mouvement()
#     terre.affiche()
#     canvas.update()
#     sleep(0.04)

# root.mainloop()


# Trois planètes : Terre et Soleil et Mars
# mars = TkPlanete(200,0,-2,7,3,"red")

# for k in range(200):
#     terre.action_attraction(soleil)
#     terre.action_attraction(mars)
#     terre.mouvement()
#     terre.affiche()
#     mars.action_attraction(soleil)
#     mars.action_attraction(terre)
#     mars.mouvement()
#     mars.affiche()
    
#     canvas.update()
#     sleep(0.04)

# root.mainloop()

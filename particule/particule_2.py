
##############################
# Particules
##############################

from math import *
from random import *
from time import *


##############################
# Rappels - Activité 1 - Particule
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
# Activité 2 - Particules en mouvement

class TkParticule(Particule):

    def __init__(self,x,y,vx,vy,m,couleur="red"):
        Particule.__init__(self,x,y,vx,vy,m)
        self.couleur = couleur
        # Creation de l'objet tkinter
        i,j = xy_vers_ij(x,y)
        rayon = min(max(1,m),10)
        disque = canvas.create_oval(i-rayon,j-rayon,i+rayon,j+rayon,fill=self.couleur)
        self.id = disque

    def affiche(self,avec_trace=False): 
        # Trace (option)
        if avec_trace:
            x,y,m = self.x, self.y, self.m
            i,j = xy_vers_ij(x,y)
            rayon = min(max(2,m),10)//2
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

##############################
# Choix d'une couleur

def hasard_couleur():
    R,V,B = randint(0,255),randint(0,255),randint(0,255)
    couleur = '#%02x%02x%02x' % (R%256, V%256, B%256)
    return couleur




# Exemple 1 - Une particule en mouvement
# p = TkParticule(-300,10,5,2,10)
# for k in range(500):
#     p.mouvement()
#     p.affiche()
#     canvas.update()
#     sleep(0.05)

# root.mainloop()

# Exemple 2 - Plusieurs particules en mouvement
# Choix des couleurs
# mes_couleurs = [hasard_couleur() for j in range(10)]
# print(mes_couleurs)
mes_couleurs = ['#8963bc', '#56988b', '#3ef562', '#120cad', '#3e4b21', '#f8e328', '#c8ee51', '#c55cdd', '#1926c5', '#1f6cea']
# Plusieurs particules en mouvement
liste_particules = [TkParticule(-350,0,10,j,5,couleur=mes_couleurs[j]) for j in range(10)]
for k in range(110):
    for p in liste_particules:
        p.mouvement()
        p.affiche(avec_trace=True)

    canvas.update()
    sleep(0.05)

root.mainloop()


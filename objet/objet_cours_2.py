
##############################
# Programmation objet
##############################

##############################
# Cours - Programmation objet - Héritage - Ennemis
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
mechant.affiche_force()
mechant.perd_vie(50)
mechant.affiche_vie()

super_mechant = Zombie(7,2,200,200)
super_mechant.perd_vie(50)
super_mechant.affiche_vie()


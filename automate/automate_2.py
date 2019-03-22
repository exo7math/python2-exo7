
##############################
# Automates
##############################

##############################
# Activité 2 - Automate linéaire
##############################

##############################
## Question 1 ##


def cellule_suivante(a,b,c,regle):
    """ Calcule la couleur 0/1 de la cellule suivante selon 
    les trois cellules a,b,c du dessus selon la règle donnée """

    rang = 4*a+2*b+c
    new_cellule = regle[rang]
    return new_cellule


# Test
print("--- Test affichage règle ---")
regle = [0, 0, 1, 0, 1, 1, 0, 1]   
print(cellule_suivante(0,0,1,regle))



##############################
## Question 2 ##

def affiche_regle(regle):
    """ Affichage de la règle """
    for a in range(2):
        for b in range(2):
            for c in range(2):
                rang = 4*a+2*b+c
                cellule = regle[rang]
                print(a,b,c," -> ",cellule)
    return


# Test
print("--- Test affichage règle ---")
regle = [0, 0, 1, 0, 1, 1, 0, 1]   
affiche_regle(regle)


##############################
## Question 3 ##

def ligne_suivante(ligne,regle):
    """ Calcule la ligne de cellules suivante """

    p = len(ligne)
    nouvelle_ligne = []

    for j in range(p):
        if j == 0:
            a,b,c = 0, ligne[j], ligne[j+1]
        elif j == p-1:
            a,b,c = ligne[j-1], ligne[j], 0
        else:
            a,b,c = ligne[j-1], ligne[j], ligne[j+1]

        cellule = cellule_suivante(a,b,c,regle)
        nouvelle_ligne = nouvelle_ligne + [cellule]

    return nouvelle_ligne


# Test
print("--- Test ligne suivante ---")

regle = [0, 0, 1, 0, 1, 1, 0, 1]
ligne = [0,0,1,0,1]
next_ligne = ligne_suivante(ligne,regle)
print(ligne)
print(next_ligne)

##############################
## Question 4 ##

def plusieurs_lignes(n,ligne,regle):
    """ Calcule n lignes suivantes """

    print(ligne)
    for __ in range(n):
        ligne = ligne_suivante(ligne,regle)
        print(ligne)
    return

# Test
print("--- Test plusieurs lignes suivantes ---")
regle = [0, 0, 1, 0, 1, 1, 0, 1]

print("Règle : ",regle)

ligne = [0]*5 + [1] + [0]*5
plusieurs_lignes(4,ligne,regle)

##############################
## Question 5 ##


def afficher_lignes(n,ligne,regle):
    """ Affichage de n lignes à partir 
    d'une ligne initiale et d'une règle """

    p = len(ligne)
    for i in range(n):
        for j in range(p):
            if ligne[j] == 1:
                couleur = "black"
            else:
                couleur = "white"
            canvas.create_rectangle(10+j*echelle,10+i*echelle,10+(j+1)*echelle,10+(i+1)*echelle,fill=couleur,outline="red")
        ligne = ligne_suivante(ligne,regle)  
    return

from tkinter import *

root = Tk()

canvas = Canvas(root, width=1000, height=800, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Echelle 
echelle = 30


# Automate
regle = [0, 0, 1, 0, 1, 1, 0, 1]  # Règle 45
print("Règle : ",regle)
affiche_regle(regle)
ligne = [0]*30 + [1] + [0]*30

# afficher_lignes(30,ligne,regle)

# root.mainloop()



##############################
## Question 7 ##

def definir_regle(numero):
    """ Définir une règle à partir d'un numéro entre 0 et 255 """

    regle = []
    for __ in range(8):
        r = numero % 2
        regle = [r] + regle
        numero = numero // 2
    return regle


# Test
print("--- Numérotation des règles ---")
numero = 45
regle = definir_regle(numero)
print("Numéro :",numero)
print("Règle : ",regle)
affiche_regle(regle)


##############################
def conversion_standard_vers_perso(numero):
    
    liste = definir_regle(numero)
    print(liste)
    perso = sum([2**i * liste[i] for i in range(8)])
    return perso

# Test
print("--- Conversion numérotation standard ---")
std = 106
numero = conversion_standard_vers_perso(std)
print(std,"->", numero)
print(definir_regle(numero))


##############################
## Question 7 ##

# Chaotique
numero = 120  # std = 30
numero = 106  # std = 86

# Sierpinski
# numero = 90  # std = 90

# Deux voyageurs
# numero = 42  # std = 84

# Pli
# numero = 136  # std = 17

# Monstre qui fait peur
# numero = 150 # std = 105

# Sierpinski étiré ?
# numero = 135 # std = 225

# Pyramide
numero = 92  # std = ?

# Coulée
numero = 98  # std = ?

# Exemple du cours
numero = 45

numero = 105

regle = definir_regle(numero)

ligne = [0]*15 + [1] + [0]*15

afficher_lignes(40,ligne,regle)

root.mainloop()
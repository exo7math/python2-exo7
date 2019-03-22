
##############################
# Automates
##############################



##############################
# Activité 1 - 
##############################


# Une suite logique

def suivant(mot):
    
    lettre_prec = ""
    nb = 0

    nouv_mot = ""

    for lettre in mot:
        if (lettre_prec == "") or (lettre == lettre_prec):
            nb = nb + 1
        else:
            nouv_mot = nouv_mot + str(nb) + lettre_prec
            nb = 1

        lettre_prec = lettre

    # Fin
    nouv_mot = nouv_mot + str(nb) + lettre_prec

    return nouv_mot

def itere(n,mot):
    for __ in range(n):
        print(mot)
        mot = suivant(mot)
    return mot

# Test
#print(suivant("11"))
itere(10,"1")

##############################
## Question 1 ##

##############################
## Question 2 ##

##############################
## Question 3 ##



##############################
# Activité 2 - 
##############################



def cellule_suivante(a,b,c,regle):
    rang = 4*a+2*b+c
    new_cellule = regle[rang]
    return new_cellule


def definir_regle(numero):
    regle = []
    for __ in range(8):
        r = numero % 2
        regle = [r] + regle
        numero = numero // 2
    return regle


def affiche_regle(regle):
    for a in range(2):
        for b in range(2):
            for c in range(2):
                cellule = cellule_suivante(a,b,c,regle)
                print(a,b,c," -> ",cellule)
    return

# Test
print("--- Test règle et cellule suivante ---")
numero = 30
regle = definir_regle(numero)
print("Numéro :",numero)
print("Règle : ",regle)
affiche_regle(regle)


def ligne_cellules_suivantes(ligne,regle):
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
print("--- Test règle et cellule suivante ---")
numero = 30
regle = definir_regle(numero)
ligne = [0,0,1,0,0]
ligne_suivante = ligne_cellules_suivantes(ligne,regle)
print(ligne)
print(ligne_suivante)


def plusieurs_lignes(n,ligne,regle):
    print(ligne)
    for __ in range(n):
        ligne = ligne_cellules_suivantes(ligne,regle)
        print(ligne)
    return

# Test
print("--- Test règle et cellule suivante ---")
numero = 202
regle = definir_regle(numero)
print("Numéro :",numero)
print("Règle : ",regle)
affiche_regle(regle)
ligne = [0]*15 + [1] + [0]*15
plusieurs_lignes(10,ligne,regle)



def afficher_lignes(n,ligne,regle):
    p = len(ligne)
    for i in range(n):
        for j in range(p):
            if ligne[j] == 1:
                couleur = "black"
            else:
                couleur = "white"
            canvas.create_rectangle(10+j*echelle,10+i*echelle,10+(j+1)*echelle,10+(i+1)*echelle,fill=couleur,outline="red")
        ligne = ligne_cellules_suivantes(ligne,regle)  
    return

from tkinter import *

root = Tk()

canvas = Canvas(root, width=1000, height=800, background="white")
canvas.pack(side=LEFT, padx=5, pady=5)

# Echelle 
echelle = 20

afficher_lignes(30,ligne,regle)

root.mainloop()
##############################
## Question 1 ##

##############################
## Question 2 ##

##############################
## Question 3 ##


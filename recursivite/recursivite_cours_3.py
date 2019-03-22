
##############################
# Récursivité
##############################

##############################
# Cours 3 - Diviser pour régner
##############################        


def somme(liste):
    if len(liste) == 0:
        return 0
    if len(liste) == 1:
        return liste[0]
    else:
        n = len(liste)
        liste_gauche = liste[:n//2]
        liste_droite = liste[n//2:]

        Sgauche = somme(liste_gauche)
        Sdroite = somme(liste_droite)
        S = Sgauche + Sdroite
        return S

# Test
print("--- Somme ---")
liste = [7,5,3,9,1,12]
print("liste =",liste)
print("somme = ",somme(liste)) 



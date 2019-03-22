
##############################
# Calculs en parallèle
##############################



##############################
# Activité 3 - Listes
##############################

##############################
## Question 1 ##

# Avec 2 processeurs

def maximum(liste):
    """ Maximum d'une liste par formule récursive en séparant la liste en 2 """
    infini = 1000
    if len(liste)==0: return -infini
    if len(liste)==1: return liste[0]
    k = len(liste)//2
    liste_gauche = liste[:k]
    liste_droite = liste[k:]
    max_gauche = maximum(liste_gauche)
    max_droite = maximum(liste_droite)
    maxi = max(max_gauche,max_droite)
    return maxi


# Test
print("--- Maximum ---")
liste = [6,3,8,10,4]
print(liste)
print(maximum(liste))


##############################
## Question 1bis ##

# Renvoie l'élément juste avant le maximum
# A faire

def sous_maximum(liste):
    pass


##############################
## Question 2 ##

def extraire_pairs(liste):
    """ Renvoie les éléments pairs d'une liste (fonction récursive) """
    if len(liste)==0: return []
    if len(liste)==1:
        if liste[0]%2 == 0:
            return [liste[0]]
        else:
            return []

    # On coupe la liste en 2
    k = len(liste)//2
    liste_gauche = liste[:k]
    liste_droite = liste[k:]
    liste_paire_gauche = extraire_pairs(liste_gauche)
    liste_paire_droite = extraire_pairs(liste_droite)
    liste_paire = liste_paire_gauche + liste_paire_droite 
    return liste_paire

print("--- Extraire les termes pairs ---")
liste = [6,8,7,3,9,10,11,5,8,2]
print(liste)
print(extraire_pairs(liste))


##############################
## Question 3 ##

# Avec 2 processeurs 

def premier_rang(liste):
    """ Renvoie le rang du premier élément non nul (fonction récursive) """
    if len(liste)==0: return None

    if len(liste)==1:
        if liste[0]==0:
            return None
        else:
            return 0

    k = len(liste)//2
    liste_gauche = liste[:k]
    liste_droite = liste[k:]
    premier_rang_gauche = premier_rang(liste_gauche)
    premier_rang_droite = premier_rang(liste_droite)
    if premier_rang_gauche != None:
        return premier_rang_gauche
    elif premier_rang_droite != None:
        return k + premier_rang_droite
    else:
        return None

# Test
print("--- Premier rang non nul ---")
liste = [0,0,0,0,0,1,0,1,1,0]
print(liste)
print(premier_rang(liste))


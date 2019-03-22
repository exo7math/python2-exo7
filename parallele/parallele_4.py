
##############################
# Calculs en parallèle
##############################


##############################
# Activité 4 - Sommes partielles (prefix-sum)
##############################

##############################
## Question 1 ##

def sommes_partielles(liste):
    """ Liste des sommes partielles d'une liste """
    liste_sommes = []
    s = 0
    for x in liste:
        s = s + x 
        liste_sommes += [s]
    return liste_sommes

# Test
print("--- Sommes partielles (prefix-sum) séquentiel ---")
liste = [1,2,3,4,5,6,7,8]
liste = [10,4,0,2,1,0,3,21]
print(liste)
print(sommes_partielles(liste))

##############################
## Question 2 ##

def sommes_partielles_recursif(liste):
    """ Liste des sommes partielles d'une liste (fonction récursive) 
    C'esl l'algorithme 'prefix-sum' 
    La liste doit être de longueur une puissance de 2 """

    n = len(liste)
    if n==1: return [liste[0]]
    
    sous_liste = [liste[2*i] + liste[2*i+1] for i in range(n//2)]
    # print(sous_liste)

    liste_remontee = sommes_partielles_recursif(sous_liste)

    print(liste_remontee)

    liste_descente = [liste[0]] 
    for i in range(1,n):    
        # print(liste,sous_liste,liste_remontee,i,i//2)
        if i%2 == 0:
            liste_descente += [liste_remontee[i//2-1] + liste[i]]
        else:
            liste_descente += [liste_remontee[(i-1)//2]]

    return liste_descente


# Test
print("--- Sommes partielles (prefix-sum) récursif ---")
liste = [1,2,3,4,5,6,7,8] 
print(sommes_partielles_recursif(liste))
print(sommes_partielles(liste))



##############################
## Question 3 ##


def selection(liste,filtre):
    """ Application. Filtrage d'une liste en conservant l'ordre :
    on ne conserve que les éléments de la liste associé à 1 dans le filtre
    L'algorithme utilise le calcul des sommes partielles précédent et est donc parallèlisable """
    
    sommes = sommes_partielles_recursif(filtre)

    n =sommes[-1]  # Nombre d'éléments à garder
    selec = [0]*n  # Liste à remplir 

    for i in range(len(liste)):  # peut se faire en parallèle
        if filtre[i] != 0:
            selec[sommes[i]-1] = liste[i]
    return selec

# Test
print("--- Rang non nul ---")
liste = [5,8,6,1,5,9,3,2]
filtre = [0,0,1,0,1,0,0,1]
# liste = [0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0]
print(liste)
print(filtre)
print(sommes_partielles_recursif(filtre))
print(selection(liste,filtre))

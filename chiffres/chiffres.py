
##############################
# Des chiffres et des lettres
##############################

##############################
# Activité 1 - Tirages au hasard
##############################

from random import *

##############################
## Question 1 ##

def tirage_total(Nmin=100,Nmax=999):
    return randint(Nmin,Nmax)

# Test
print("--- Nombre à obtenir ---")
total = tirage_total()
print(total)


##############################
## Question 2 ##

def tirage_chiffres(nb_chiffres=6):

    CHIFFRES = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,25,50,75,100]

    # Sans remise
    liste_choix = [c for c in CHIFFRES]
    liste = []
    for i in range(nb_chiffres):
        n = len(liste_choix)
        k = randint(0,n-1)
        liste += [liste_choix[k]]
        del liste_choix[k]
    return liste.sort()

# Test
print("--- Chiffres à jouer ---")
chiffres = tirage_chiffres()
print(chiffres)


##############################
## Question 3 ##
def operation(a,b,op):
    if op == '+':
        calcul = a + b
    elif op == '-':
        calcul = a - b
    elif op == '*':
        calcul = a * b
    elif op == '/':
        calcul = a / b
    return calcul          

##############################
# Activité 2 -  Recherche basique
##############################

##############################
## Pour le cours ##

print("--- Pour le cours ---")


chiffres = [2,3,5,6,8,10]           # Plaques disponibles
total = 18                          # Objectif

chiffres1 = list(chiffres)          # Copie
for c1 in chiffres1:                # Premier chiffre
    chiffres2 = list(chiffres1)     # Copie
    chiffres2.remove(c1)            # Retirer la plaque déjà tirée

    for op in ['+','*']:            # Opération

        for c2 in chiffres2:        # Second chiffre

            calcul = operation(c1,c2,op)   # Résultat du calcul

            if calcul == total:                 # Total atteint ?
                print("Trouvé !",c1,op,c2,'=',calcul)


print("--- Fin pour le cours ---")

##############################
# Pour le cours 
## Activité ##

def recherche_basique(total,chiffres):

  OPERATIONS = ['+','-','*','/']
  
  chiffres1 = list(chiffres)

  for c1 in chiffres1:
    if c1 == total: 
      print("Trouvé !",c1)

    chiffres2 = list(chiffres1)
    chiffres2.remove(c1) 
           
    for op1 in OPERATIONS:

      for c2 in chiffres2:
        calcul1 = operation(c1,c2,op1)

        if calcul1 == total: 
          print("Trouvé !",c1,op1,c2,'=',total) 

        chiffres3 = list(chiffres2)
        chiffres3.remove(c2)

        for op2 in OPERATIONS:

          for c3 in chiffres3:
            calcul2 = operation(calcul1,c3,op2)

            if calcul2 == total: 
              print("Trouvé !",
                    c1,op1,c2,'=',calcul1,",",
                    calcul1,op2,c3,'=',total)

            chiffres4 = list(chiffres3)
            chiffres4.remove(c3)

            for op3 in OPERATIONS:
    
              for c4 in chiffres4:
                calcul3 = operation(calcul2,c4,op3)
    
                if calcul3 == total: 
                  print("Trouvé !",
                        c1,op1,c2,'=',calcul1,",",
                        calcul1,op2,c3,'=',calcul2,",",
                        calcul2,op3,c4,'=',total)
  
                chiffres5 = list(chiffres4)
                chiffres5.remove(c4)
  
                for op4 in OPERATIONS:
    
                  for c5 in chiffres5:
                    calcul4 = operation(calcul3,c5,op4)
        
                    if calcul4 == total: 
                      print("Trouvé",
                            c1,op1,c2,'=',calcul1,",",
                            calcul1,op2,c3,'=',calcul2,",",
                            calcul2,op3,c4,'=',calcul3,",",
                            calcul3,op4,c5,'=',total),",",
      
                    chiffres6 = list(chiffres5)
                    chiffres6.remove(c5)

                    for op5 in OPERATIONS:
            
                      for c6 in chiffres6:
                        calcul5 = operation(calcul4,c6,op5)
            
                        if calcul5 == total: 
                          print("Trouvé !",
                                c1,op1,c2,'=',calcul1,",",
                                calcul1,op2,c3,'=',calcul2,",",
                                calcul2,op3,c4,'=',calcul3,",",
                                calcul3,op4,c5,'=',calcul4,",",
                                calcul4,op5,c6,'=',total)                              

  return

# Test
print("--- Recherche basique ---")
print(" -- Test 809 ---")
# recherche_basique(809,[2, 3, 6, 8, 75, 100])
print(" -- Test 779 ---")
# recherche_basique(779,[5, 6, 7, 8, 25, 50])

print(" -- Test 773 ---")
# recherche_basique(773,[2, 4, 6, 8, 10, 50])
print(" -- Test 769 ---")
# recherche_basique(769,[2, 4, 6, 8, 10, 50])
print(" -- Test 752 ---")
recherche_basique(756,[2, 4, 6, 8, 10, 50])

##############################
# Activité 3 - Recherche d'une somme
##############################

def atteindre_somme(S,chiffres):
    # Cas terminaux
    if S == 0:
        return []
    if S < 0:
        return None

    # Cas général
    for x in chiffres:     
        parcours = atteindre_somme(S-x,chiffres)
        if parcours != None:
            parcours = [x] + parcours
            return parcours

    return None

# Test
print("--- Atteindre une somme ---")
chiffres = [5, 7, 11]
somme = 19
print(chiffres)
print(somme)
parcours = atteindre_somme(somme,chiffres)
print("Parcours :",parcours)
if parcours:
    print("Vérification :",sum(parcours))



##############################
# Activité 4 - Le compte est bon (recherche récursive).
##############################

def compte_est_bon(total,chiffres):
    # Cas terminaux
    if total in chiffres:
        return [str(total)]
    if len(chiffres) < 2:
        return None

    # Cas général
    chiffres.sort()    # Tri de la liste...
    chiffres.reverse() # ...du plus grand au plus petit

    n = len(chiffres)
    for i in range(n-1):
        for j in range(i+1,n):
            c1 = chiffres[i]
            c2 = chiffres[j]
            # print(c1,c2)
                      
            for op in ['+','-','*','/']:
                nouv_chiffres = [cc for cc in chiffres]
                nouv_chiffres.remove(c1)
                nouv_chiffres.remove(c2)  
                
                calcul_str =  str(c1) + op + str(c2)              
                calcul = operation(c1,c2,op)
                
                if (calcul>0) and isinstance(calcul,int):  # Evite la division par zéro ou div. non entière
                    nouv_chiffres += [calcul]

                    parcours = compte_est_bon(total,nouv_chiffres)
                    if parcours != None:
                        operation_str = calcul_str + '=' + str(eval(calcul_str))
                        nouv_parcours = [operation_str] + parcours 
                        return nouv_parcours

    return None

# Test
print("--- Le compte est bon ---")
chiffres = [3,5,7,2]
total = 72
print("Chiffres :",chiffres)
print("Total :",total)
parcours = compte_est_bon(total,chiffres)
print("Parcours :",parcours)


# Test
print("--- Tests réel ---")
# Exemple facile
print("  -- Facile --")
chiffres = [2, 3, 7, 9, 9, 25]
total = 457
print("Chiffres :",chiffres)
print("Total :",total)
parcours = compte_est_bon(total,chiffres)
print("Parcours :",parcours)


# Exemple long
print("  -- Impossible --")

# chiffres = [2, 4, 5, 6, 8, 10]
# total = 851
print("Chiffres :",chiffres)
print("Total :",total)
parcours = compte_est_bon(total,chiffres)
print("Parcours :",parcours)

# Exemple très long (pas possible)
chiffres = [1, 6, 4, 1, 8, 4]
total = 970


# Recrhche de totaux réalisable à partir d'une liste de chiffres fixés
# chiffres = [2, 4, 5, 6, 8, 10]  # 114 totaux pas trouvés
# chiffres = [1, 2, 5, 7, 75, 100]  # 0 totaux pas atteints
# chiffres = [10, 10, 25, 50, 75, 100] # beaucoup pas atteints
chiffres = [2, 4, 6, 8, 10, 50]
print("Chiffres :",chiffres)
nb_echec = 0
for total in range(750,760):
    parcours = compte_est_bon(total,chiffres)
    if parcours == None:
        print("Total pas atteint :",total)
        nb_echec +=1
print("Nombre de totaux pas atteints",nb_echec)


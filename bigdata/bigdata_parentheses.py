
##############################
# Big data
##############################


from random import *

##############################
# Activité - Parenthèses
##############################

##############################
# Rappels activité "Piles" du livre 1
##############################

def empile(element):
    global pile
    pile = pile + [element]
    return None

def depile():
    global pile
    sommet = pile[len(pile)-1]
    pile = pile[0:len(pile)-1]
    return sommet   

def pile_est_vide():
    if len(pile) == 0:
        return True
    else:
        return False


def parentheses_correctes(expression):
    """ Teste si une expression est bien parenthésée
    Entrée : un expression (chaîne de caractère)
    Sortie : vrai/faux
    Action : utilise une pile """
    
    global pile
    pile = []    # On part d'une pile vide

    for car in expression:
        if car == "(":
            empile(car)

        if car == ")":
            if pile_est_vide():
                return False     # Problème : il manque une "(" 
            else:
                depile()

    # A la fin : 
    if pile_est_vide():
        return True
    else: 
        return False


def crochets_parentheses_correctes(expression):
    """ Teste si une expression a des crochets et des parenthèses bien placées
    Entrée : un expression (chaîne de caractère)
    Sortie : vrai/faux
    Action : utilise une pile """
    
    global pile
    pile = []    # On part d'une pile vide

    for car in expression:

        if car == "(" or car == "[":
            empile(car)
        
        if car == ")" or car == "]":
            if pile_est_vide():
                return False     # Problème : il manque "(" ou "[" 
            else:
                element = depile()
                if element == "[" and car == ")":
                    return False     # Problème du type [)
                if element == "(" and car == "]":
                    return False     # Problème du type (]

    # A la fin
    return pile_est_vide()

# Test
print("--- Vérification exacte - Parenthèses ---")       
exp = "()()(())(()(()))"  # Vrai
# exp = "()()(())((((()))"  # Faux
print(exp)
print("Verification exacte ok ?:",parentheses_correctes(exp))

print("--- Vérification exacte - Parenthèses et crochets ---")       
exp = "()()(())[[](())]"  # Vrai
# exp = "()[(())((((]))"  # Faux
print(exp)
print("Verification exacte ok ?:",crochets_parentheses_correctes(exp))



##############################
## Partie A - Parenthèses seules ##
##############################

print("\n=== Partie A. Parenthèses ===\n")

##############################
## Question 0 ##

def construction_parentheses(n):
    """ Constructions d'une expression aléatoire de longueur 2n 
    avec parenthèses cohérentes. """ 
    p = 0.5    # probalibilités
    exp = ""   # Expression
    pile = []  # Pile
    k = 0      # Nombre de pairs
    while k<n:
        x = random()    # Nb aléatoire 0 <= x < 1

        if 0 <= x < p:  # Parenthèses
            exp += "("
            pile.append(")")
            k = k+1

        if p <= x < 1 and len(pile)>0:  # Dépiler
            el = pile.pop()
            exp += el

    # A la fin vider la pile        
    while len(pile)>0:
        el = pile.pop()
        exp += el
        
    return exp                    

# Test
# print("--- Constructions d'une expression ---")
# exp = construction_parentheses(10)
# print(exp)
# print("Verif ok ?:",parentheses_correctes(exp))


##############################
## Question 2 ##

def test_parentheses(expression,p=101,a=2):
    """ Vérification probabiliste qu'une expression 
    est correctement parenthésées """

    # p est un nombre premier
    # a est un entier pour les parenthèses

    S = 0    # somme de contrôle
    h = 0    # hauteur
    for car in expression:
        if car == "(":
            h = h + 1
            S = (S + a**h) % p
        if car == ")":
            S = (S - a**h) % p
            h = h - 1
        if h < 0:
            return False

    if S == 0:
        return True
    else:
        return False


 # Test
print("--- Test probabiliste d'une expression : parenthèses ---")
exp = construction_parentheses(20)
print(exp)
exp = "()()(())(()(()))"  # Vrai
# exp = "()()(())((((()))"  # Faux
exp = ")("
print("Test proba ok ?:",test_parentheses(exp))         
print("Verification exacte ok ?:",parentheses_correctes(exp))


##############################
## Partie B - Parenthèses et crochets ##
##############################

print("\n=== Partie B. Parenthèses et crochets ===\n")

##############################
## Question 0 ##

def construction_crochets_parentheses(n):
    """ Constructions d'une expression aléatoire de longueur 2n 
    avec parenthèses et crochets cohérents. """ 
    p = 0.33    # probalibilités
    q = 0.66
    exp = ""   # Expression
    pile = []  # Pile
    k = 0      # Nombre de pairs
    while k<n:
        x = random()    # Nb aléatoire 0 <= x < 1

        if 0 <= x < p:  # Parenthèses
            exp += "("
            pile.append(")")
            k = k+1

        if p <= x < q:  # Crochets
            exp += "["
            pile.append("]")
            k = k+1

        if q <= x < 1 and len(pile)>0:  # Dépiler
            el = pile.pop()
            exp += el

    # A la fin vider la pile        
    while len(pile)>0:
        el = pile.pop()
        exp += el
        

    return exp                    

# Test
# print("--- Constructions d'une expression ---")
# exp = construction_crochets_parentheses(20)
# print(exp)
# print("Verif ok ?:",crochets_parentheses_correctes(exp))


##############################
## Question 1 ##

def test_crochets_parentheses(expression):
    p = 101  # un nombre premier
    a = 2    # entier pour les parenthèses
    b = 3    # entiers pour les crochets
    S = 0    # somme de contrôle
    h = 0    # hauteur
    for car in expression:
        if car == "(":
            h = h + 1
            S = (S + a**h) % p
        if car == ")":
            S = (S - a**h) % p
            h = h - 1
        if car == "[":
            h = h + 1
            S = (S + b**h) % p
        if car == "]":
            S = (S - b**h) % p
            h = h - 1
        if h < 0:
            return False

    if S == 0:
        return True
    else:
        return False

 # Test
print("--- Test probabiliste d'une expression : parenthèses et crochets ---")
exp = construction_crochets_parentheses(20)
exp = "[([[]][[[[(()[(()([((())[[]])]))])]]]])]"  # vrai
exp = "[[[()](()[((([[]])()(([[[]][()]]])))])]]"  # Faux
#exp = "[[[()](()[((([[]])()([[[[]][()]]])))])])"  # Faux
#exp = "[)(]"  # Faux
print(exp)

print("Test proba ok ?:",test_crochets_parentheses(exp))         
print("Verification exacte ok ?:",crochets_parentheses_correctes(exp))

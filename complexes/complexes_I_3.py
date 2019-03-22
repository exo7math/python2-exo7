
##############################
# Complexes I
##############################


##############################
# Activité 3 - Hack - Equation de degré 1
##############################

def solution_equation_lineaire(equation):
    """ 
    Résoud une équation linéaire réelle de degré 1
    Entrée : une chaîne de caractère sous la forme "3*(x+1) + x = 2*x+1"
    Sortie : la valeur de la solution x (par exemple ici renvoie -1)
    Remarque : utilise astucieusement les nombres complexes !
    """

    # Parties gauche et droite de l'équation 
    # Ex "3*(x+1) + x = 2*x+1" -> "3*(x+1) + x" et "2*x+1"
    eq_gd = equation.split("=")

    # On bascule tout à gauche 
    # Ex : on obtient "3*(x+1) + x - ( 2*x+1 )" (sous-entendu = 0)
    new_eq = eq_gd[0] + "- (" + eq_gd[1] + " )"  # 

    # On remplace les x par le nb complexe 1j
    # Ex :on obtient "3*(1j+1) + 1j - ( 2*1j+1 )"
    z_str = new_eq.replace("x","1j")

    # On évalue la chaîne
    # Ex : la chaîne devient le nb complexe z = 3*(1j+1) + 1j - ( 2*1j+1 )
    z = eval(z_str)

    # On récupère les parties réelle et imaginaire
    # Ex : a = 2, b = 2
    a = z.real
    b = z.imag

    # Solution de l'équation qui correspond en fait à "a + bx = 0"
    # Ex : sol = -1
    sol = -a/b

    return sol


# Test
print("--- Solution d'une équation linéaire réelle ---")
eq = "7*x+3 = 0"
# eq = "3*(x+1) + x = 2*x+1"
x = solution_equation_lineaire(eq)
print("Equation :",eq)
print("Solution :", x)


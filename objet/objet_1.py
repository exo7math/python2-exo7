
##############################
# Programmation objet
##############################


##############################
# Activité 1 - Matrice 2x2
##############################

class Matrice:

    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self):
        ligne1 = str(self.a) + " " + str(self.b) + "\n"
        ligne2 = str(self.c) + " " + str(self.d)
        return ligne1 + ligne2

    def trace(self):
        tr = self.a + self.d
        return tr

    def determinant(self):
        det = self.a*self.d - self.b*self.c
        return det

    def produit_par_scalaire(self,k):
        M = Matrice(k*self.a,k*self.b,k*self.c,k*self.d)
        return M

    def inverse(self):
        det = self.determinant()
        if det == 0:
            return None
        else:
            M = Matrice(self.d,-self.b,-self.c,self.a)
            MM = M.produit_par_scalaire(1/det)
        return MM       

    def __add__(self,other):
        M = Matrice(self.a+other.a,self.b+other.b,self.c+other.c,self.d+other.d)
        return M

    def __mul__(self,other):
        M = Matrice(self.a*other.a + self.b*other.c,
                    self.a*other.b + self.b*other.d,
                    self.c*other.a + self.d*other.c,
                    self.c*other.b + self.d*other.d
            )
        return M

# Test
print("--- Objet : Matrice() ---")

print("- Affichage -")
M = Matrice(1,2,3,4)
print(M)
M.__str__
print("Trace :",M.trace())
print("Déterminant : ",M.determinant())

print("- Produit par scalaire -")

MM = M.produit_par_scalaire(5)
print(MM)

print("- Inverse -")

print(M.inverse())

print("- Addition -")

M1 = Matrice(4,3,2,1)
M2 = Matrice(1,0,-1,1)
M3 = M1+M2
print(M3)

print("- Multiplication -")

M4 = M1*M2
print(M4)
print(M2*M1)

print("- Verif. inverse -")
M1 = Matrice(4,3,2,1)
M5 = M1.inverse()
# print(M5)
print(M1*M5)

# Application à Fibonnacci
print("- Fibonacci -")

M = Matrice(0,1,1,1)
n = 100
Mn = M
for k in range(n-1):
    Mn = Mn * M
print("n =",n)
print("Matrice puissance n :",Mn)
print("Print coeff. Fn (donné par d) :",Mn.d)

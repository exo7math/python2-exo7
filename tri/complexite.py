
##############################
# Tri - Compléxité
##############################


##############################
# Activité 1 - Notation grand O
##############################

from math import *

import matplotlib.pyplot as plt


def afficher_suite(u,couleur="red",N=10):
    liste_xy = [(n,u(n)) for n in range(N)]
    liste_un = [u(n) for n in range(N)]
    plt.plot(liste_un,color=couleur)
    for (x,y) in liste_xy:
        plt.scatter(x,y,color=couleur,s=15)

afficher_suite(lambda u:exp(u),couleur="brown",N=5)
afficher_suite(lambda u:u**2,couleur="red",N=6)
afficher_suite(lambda u:u,couleur="orange",N=26)
afficher_suite(lambda u:sqrt(u),couleur="green",N=41)
afficher_suite(lambda u:log(u+0.1),couleur="blue",N=41)


plt.axes().set_aspect('equal')
plt.xlim(xmin=0,xmax=40)
plt.ylim(ymin=0,ymax=25)
plt.grid()
# plt.show()


def est_grand_O(u,v,Nmin=10,Nmax=1000,k=10):
    ok = True 
    for n in range(Nmin,Nmax):
        if u(n) > k*v(n):
            ok = False
    return ok


print("--- Est grand O ---")
u = lambda n:n**2
# def u(n): return n**2
v = lambda n:2**n
print("Est grand O :",est_grand_O(u,v))

u = lambda n:n
v = lambda n:sqrt(n)
print("Est grand O :",est_grand_O(u,v))

u = lambda n:1000*n**2
v = lambda n:0.001*exp(n)
print("Est grand O :",est_grand_O(u,v,Nmin=20,Nmax=40))


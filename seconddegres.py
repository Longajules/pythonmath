from math import *

a = float(input("donner a")) #demande a
b = float(input("donner b")) #demande b
c = float(input("donner c")) #demande c

D=b**2-4*a*c

print("D =",D) #affiche delta

if D<0 :
    print("pas de solution réelle")
elif D==0 :
    print("une solution réelle")
else :
    x1=(-b-sqrt(D))/20
    x2=(-b-sqrt(D))/2*a

    print("la solution x1 est x1=",x1)
    print("la solution x2 est x2=",x2)
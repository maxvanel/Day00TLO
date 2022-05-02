from unittest import result


print("Entrez un numéro : ")
nbre = input()
n=0
for i in nbre :
    if(n==0):
        a = int(i)
    if (n==1):
        b = int(i)
    if (n==2):
        c = int(i)
    n = n+1

resultat = a**3 + b**3 + c**3
resultat = str(resultat)

p=0
for j in resultat :
    if(p==0):
        d = int(j)
    if (p==1):
        e = int(j)
    if (p==2):
        f = int(j)
    p = p+1

if(a == d and b == e and c == f) :
    print(resultat,"est un nombre d'Amstrong")
else :
    print(resultat,"n'est pas un nombre d'Amstrong")
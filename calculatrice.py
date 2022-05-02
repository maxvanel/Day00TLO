print ("premier chiffre")
a = int(input())
print ("opérateur")
operateur = input()
print ("deuxième chiffre")
b = int(input())
if(operateur == "+") :
    resultat = a + b
    print(resultat)
else :
    if(operateur == "-"):
        resultat = a - b
        print(resultat)
    else :
        if(operateur == "*"):
            resultat = a * b
            print(resultat)
        else : 
            if(operateur == "/"):
                resultat = float(a / b)
                print(resultat)
            else :
                print("Vous n'avez pas mis un bon opérateur")
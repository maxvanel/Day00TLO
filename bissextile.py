print ("Veuillez saisir une année :")
annee = int(input())
if(annee%4 == 0) :
    if(annee%100 == 0):
        if(annee%400 == 0):
            print("C'est une année bissextile")
        else :
            print("Ce n'est pas une année bissextile")
    else :
        print("C'est une année bissextile")
else :
    print("Ce n'est pas une année bissextile")
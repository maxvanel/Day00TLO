import random

def trier(liste):
    while liste:
        min=liste[0]
        for i in liste:
            if i < min:
                min=i
        liste.remove(min)
        r.append(min)
    return r

list_random = [random.randrange(1,100) for i in range(15)]
r=[] 
trier(list_random)
print(r)
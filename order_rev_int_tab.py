import random

def trier(liste):
    while liste:
        max=liste[0]
        for i in liste:
            if i > max:
                max=i
        liste.remove(max)
        r.append(max)
    return r

list_random = [random.randrange(1,100) for i in range(15)]
r=[] 
trier(list_random)
print(r)
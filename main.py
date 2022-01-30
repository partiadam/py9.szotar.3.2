'''
3.2 Feladat
Írj egy programot, amely szótárban tárol adatokat (legalább egy int, str, és bool típusút). 
A program a írja ki a képernyőre az adatszerkezet! 
A felhasználónak legyen lehetősége ezt az adatszerkezetet egy kulcs-érték párral bővítenie. 
A program végül írja ki a képernyőre a frissített adatszerkezetet!

Feladat
Módosítsd úgy a programot, hogy a felhasználónak többször is legyen lehetősége bővíteni az adatszerkezetet!
'''

szotar = {
    'szam': 10,
    'szoveg': 'valami',
    'igazhamis': True,    
}

print(szotar)
print()

while True:
    beker = input('Szeretnél változtatni az adatszerkezeten? (igen/nem): ')
    if beker == "igen" or beker == "Igen":
        beker1 = input('Első új érték: ')
        beker2 = input('Második új érték: ')
         
        szotar[beker1] = beker2

    if beker == "nem" or beker == "Nem":
        break

print(szotar)
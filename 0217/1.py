lista = []
eredmeny = 0
def run():
    with open ("0217/pontok.txt","r",encoding="utf-8") as f:
        for i in f:
            lista.append(int(i))
    eredmeny = lista[0]
    for szam in range(1,len(lista)):
        eredmeny = eredmeny + lista[szam]
    print("A számok összege: %0.2f" % eredmeny)
    eredmeny = lista[0]
    for szam in range(1,len(lista)):
        eredmeny = eredmeny + lista[szam]
    eredmeny = eredmeny / len(lista)
    print("A számok átlaga: %0.2f" % eredmeny)
    eredmeny = max(lista)
    print("A legnagyobb szám a listában: %0.2f" % eredmeny)

temp = input("Meg győződtél róla hogy a listában 1 sorban 1 szám van? (y/n)")
from time import sleep
if temp == "y":
    print("A program elindul.")
    sleep(1)
    print("Számok összegének kiszámítása...")
    sleep(0.3)
    print("Számok átlagának kiszámítása...")
    sleep(0.3)
    print("A legnagyobb szám megkeresése...")
    sleep(0.3)
    print("")
    run()
else:
    print("Ez esetben a program működése megáll...")

from pathlib import Path
from time import sleep
# Az NR változó adja meg hogy hány nevet kérsz be
nr = 3
lista = []
def beleiras():
    with open("0217/nevek.txt","a",encoding="utf-8") as f:
        for i in range(len(lista)):
            f.write("%s\n" % lista[i])
            print("%s hozzáadva a fájlhoz." % lista[i])
            sleep(0.5)
def uj():
    with open("0217/nevek.txt","w",encoding="utf-8") as f:
        for i in range(len(lista)):
            f.write("%s\n" % lista[i])
            print("%s hozzáadva a fájlhoz." % lista[i])
            sleep(0.5)

for i in range(nr):
    bevitel = input("Adj meg még %i nevet: " % nr)
    nr -= 1
    lista.append(str(bevitel))
    sleep(0.5)
if Path("0217/nevek.txt").exists:
    temp = input('A "nevek.txt" nevű fájl már létezik, törlöd és újat hozol létre vagy beleírsz? (uj/beleiras) ')
    if temp == "uj":
        uj()
    else:
        beleiras()
else:
    beleiras()
sleep(0.6)
print("")
print("A program sikeresen lefutott!")
print("A nevek sikeresen hozzá lettek adva a fájlhoz.")
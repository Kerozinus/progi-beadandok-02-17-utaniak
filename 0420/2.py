paros = []
paratlan = []
with open("0420/szamok2.txt","r",encoding="utf-8")as f:
    for i in f:
        if int(i) % 2 == 0 :
            paros.append(int(i))
        else:
            paratlan.append(int(i))
with open("0420/paros.txt","w",encoding="utf-8")as paro:
    paro.write("A szamok2.txt fájlból az alábbi páros számokat szedtem ki: \n")
    for i in range(len(paros)):
        paro.write(str(paros[i]))
        paro.write("\n")
with open("0420/paratlan.txt","w",encoding="utf-8")as para:
    para.write("A szamok2.txt fájlból az alábbi páratlan számokat szedtem ki: \n")
    for i in range(len(paratlan)):
        para.write(str(paratlan[i]))
        para.write("\n")
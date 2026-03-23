tanulok = []
with open("0323/tanulok.txt","r",encoding="utf-8") as f:
    for i in f:
        tanulok.append(i.strip().split(";"))
print(tanulok)
eredmeny = 0
for i in range(len(tanulok)):
    eredmeny = eredmeny + float(tanulok[i][2])
print(f"{len(tanulok)+1} Tanuló van")
eredmeny = eredmeny / len(tanulok)
print("%0.5s az osztály átlag" % eredmeny)
eredmeny = []
print("4.0-nál jobb átlagú tanulók: ")
for i in range(len(tanulok)):
    if float(tanulok[i][2]) > 4.0:
        print(tanulok[i][0])
with open("0323/eredmeny.txt","w",encoding="utf-8")as c:
    c.write("Tanulók száma: %i" % len(tanulok))
    eredmeny = 0
    for i in range(len(tanulok)):
        eredmeny = eredmeny + float(tanulok[i][2])
    eredmeny = eredmeny / len(tanulok)
    c.write("\n")
    c.write("%0.5s az osztály átlag" % eredmeny)
    c.write("\n")
    c.write("jó tanulók: " + "\n")
    for i in range(len(tanulok)):
        if float(tanulok[i][2]) > 4.0:
            c.write(tanulok[i][0]+f"({tanulok[i][2]})")
            c.write("\n")
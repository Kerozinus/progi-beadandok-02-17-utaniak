lista = []
szamlalo = 0 
with open("0217/pontok.txt","r") as f:
    for i in f:
        lista.append(int(i))
        if int(i) >= 50:
            szamlalo += 1
with open("0217/pontok.txt","a",encoding="utf-8") as c:
    c.write("\n")
    c.write("Sikeres dolgozatok száma: %i " % szamlalo)
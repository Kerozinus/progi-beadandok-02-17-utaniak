szamok = []
with open("0420/szamok.txt","r",encoding="utf-8")as f:
    for i in f:
        szamok.append(int(i))
eredmeny = szamok[0]
for x in range(1,len(szamok)):
    eredmeny = eredmeny + szamok[x]
print(f"A számok összege: {eredmeny}")
with open("0420/osszeg.txt","w",encoding="utf-8")as c:
    c.write("A szamok.txt ben lévő számok eredménye: ")
    c.write(str(eredmeny))
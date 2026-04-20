hosszu_szavak = []
with open("0420/szavak.txt","r",encoding="utf-8")as f:
    for i in f:
        if len(i) > 5:
            hosszu_szavak.append(i.strip())
with open("0420/hosszu_szavak.txt","w",encoding="utf-8") as c:
    c.write("5 karakternél hosszabb szavak: \n")
    for i in range(len(hosszu_szavak)):
        c.write(hosszu_szavak[i])
        c.write("\n")
szavak = []
with open("0420/szavak.txt","r",encoding="utf-8")as f:
    for i in f:
        szavak.append(i.strip())
print(f"{len(szavak)} db szót találtam a szavak.txt ben")
print(f"'{max(szavak)}' a leghosszabb szó a listában")
with open("0420/eredmeny.txt","w",encoding="utf-8") as c:
    c.write(str(len(szavak)))
    c.write("db szót találtam a szavak.txt ben")
    c.write("\n")
    c.write(str(max(szavak)))
    c.write("  a leghosszabb szó a listában")
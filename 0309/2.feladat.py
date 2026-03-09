szamok = [41, 18, 72, 51, 62, 1, 39, 90, 24]
eredmeny = []
for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        eredmeny.append(szamok[i])
print(f"Az első páros szám: {eredmeny[0]} és az utolsó: {eredmeny[len(eredmeny)-1]}")
for i in range(len(szamok)):
    if szamok[i] % 6 == 0:
        print(f"Az első 6-al osztható szám: {szamok[i]}")
        break
for i in range(len(szamok)):
    if szamok[i] > 50 and szamok[i] < 70:
        print(f"Az első 50 és 70 közé eső szám: {szamok[i]}")
        break
for i in range(len(szamok)):
    if szamok[i] == 1:
        print(f"Az 1 a  {i+1}. helyen van a listában")
        break

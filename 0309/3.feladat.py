szamok = []
nr = 5
for i in range(0,nr):
    bevitel = int(input(f"Adj meg még {nr} számot: "))
    szamok.append(bevitel)
    nr -= 1
eredmeny = szamok[0]
for f in range(1,5):
    eredmeny = eredmeny + szamok[f]
print(f"A számok összege: {eredmeny}")
eredmeny = szamok[0]
for f in range(1,5):
    eredmeny = eredmeny - szamok[f]
print(f"A számok különbsége: {eredmeny}")
eredmeny = szamok[0]
for f in range(1,5):
    eredmeny = eredmeny * szamok[f]
print(f"A számok szorzata: {eredmeny}")
eredmeny = szamok[0]
for f in range(1,5):
    eredmeny = eredmeny / szamok[f]
print(f"A számok hányadosa: {eredmeny}")
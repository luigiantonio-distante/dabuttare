somma=0
i=0
lista=[]
while i<5:
    a = int(input("Numero > "))
    if a > 0:
        lista.append(a)
        somma = somma + a
        i+=1
print("Somma > ",somma)

for x in lista:
    print(x)


import random
pensato=random.randint(1,90)
numero=int(input("Numero > "))
numerotentativi=1
s=""
while pensato!=numero and numerotentativi<5:     
    if abs(numero-pensato)<5:
        s="fuoco"
    elif abs(numero-pensato)<10:
        s="fuocherello"
    elif abs(numero-pensato)<15:
        s="fuochino"
    elif abs(numero-pensato)>=15:
        s="acqua"
    print(s)
    numero=int(input("Ritenta > "))
    numerotentativi+=1
if numero==pensato:
    print("HAI INDOVINATO IN ",numerotentativi," TENTATIVI")
else:
    print("Numero di tentativi superiore al limite")


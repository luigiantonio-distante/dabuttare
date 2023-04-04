import random
pensato=random.randint(1,90)
numero=int(input("Numero > "))
numerotentativi=1
while pensato!=numero:     
    if numero>pensato:
        print("Numero inserito più grande")   
    else:
        print("Numero inserito più piccolo")   
    numero=int(input("Ritenta > "))
    numerotentativi+=1
print("HAI INDOVINATO IN ",numerotentativi," TENTATIVI")


from random import randint
i=0
j=0
while i<10:
    j+=1
    i=0
    for x in range(10):
        a = randint(1,100)    
        if a > 50:
            i+=1
            print(a, end = " ")

    print("> ",i)
print("Serie di tiri: ", j)
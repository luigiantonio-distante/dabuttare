from random import randint
i=0
while i<10:
    i=0
    for x in range(10):
        a = randint(1,100)    
        if a > 50:
            i+=1
            print(a)

    print("> ",i)


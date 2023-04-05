from random import randint
l=[]
for x in range(10):
    l.append(randint(1,100))

contatore=0
for e in l:
    if e>30 and e<70:
        contatore+=1
print(l)
print(contatore)

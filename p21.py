from random import randint
l=[]
for x in range(10):
    l.append(randint(1,100))
cont=0
for z in l:
    if z>30:
        cont+=1
print(l) 
print(cont)

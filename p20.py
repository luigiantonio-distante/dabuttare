from random import randint
l=[]
for x in range(10):
    a=randint(1,100)
    if a>50:
        l.append(a)
print(l)
print(len(l))


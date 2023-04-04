from random import randint
l=[]
for x in range(10):
    l.append(randint(1,100))

s=0
for z in l:
    s+=z
print(l)
print(s)

from random import randint
a=randint(1,6)
b=randint(1,6)
i=1
while a != b:
    i+=1
    print(a,b)
    a=randint(1,6)
    b=randint(1,6)
    print(a,b)
print(i)


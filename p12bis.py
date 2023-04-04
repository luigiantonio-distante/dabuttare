from random import randint
a=randint(1,6)
b=randint(1,6)
print(a,b)
i=1
while a != b:
    i+=1
    a=randint(1,6)
    b=randint(1,6)
    print(a,b)
print(i)

a=randint(1,6)
b=randint(1,6)
print(a,b)
j=1
while a != b:
    j+=1
    a=randint(1,6)
    b=randint(1,6)
    print(a,b)
print(j)

print("Primo" if i<j else "Secondo")


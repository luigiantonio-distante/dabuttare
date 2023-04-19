import sys
from random import randint
dbfilename='dati.dat'
dbfile=open(dbfilename,'a')
sys.stdout=dbfile
for z in range(10):
    for x in range(6):
        num=randint(1,90)
        car="-" if x<5 else ""        
        if num<10:
            print(" "+str(num),end=car)
        else:
            print(num,end=car)
    print()

dbfile.close()

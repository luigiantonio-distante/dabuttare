import sys
lista=list()
dbfilename='dati.dat'
dbfile=open(dbfilename,'r')
sys.stdin=dbfile
fine=False
while not fine:
    try:
        riga=input()
        lista.append(riga)
    except EOFError:
        fine=True

dbfile.close()
for riga in lista:
    l=riga.split("-")
    min10=0
    for n in l:
        if int(n)<10:
            min10+=1        
    if min10>2:
        print(l)


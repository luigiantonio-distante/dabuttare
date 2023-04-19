import pickle
rubrica={}
rubrica[1]=dict(nome="ANDREA SANSA", ETA=23, REDDITO=50000, AREA='SOFTWARE')
rubrica[2]=dict(nome="DAVIDE K.", ETA=55, REDDITO=10000, AREA='VARIE')
rubrica[3]=dict(nome="SIMONE", ETA=32, REDDITO=0, AREA='EDILIZIA')
#scrittura
dbfile=open("rubrica.dat",'wb')
pickle.dump(rubrica,dbfile)
dbfile.close()

#lettura
dbfile=open("rubrica.dat",'rb')
new = pickle.load(dbfile)
dbfile.close()

for x in new:
    print(x," => ",new[x]['nome'])


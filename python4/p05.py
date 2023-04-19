import csv
header=['nome','cognome','telefono']
dati=[['n1','c1','123'],['n2','c2','456'],['n3','c3','789']]
filename='provacsv.csv'
with open(filename,'w',newline="") as file:
    csvwriter = csv.writer(file)    #crea un oggetto writer
    csvwriter.writerow(header)      #scrivo la riga header
    csvwriter.writerows(dati)       #scrivo i dati

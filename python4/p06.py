import csv
file=open('provacsv.csv')
lettore=csv.reader(file)
header=[]
header=next(lettore)
rows=[]
for row in lettore:
    rows.append(row)
file.close()
s=""
print("Campi")
for campo in header:
    s+=" "+str(campo)
print(s)
for row in rows:
    stringa=""
    for data in row:
        stringa+=" "+str(data)
    print(stringa)


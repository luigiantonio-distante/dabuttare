nomi=['ANDREA', 'RICCARDO', 'STEFANO', 'NICOLE', 'CARLOS', 'MARCO']
cognomi=['SANSA', 'CESARETTI', 'BERALDI', 'PEZZI', 'ANDREAS', 'FULFARO']
nominativi=[]
for n in nomi:
    for c in cognomi:
        nominativi.append(n + " " + c)
print(nominativi)

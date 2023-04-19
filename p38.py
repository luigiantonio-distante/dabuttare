def media(lista):
    s=0
    for n in lista:
        s += n['voto']
    media = s/len(lista)
    return media

lista=list()
for n in range(3):
    allievo=dict()
    allievo['nome']=input("Nome")
    allievo['cognome']=input("Cognome")
    allievo['eta']=int(input("Età"))
    allievo['test'] = list()
    for x in range(3):
        d=dict()
        d['voto']=int(input("Voto"))
        d['data']=input("Data")
        allievo['test'].append(d)
    lista.append(allievo)
"""
allievo=dict()
allievo['nome']="Stefano"
allievo['cognome']="Cesaretti"
allievo['eta']=31
allievo['test']=[{  'voto':25,
                    'data':"05/02/2021"
                },
                {   'voto':28,                 
                    'data':"05/04/2021"
                },
                {   'voto':22,                 
                    'data':"05/05/2021"
                }
                ]
lista.append(allievo)

allievo=dict()
allievo['nome']="Marco"
allievo['cognome']="Fulfaro"
allievo['eta']=19
allievo['test']=[{  'voto':27,
                    'data':"06/02/2021"
                },
                {   'voto':25,                 
                    'data':"06/04/2021"
                },
                {   'voto':26,                 
                    'data':"06/05/2021"
                }
                ]
lista.append(allievo)
"""

for x in lista:
    print(x['nome'],media(x['test']))


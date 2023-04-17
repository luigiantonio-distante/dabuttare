def media(lista):
    s=0
    for n in lista:
        s += n['voto']
    media = s/len(lista)
    return media

lista=list()
allievo=dict()
allievo['nome']="Andrea"
allievo['cognome']="Sansa"
allievo['eta']=28
allievo['test']=[{  'voto':21,
                    'data':"01/02/2021"
                },
                {   'voto':29,                 
                    'data':"01/04/2021"
                },
                {   'voto':25,                 
                    'data':"01/05/2021",
                    'domande':[True, False, False, True]
                }
                ]
lista.append(allievo)

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

for x in lista:
    print(x['nome'],media(x['test']))


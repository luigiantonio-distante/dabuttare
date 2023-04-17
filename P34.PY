lista=list()
giocatore=dict()
giocatore['nome']='andrea'
giocatore['cognome']='sansa'
giocatore['ruolo']='portiere'
giocatore['reti']=5
lista.append(giocatore)
giocatore=dict()
giocatore['nome']='carlos'
giocatore['cognome']='anrdeas'
giocatore['ruolo']='terzino'
giocatore['reti']=2
lista.append(giocatore)
giocatore=dict()
giocatore['nome']='stefano'
giocatore['cognome']='cesaretti'
giocatore['ruolo']='centravanti'
giocatore['reti']=8
lista.append(giocatore)
for x in lista:
    print(x['nome']+" " +x['cognome'])
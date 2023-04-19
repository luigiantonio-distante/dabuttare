import json
db={
    'rubrica':[
            {
                'nome':'LUIGI',
                'cognome':'DISTANTE',
                'telefono':'3914949389'
            },
            {
                'nome':'ADELE',
                'cognome':'CASTRI',
                'telefono':'3208787345'
            }
    ]
}
class Contatto:
    def __init__(self,nome="", cognome="", telefono="") -> None:
        self.nome=nome
        self.cognome=cognome
        self.telefono=telefono
class Repository:
    def load(self):
        self.dati=json.load(open("filejson.json"))
    def __init__(self, dati):
        self.dati=dati    
    def regContatto(self, contatto:Contatto):
        dizContatto=dict()
        dizContatto['nome']=contatto.nome
        dizContatto['cognome']=contatto.cognome
        dizContatto['telefono']=contatto.telefono
        self.dati['rubrica'].append(dizContatto)
    def lista(self):
        return self.dati['rubrica']
    def registra(self):
        with open("filejson.json","w") as outfile:
            json.dump(db, outfile)

class IO:
    def mostramenu(self):
        print("1. Nuovo")
        print("2. Lista")
        print("3. Salva")
        print("0. Uscita")
    def leggiScelta(self):
        return input("> ")
    def acqContatto(self):
        contatto=Contatto()
        contatto.nome=input("Nome > ")
        contatto.cognome=input("Cognome > ")
        contatto.telefono=input("Telefono > ")
        return contatto
    def elenco(self, lista):
        for x in lista:
            print(x['nome']," " , x['cognome'], " " , x['telefono'])

def main():
    io=IO()
    repository=Repository(db)
    repository.load()
    io.mostramenu()
    scelta=io.leggiScelta()
    while scelta != '0':
        if scelta=='1':
            contatto = io.acqContatto()
            repository.regContatto(contatto)
        if scelta=='2':
            lista=repository.lista()
            io.elenco(lista)
        if scelta=='3':
            repository.registra()
        io.mostramenu()
        scelta=io.leggiScelta()

main()
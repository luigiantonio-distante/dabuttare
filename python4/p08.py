import json

db={
    'auto':[
            {
                'targa':'FF345DD',
                'modello':'GIULIA',
                'marca':'ALFA ROMEO'
            },
            {
                'targa':'GG123CC',
                'modello':'320',
                'marca':'BMW'
            },
            {
                'targa':'GD898DD',
                'modello':'ALFA ROMEO',
                'marca':'159'
            },
            {
                'targa':'FG555CC',
                'modello':'GIULIA',
                'marca':'ALFA ROMEO'
            },
            {
                'targa':'GF000BB',
                'modello':'318',
                'marca':'BMW'
            },
            {
                'targa':'GA787FF',
                'modello':'ALFA ROMEO',
                'marca':'159'
            }
    ],
    'clienti':[
            {
                'id':1,
                'nome':'n1',
                'cognome':'c1'
            },
            {
                'id':2,
                'nome':'n2',
                'cognome':'c2'
            },
            {
                'id':3,
                'nome':'n3',
                'cognome':'c3'
            },
    ],
    'noleggi':[
                {
                    'targa':'GF000BB',
                    'dataini':'2023-04-18',
                    'datafine':'2023-04-20',
                    'idcliente':2
                }
               ]
}

class Criteri:
    def ricercaAuto(a,auto):
        return ((a['marca']==auto.marca or len(auto.marca) == 0)
                and
                (a['modello']==auto.modello or len(auto.modello) == 0)
                and
                (a['targa']==auto.targa or len(auto.targa) == 0))

                        
class Auto:
    def __init__(self,marca="", modello="", targa="") -> None:
        self.marca=marca
        self.modello=modello
        self.targa=targa
class Repository:
    def load(self):
        self.dati=json.load(open("filejson.json"))
    def __init__(self, dati):
        self.dati=dati    
    def regContatto(self, contatto):
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
    def filtro(self, contatto):
        lista=list()
        for c in self.dati['rubrica']:
            if ((c['nome']==contatto.nome or len(contatto.nome) == 0)
                and
                (c['cognome']==contatto.cognome or len(contatto.cognome) == 0)
                and
                (c['telefono']==contatto.telefono or len(contatto.telefono) == 0)):
                lista.append(c)
        return lista
    def filtroFunction(self, auto, f):
        lista=list()
        for a in self.dati['auto']:
            if (f(a,auto)):
                lista.append(a)
        return lista
class IO:
    def mostramenu(self):
        print("1. Ricerca")
        print("0. Uscita")
    def leggiScelta(self):
        return input("> ")
    def acqAuto(self):
        auto=Auto()
        auto.marca=input("Marca > ")
        auto.modello=input("Modello > ")
        auto.targa=input("Targa > ")
        return auto
    def elenco(self, lista):
        for x in lista:
            print(x['marca']," " , x['modello'], " " , x['targa'])

def main():
    io=IO()
    repository=Repository(db)
    #repository.load()
    io.mostramenu()
    scelta=io.leggiScelta()
    while scelta != '0':
        if scelta=='1':
            auto = io.acqAuto()
            listaFiltrata = repository.filtroFunction(auto, Criteri.ricercaAuto)
            if len(listaFiltrata)>0:
                io.elenco(listaFiltrata)
            else:
                print("Nessuna auto trovata")
        io.mostramenu()
        scelta=io.leggiScelta()

main()
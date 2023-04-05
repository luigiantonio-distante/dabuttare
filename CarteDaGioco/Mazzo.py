from random import randint
from Carta import Carta
class Mazzo:
    def creaMazzo(self, max, semi):
        mazzoApp=list()
        while len(mazzoApp)<self.max*len(self.semi):
            rand=randint(1,self.max*len(self.semi))
            q=(rand-1)//self.max    #seme
            r=rand%self.max     #valore
            #print(rand," " , q, " seme e valore " , r)
            if rand not in mazzoApp:
                mazzoApp.append(rand)
        self.mazzo=[Carta(x%self.max+1,self.semi[(x-1)//self.max]) for x in mazzoApp]
    def __init__(self, max, semi):
        self.max=max
        self.semi=semi
        self.mazzo=list()
        self.creaMazzo(max, semi)
    
        
            
from random import randint
def creaLista():
    L=[]
    for x in range(10):
        L.append(randint(1,90))
    return L

def stampaLista(X):
    for n in X:
        print(n,end = " ")

def main():
    M = creaLista()
    stampaLista(M)

main()

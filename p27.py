def acqNumero():
    x = int(input("Numero > "))
    return x
def outRisultato(x):
    print("Risultato > ",x)
def potenza(a, b):
    p=a
    for x in range(b-1):
        p = p * a
    return p
def main():
    m=acqNumero()
    n=acqNumero()
    pot = potenza(m, n)
    outRisultato(pot)
main()

from random import randint
vocali=['a','e','i','o','u']
conson=['b','c','d','f','g','h','l','m','n','p','q','r','s','t','v','z']
def estrae(lista):
    i=randint(0,  len(lista)-1)
    return lista[i]
def creaParola(lun):
    s=''
    inizio=randint(0,1)
    if inizio==0:
        for x in range(lun//2):
            s = s + estrae(conson) + estrae(vocali)
    else:
        for x in range(lun//2):
            s = s + estrae(vocali) + estrae(conson)
    return s
def main():
    parola = creaParola(6)
    print("Parola > ",parola)

main()

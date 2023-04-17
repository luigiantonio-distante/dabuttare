from random import randint
vocali=['a','e','i','o','u']
conson=['b','c','d','f','g','h','l','m','n','p','q','r','s','t','v','z']
def estrae(lista):
    i=randint(0,  len(lista)-1)
    return lista[i]
def creaParola(lun):
    s=''
    inizio=randint(0,2)
    if inizio==0:
        for x in range(lun//2):
            s = s + estrae(vocali) + estrae(conson)
    else:
        for x in range(lun//2):
            s = s + estrae(conson) + estrae(vocali)
    return s
def main():
    parola = creaParola(6)
    print("Parola > ",parola)

main()

L=[22,28,20,30]

def media(lista):
    s=0
    for n in L:
        s += n
    media = s/len(L)
    return media

def main():
    mm = media(L)
    print(mm)

main()
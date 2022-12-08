
def find(wartosc, lista):
    x= 0
    indeksy = []

    for i in lista:
        if i == wartosc:
           indeksy.append(x)
        x+= 1
    return(indeksy)
#print(find(3, [1,3,5,20, 3]))
E = find(3, [1,3,5,20, 3]
print(E)


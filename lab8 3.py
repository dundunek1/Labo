

def potega(liczby, potegi):
    i=0
    lista3=[]
    if len(liczby) != len(potegi):
        print("Listy sa rozne")
        return lista3
    for i in range(len(liczby)):
        x = liczby[i] ** potegi[i]
        lista3.append(x)
    return lista3
w = potega([2,2,2,2], [1,2,3,4])
print(w)


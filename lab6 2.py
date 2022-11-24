def oblicz(x,y):
    roz = x-y
    sum= x+y
    return roz,sum

x = int(input("Podaj liczbe x:"))
y = int(input("Podaj liczbe y:"))

w = oblicz(x,y)
print(w)
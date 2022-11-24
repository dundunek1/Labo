def oblicz(x,y):
    roz = x-y
    sum= x+y
    return roz,sum

x = input("Podaj liczbe x:")
y = input("Podaj liczbe y:")

w = oblicz(12.34,45.234)
print(w[0], w[1])

a,b = oblicz(13, 11.23)
print(a,b)
x = int(input("Podaj pierwsza liczbe:"))
y = int(input("Podaj druga liczbe:"))

if  x > y:
    x,y = x,y
while x <= y:
    print (x)
    x += 1
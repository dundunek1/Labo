x = int(input("Podaj pierwsza liczbe:"))
y = int(input("Podaj druga liczbe:"))

if  x > y:
    x,y = x,y
while x <= y:
    if x % 2 == 1:
        x= x+1
        continue

    print (x)
    x += 1

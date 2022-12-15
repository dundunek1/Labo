#Użytkownik podaje 7 liczb. Napisz program, który sprawdzi, ile z tych liczb jest podzielnych przez 3.
y = 0
for l in range(7):
    x = int(input("Podaj liczbe"))
    if x%3==0:
        print("Liczba jest podzielna przez 3")
        y+=1
    else:
        print("Liczba nie jest podzielna przez 3")

print("Podzielnych liczb przez 3 jest:", y)

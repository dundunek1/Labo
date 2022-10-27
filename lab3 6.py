n = int(input("Podaj liczbe studentow:"))

i = 1
suma = 0

while i < n+1:
    punkty = float(input(f'Podaj liczbe punktow studenta {i}:'))
    if punkty < 0 or punkty > 100:
        continue
    i = i + 1
    suma = suma + punkty

srednia = suma / n
print(f"srednia wynosi: {srednia}")
x = int(input("Podaj wiek: "))
if x < 4:
    cena = 0
elif x <= 18:
    cena = 10
else:
    cena = 20
print(f"Cena biletu: {cena}zł")
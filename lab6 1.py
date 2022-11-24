def func_1(imie, wiek):
    """Funkcja wypisujaca imie i wiek"""
    print(imie, " ", wiek)

a = input("podaj imie:")
b=int(input("podaj wiek:"))
#func_1("Jakub", 20)
func_1(a, b)

func_1(wiek=19, imie="Igor")
print(func_1.__doc__)
print(help(func_1))
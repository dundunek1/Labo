def dodawanie(a,b):
    suma = a + b
    return suma
def odejmowanie(a,b):
    roznica = a - b
    return roznica
def mnozenie(a,b):
    iloczyn = a * b
    return iloczyn
def dzielenie(a,b):
    if b != 0:
        return a / b
    else:
        print("Dzielenie przez 0!")
dic = {'+':dodawanie, '-':odejmowanie, '*':mnozenie, '/':dzielenie}
x = int(input("Podaj liczbe 1: "))
y = int(input("Podaj liczbe 2: "))
z = input("Podaj działanie: ")
# dic[z](x,y)
print(dic[z](x,y))
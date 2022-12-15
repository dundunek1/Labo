#Napisz funkcję, która ma trzy parametry a, b, c. Funkcja ma utworzyć i zwrócić listę wypełnioną liczbami
#od a do b z krokiem c. Sprawdź działanie funkcji.
a= int(input("Podaj liczbe a:"))
b= int(input("Podaj liczbe b:"))
c= int(input("Podaj liczbe c:"))
def funkcja(a,b,c):
    L=[]
    L = list(range(a, b, c))
    return L
print(funkcja(a,b,c))

zestaw_1=[]
import random
y = int(input("Podaj liczbe elementow listy:"))
for i in range(y):
    x = random.randint(1,10)
    zestaw_1.append(x)
print(zestaw_1)


j = int(input("Podaj liczbe elementow listy:"))
zestaw_2=[random.randint(5, 15) for i in range(j)]
print(zestaw_2)

f = int(input("Podaj liczbe ktora sprawdzamy"))

if f in zestaw_1:
    print("Liczba z zestawu 1")

elif f in zestaw_2:
    print("Liczba z zestawu 2")

else:
    print("Liczba nie jest w zadnym")

zestaw_1_22=zestaw_1+zestaw_2
print(zestaw_1_22)
print('Posegregowanie i polaczenie ich')
zestaw_1_22.sort()
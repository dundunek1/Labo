#Napisz program wypełniający listę znakami podawanymi przez użytkownika, a następnie wyświetlający
#znaki w kolejności odwrotnej do wprowadzania (bez wykorzystania funkcji reversed() lub reverse() ).

L = []
L2=[]
x = int(input("Ile znakow bedziesz podawac?:"))

for i in range(x):
    y= input("Jaki znak chcesz dodac?:")
    L.append(y)

L2 = L[::-1]
print(L)
print(L2)
import numpy as np
#tab_1= np.array([1, 2, 3]), dtype='int32');
#print(tab_1)

#tab_2= np.array9([5,6,7,8])
#print(tab_2)


#Zadanie 1. Konwersja 8-bitowej liczby binarnej na liczbę dziesiętną.
#• Utwórz 8-elementową listę składaną o wartościach będących kolejnymi potęgami dwójki - [128 64 32
#16 8 4 2 1]
#• Na podstawie tej listy utwórz tablice ndarray o nazwie wagi.
#• Utwórz drugą 8-elementową tablicę ndarray wypełnioną zerami i jedynkami (losowo) o nazwie
#liczba_bin.
#• Oblicz iloczyn tablic wagi i liczba_bin, a następnie policz sumę wartości iloczynu.

#arr=[128,64,32,16,8,4,2,1]
#arr=[]
#for i in range(7,-1, -1):
   # arr.append(2**i)

#print(arr)

arr=[2**i for i in range(7,-1,-1)]
print(arr)

wagi= np.array(arr)
print(wagi)

liczba_bin= np.random.randint(low=0, high=2, size=8);
print(liczba_bin)

dziesietny= wagi*liczba_bin
print(dziesietny)

suma = dziesietny.sum()
print(suma)
#Zadanie 2.
#• Utwórz losową macierz o wymiarach 5x5. Znajdź największy i najmniejszy element. (patrz tab4_2d;
#metoda max(), min())
#• Policz sumę wartości w poszczególnych wierszach.


import numpy as np

macierz = np.random.randint(low=0, high = 25, size = (5, 5))
print(macierz)
print("wartosc minimalna: ", macierz.min())
print("wartosc maksymalna: ", macierz.max())

print("wartosci minimalne wiersza:", macierz.min(axis=1))
print("wartosci maksymalne wiersza:", macierz.max(axis=0))

print("suma wartosci wierszy:", macierz.sum(axis=1))
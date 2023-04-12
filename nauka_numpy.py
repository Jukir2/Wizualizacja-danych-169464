import numpy as np

# inicjalizacja tablicy
a = np.array([[0, 1], [2, 3]])
print(a)
# lub drugi sposób
a = np.arange(2, 5, 0.1)
print(a)
# wypisanie tpu zmiennej tablicy (nie jej elementów)
print(type(a))
# sprawdzenie typu danych tablicy
print(a.dtype)
# inicjalizacja tablicy z konkretnym typem danych
a = np.arange(2, dtype='int64')
print(a.dtype)
# zapisywanie kopii tablicy z konkretnym typem danych
b = a.astype('float')
print(b)
print(b.dtype)
# stworzenie tablicy wielowymiarowej może wyglądać tak
# parametrem przekazywanym do funkcji array jest obiekt, k
# może to być Pythonowa lista
m = np.array([np.arange(2), np.arange(2)])
print(m.shape)
# ponownie typem jest ndarray
print(type(m))

zera = np.zeros((5, 5))
jedynki = np.ones((4, 4))
print(zera)
print(jedynki)
# warto sprawdzić jaki jest domyślny typ danych takich tablic
print(zera.dtype)
print(jedynki.dtype)
# można również stworzyć "pustą" macierz o podanych wymiarach
# wartości umieszczane są losowe, najpierw podana jest ilość wierszy a potem kolumn
pusta = np.empty((2, 2))
print(pusta)

macierz = np.array([[12, 11], [2, 1]])
print(macierz)
# do elementów tablicy możemy odwołać się tak jak do elementów słownika
poz_1 = macierz[1, 1]
poz_2 = macierz[0][1]
print(poz_1)
print(poz_2)

liczby_lin = np.linspace(1, 2, 5, endpoint=False)
print(liczby_lin)

mat_diag = np.diag([a for a in range(5)])
print(mat_diag)
mat_diag = np.diag([a + +2 for a in range(5)])
print(mat_diag)
mat_diag = np.diag([a for a in range(5)], 1)
print(mat_diag)

z = np.indices((5, 3))
print(z)
print(z[0])
print(z[0][1])
print(z[0][1][2])

z = np.fromiter(range(5), dtype='int32')
print(z)

znaki = b'ogolna'
z1 = np.frombuffer(znaki, dtype='S1')
print(z1)
z2 = np.frombuffer(znaki, dtype='S2')
print(z2)

znaki = 'ogolna'
z3 = np.array(list(znaki))
z4 = np.array(list(znaki), dtype='S1')
z5 = np.array(list(b'ogolna'))
z6 = np.fromiter(znaki, dtype='S1')
print(z3)
print(z4)
print(z5)
print(z6)

a = np.arange(10)
print(a)
s = slice(2, 7, 2)
print(a[s])
s = range(2, 7, 2)
print(a[s])
print(a[2:7:2])
print(a[1:])
print(a[2:5])

mat = np.arange(25)
mat = mat.reshape((5, 5))
print(mat)
print(mat[1:])  # od drugiego wiersza
print(mat[:, 1])  # druga kolumna jako wektor
print(mat[:, -1])  # ostantnia kolumna
print(mat[2:6, 1:3])  # 2 i 3 kolumna dla 3,4,5 wierszy
print(mat[:, range(2, 6, 2)])  # 3 i 5 kolumna
print(mat[:, [2, 4]])  # to samo co poprzednia linia

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print(y)

import random

# Zad1
A = [1 - x for x in range(1, 10)]
print(A)

B = [4 ** i for i in range(8)]
print(B)

C = [x for x in B if x % 2 == 0]
print(C)

# Zad2
lista1 = []

for x in range(10):
    lista1.append(random.randint(1, 100))
print(lista1)
L = [x for x in lista1 if x % 2 == 0]
print(L)

# Zad3
jedzenie = {"jajka": "szt", "mleko": "l", "mąka": "kg"}
J = {key: value for (key, value) in jedzenie.items() if value == "szt"}
print(J)


# Zad4
def czytrojkatprostokatny(a, b, c):
    if (a * a + b * b == c * c) | (a * a + c * c == b * b) | (c * c + b * b == a * a):
        return 1
    else:
        return 0


if czytrojkatprostokatny(3, 4, 5) == 1:
    print("Trójkąt jest prostokątny!")
else:
    print("Trójkąt nie jest prostokątny!")


# Zad5
def poletrapezu(a, b, h):
    pole = ((a + b) * h) / 2
    return pole


print(poletrapezu(3, 4, 6))


# Zad6
def iloczynciagu(a, b, n):
    wynik = a
    for x in range(1, n):
        wynik *= b

    return wynik


print(iloczynciagu(1, 4, 10))


# zad7
def iloczynciaguzgwiazdka(a, b, n):
    wynik = a * (b ** (n - 1))
    return wynik


print(iloczynciaguzgwiazdka(1, 4, 10))

#zad8

def listazakupow(lista):
    elementy = len(lista)

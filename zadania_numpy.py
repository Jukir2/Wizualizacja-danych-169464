import numpy as np

# zad1
tab1 = np.arange(4, 20 * 4, 4)
print(tab1)

# zad2
tab2 = np.arange(1, 5, 0.5)
print(tab2)
print(tab2.dtype)
tab3 = tab2.astype('int32')
print(tab3)
print(tab3.dtype)


# zad3
def foo3(n):
    tab = np.array([2 ** a for a in range(n * n)])
    return tab


print(foo3(3))


# zad4
def foo4(x, n):
    tab = np.logspace(x, n, num=5, dtype=int)
    return tab


print(foo4(2, 4))

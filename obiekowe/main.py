# import random
#
# # zad1
# plik = open("dane.txt", "w+")
# for i in range(1, 10, 1):
#     x = random.randint(0, 30)
#     x *= 2
#     plik.write(str(x))
#     if i != 9:
#         plik.write(", ")
# plik.close()
#
# # zad2
# plik = open("dane.txt", "r")
# wiersze = plik.readlines()
# plik.close()
# print(wiersze)
#
# # zad3
# with open("dane.txt", "w") as plik:
#     for i in range(1, 10, 1):
#         x = random.randint(0, 30)
#         plik.write(str(x))
#         if i != 9:
#             plik.write(", ")
#
# with open("dane.txt", "r") as plik:
#     for linia in plik:
#         print(linia, end="")
#

# zad4
class NaZakupy:

    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print(self.nazwa_produktu, str(self.ilosc), self.jednostka_miary, self.cena_jed)

    def ile_produktu(self):
        return str(self.ilosc), self.jednostka_miary

    def ile_kosztuje(self):
        return round(self.ilosc * self.cena_jed, 2)


produkt1 = NaZakupy("Masło", 44, "kostki", 13.98)
produkt1.wyswietl_produkt()
print(produkt1.ile_produktu())
print(produkt1.ile_kosztuje())


class Ciagi_arytmetyczne:

    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def wyswietl_dane(self):
        print("a1: ", self.a1, "r: ", self.r, "n: ", self.n)

    def pobierz_elementy(self):
        print("Podaj a1, r i n ciagu:\n")
        a1 = input()
        r = input()
        n = input()
        self.a1 = a1
        self.r = r
        self.n = n

    def policz_sume(self):
        return (self.a1 + (self.a1 + (self.n - 1) * self.r) / 2) * self.n


ciag1 = Ciagi_arytmetyczne(1, 1, 5)
ciag1.wyswietl_dane()
ciag1.pobierz_elementy()
ciag1.wyswietl_dane()
print(ciag1.policz_sume())
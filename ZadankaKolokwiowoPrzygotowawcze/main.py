# #zad1
# try:
#     a = input("Podaj liczbę calkowitą a:\n")
#     b = input("Podaj liczbę calkowitą b:\n")
#     plik = open("zadanie1.txt", "w+")
#     wynik = pow(int(a), 2) + int(a) * int(b) + pow(int(b), 2)
#     plik.write(str(wynik))
#     plik.close()
# except:
#     print("Złe dane!\n")
#
#
# # zad2
# def foo2(lista1, lista2):
#     lista_wyjsciowa = []
#     if len(lista1) > len(lista2):
#         x = 0
#         while x < len(lista1):
#             if x < len(lista2):
#                 lista_wyjsciowa.append(lista1[x] + lista2[x])
#             else:
#                 lista_wyjsciowa.append(lista1[x])
#             x += 1
#     elif len(lista1) < len(lista2):
#         x = 0
#         while x < len(lista2):
#             if x < len(lista1):
#                 lista_wyjsciowa.append(lista1[x] + lista2[x])
#             else:
#                 lista_wyjsciowa.append(lista2[x])
#             x += 1
#     else:
#         x = 0
#         while x < len(lista1):
#             lista_wyjsciowa.append(lista1[x] + lista2[x])
#             x += 1
#
#     return lista_wyjsciowa
#
#
# lista1 = [2, 3, 4, 5, 3, 4, 6, 7]
# lista2 = [12, 34, 5, 22]
# print(lista1)
# print(lista2)
# print(foo2(lista1, lista2))

# zad3
with open('dane.txt', 'r', encoding='utf8') as plik2:
    plik2.seek(100)
    print(plik2.read(35))

# zad4

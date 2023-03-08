# # zmienne
# a = 'napis'
# print(a)
# print(type(a))
# b = 5
# print(b)
# c = 7.5
# print(c)
# print(b + c)
#
# # listy
# listy = ['2', 4, 5, 2, 3, 5.4, [2, 3, 4]]
# print(listy)
# listy.append(4)
# print(listy)
#
# # dodanie do listy na danej pozycji,
# # usuniecie elementu z danej pozyji
# # usuniecie elementu o danej wartości
# # dodać sekwencję do listy
# # odwrócic listę
# # posortować elementy w liście
#
# listy.insert(3, 5)
# print(listy)
# del listy[7]
# print(listy)
# listy.remove('2')
# print(listy)
# listy.extend([2, 0])
# print(listy)
# listy.reverse()
# print(listy)
# listy.sort()
# print(listy)

# # slownik
# slownik = {"kamienie": 2, "drewno": 7, "złoto": 27}
# print(slownik)
# print(slownik.keys())
# print(slownik.values())
# print(len(slownik))
#
# print('a = %(zm)d' % {'zm': 12})
# print('a = {}'.format(12))
# #
# # napis = input('wprowadz liczbe: ')
# # print(napis)
# # print(type(napis))
# # napis = int(napis)
# # print(type(napis))
#
# # instrukcja warunkowa
# # if warunek:
# # instrukcje
# # elif warunek:
# # instrukcje
# # else:
# # instrukcje
#
# x = input('podaj x: ')
# y = input('podaj y: ')
# z = input('podaj z: ')
# t = input('podaj t: ')
# if x > y:
#     print(x + ' jest wieksze od ' + y)
# elif x < y:
#     print(x + ' jest mniejsze od ' + y)
# else:
#     print(x + ' jest równe ' + y)
#
# if (x > y) & (z > t):
#     print("x jest wieksze od y i z jest wieksze od t")
#
# for i in range(1, 6, 1):
#     print(i)
# else:
#     print('koniec petli for')
#
# for j in range(len(listy)):
#     print(j, listy[j])

#pętla while
#while warunek:
#   instrukcje
#else:
#   instrukcje

# licznik = 0
# while licznik < len(listy):
#     print(listy[licznik])
#     licznik += 1
#
#
# liczby = [420, 69, 1337, 2137, 34]
# a = input('podaj liczbe a: ')
# a = int(a)
# licznik = 0
#
# while licznik < len(liczby):
#     if liczby[licznik] - a == 0:
#         print(str(a) + ' - ' + str(liczby[licznik]) + ' = 0')
#         break
#     licznik += 1
# else:
#     print(licznik)

lista = [2, 4, 2, 2, 2, 5]
counter = 0
print(lista)
while counter != len(lista):
    if lista[counter] == 2:
        del lista[counter]
    else:
        counter += 1

print(lista)

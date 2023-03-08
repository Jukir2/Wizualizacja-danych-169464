listy = ['2', 4, 5, 2, 3, 5.4, [2, 3, 4]]
print(listy)
listy.append(4)
print(listy)

# dodanie do listy na danej pozycji,
# usuniecie elementu z danej pozyji
# usuniecie elementu o danej wartości
# dodać sekwencję do listy
# odwrócic listę
# posortować elementy w liście

listy.insert(3, 5)
print(listy)
del listy[7]
print(listy)
listy.remove('2')
print(listy)
listy.extend([2, 0])
print(listy)
listy.reverse()
print(listy)
listy.sort()
print(listy)

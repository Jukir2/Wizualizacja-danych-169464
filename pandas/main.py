import pandas as pd
import numpy as np

# Excel i pliki otwieranie/czytanie czy coś
df1 = pd.read_csv("australian.txt", header=None, sep=' ', decimal='.')
print(df1)
xlsx = pd.ExcelFile('Wyniki.xlsx')
df2 = pd.read_excel(xlsx, header=0)
print(df2)

# Listing 1 - tworzenie Series i DataFrames

# Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)

# DataFrame
# tworzenie dataframe na podstawie słownika
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847526]}
df3 = pd.DataFrame(data)
print(df3)

# DataFrame przechowuje typ dla każdej kolumny co możemy sprawdzić wpisując
print(df3.dtypes)
# możemy również w prosty sposób stworzyć serię danych - czyli próbki dla kolejnych #dat, pomiarów czasu
daty = pd.date_range('20210324', periods=5)
print(daty)
df4 = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
print(df4)

# biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych
# CSV, odczyt i zapis
df5 = pd.read_csv('australian.txt', header=0, sep=";", decimal=',')
print(df5)
df5.to_csv('plik.csv', index=False)

# Excel - wymagana jest biblioteka openpyxl
# trzeba ją zainstalować

xlsx2 = pd.ExcelFile('Wyniki.xlsx')
df6 = pd.read_excel(xlsx2, header=0)
print(df6)
df6.to_excel('Wyniki2.xlsx', sheet_name='arkusz_pierwszy')

# Pobieranie danych ze struktur

# pojedynczy element serii, odnosimy się do nazwy indeksu
print(s['c'])
# możemy również dostać się do wartości serii jak do pola klasy
print(s.c)

# pojedynczy element ramki danych, tak jak przy cięciu tablic, oparte na indeksach
print(df3[0:1])
print("")
# kolumna po etykiecie
print(df3['Populacja'])
# pobieranie pojedynczej wartości po indeksie wiersza i kolumny
print(df3.iloc[0, 0])
# pobieranie wartości po indeksie wiersza i etykeicie kolumny
print(df3.loc[0, "Kraj"])
print(df3.at[0, "Kraj"])
# podobnie jak w przypadku serii można odwoływać się do kolumn jak do pól klasy
# dodatkowo print jest wywoływany jak w pętli dla każdego elementu danej kolumny
print('kraj: ' + df3.Kraj)

# jeden losowy element
print(df3.sample())
# n losowych elementów
print(df3.sample(2))
# ilość elementów procentowo, uwaga na zaokrąglenie
print(df3.sample(frac=0.5))

# jeżeli potrzeba nam więcej próbek niż najduje się w zbiorze i dopuszczamy duplikaty
# to możemy użyć parametru replace, który będzie losował z powtórzeniami
print(df3.sample(n=10, replace=True))

# zamiast wyświetlać całą kolekcje możemy wyświetlić określoną ilość elementów od początku kolekcji
# lub od jej końca
print(df3.head())
print(df3.head(2))
print(df3.tail(1))

# Pandas jest też w stanie wyświetlić statystykę dla wartości, które dana kolekcja zawiera, o ile są jakieś kolumny
# z danymi numerycznymi
print(df3.describe())
# transpozycja to zmienna T kolekcji, podobnie jak w numpy
print(df3.T)

# Listing 3 - filtrowanie, grupowanie i agregowanie danych

s = pd.Series([10, 12, 8, 14], index=['a', 'b', 'c', 'd'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'], 'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847526]}
df = pd.DataFrame(data)
print(df)
# wyświetla dane z serii gdzie wartość większa od 1
print(s[(s > 9)])
# nieco inny efekt można oosiagnąć wykorzystując funkcję where, która zwraca kolekcję w oryginalnej wielkości
# (liczebności) elementów, ale wartości nie spełniające warunku uzupełnia wartość NaN
print(s.where(s > 10))
# możemy też podać wartość, która zostanie podstawiona zamiast NaN
print(s.where(s > 10, 'za duże'))
# jeszcze inna własnośc where pozwala na modyfikowanie oryginalnego zbioru (domyślnie zwracana jest kopia)
seria = s.copy()
seria.where(seria > 10, 'za duże', inplace=True)
print("########")
print(seria)

# wyświetla dane z serii gdzie wartość nie jest większa od 10
print(s[~(s > 10)])
# warunki możemy też łączyć
print(s[(s < 13) & (s > 8)])

# warunki dla pobierania DataFrame
print(df[df['Populacja'] > 1200000000])
# bardziej skomplikowane warunki
print(df[(df.Populacja > 1000000) & (df.index.isin([0, 2]))])

# inny przykład z listą dopuszczalnych wartości oraz isin zwracają wartości boolowskie
print('#########')
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))

# zmiana, usuwanie i dodawanie danych

# w przypadku serii możemy dodać/zmienić wartowść poprzez odwołanie się do elementu serii przez klucz (indeks)
s['e'] = 15
print(s.e)
s['f'] = 16
print(s)

# podobna operacja dla DataFrame ma nieco inny efekt - wartość ustawiona dla wszystkich kolumn
df.loc[3] = 'dodane'
print(df)
# ale można dodać wiersz w postaci listy
df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)

# usuwanie danych można wykonać przez funkcję drop, ale pamiętajmy, że operacja nie wykonuje się in=place więc
# zwracana jest kopia DataFrame z usuniętymi wartościami
new_df = df.drop([3])
print(new_df)
# więc jeżeli chcemy zmienić pierwotny zbiór dodajemy parametr inplace=True
df.drop([3], inplace=True)
print(df)
# można usuwać również całe kolumny po nazwie indeksu, ale wykonanie tej komendy uniemożliwi
# wykonanie dalszego kodu (można przetwstować po zakomentowaniu dalszej części listingu)
# df.drop('Kraj', axis = 1, inplace=True)

# do DataFrame możemy dodawać również kolumny zamiast wierszy
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka południowa', 'Europa']
print(df)

# Pandas ma również własne funkcje sortowania danych
print(df.sort_values(by='Kraj'))

# grupowania
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
# można też jak w SQL czy Excelu uruchomić funkcje agregujące na danej kolumnie
print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))


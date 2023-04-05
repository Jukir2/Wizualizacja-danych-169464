import math

 # Zad1
 a = pow(math.e, 10)
 print(a)
 b = math.pow(math.log(5 + pow(math.sin(8), 2)), 1.0 / 6)
 print(b)
 c = 3.0 + 0.55
 print(float(c))
 d = 4.80
 print(float(d))

 # Zad2
 imie = "JAKUB"
 nazwisko = "MICHALSKI"
 print(imie.capitalize() + " " + nazwisko.capitalize())

 # Zad3
 string = "Zabiłem byka, cóż to był za byk. Krew z niego sika, siku siku sik! La la, la la la la la la!"
 print(string.count("la"))

 # Zad4
 zmienna_lancuchowa = "Siedemnaście"
 print(zmienna_lancuchowa[0] + " " + zmienna_lancuchowa[len(zmienna_lancuchowa) - 1])

 # Zad5
 string2 = string.split(" ")
 print(string2)

 # Zad6
 stringowa_zmienna = "dwanaście groszy"
# floatowa_zmienna = 320
 szesnastkowa_zmienna = 12254
 print(hex(szesnastkowa_zmienna))
 print(float(320))
 print(stringowa_zmienna)

 # Zad7
 sporty = ["Siatkówa", "Skoki narciarskie", "Piłka ręczna"]
 print(sporty)
 sporty.reverse()
 sporty.append("Piłka nożna")
 print(sporty)

 # Zad8
shortcuts = {"np": "Na przykład", "pt": "Pod tytułem", "itp": "I tym podobne"}

 # Zad9
 gry_komputerowe = {1: "World of warcraft", 2: "Terraria", 3: "League of legends", 4: "Hades"}
 print(len(gry_komputerowe))

 #Zad10
 zdanie = input()
 print(zdanie)
 print(zdanie.count("a"))

 #Zad11
 print("Podaj 3 liczby całkowite:")
 l1 = input()
 l2 = input()
 l3 = input()
 if (l1>l2) & (l1>l3):
     print(l1 + " jest największa!")
 elif (l2>l1) & (l2>l3):
     print(l2 + " jest największa!")
 elif (l3>l1) & (l3>l2):
     print(l3 + " jest największa!")
 else:
     print("liczby są takie same")

# Zad12
lista = [1, 2, 3, 4.5, 3.4, 3.2, 2, 0]
print(lista)
for x in range(0, len(lista), 1):
    lista[x] *= lista[x]
print(lista)

# Zad13
counter = 0
lista2 = []
while counter < 10:
    b = int(input())
    if b % 2 == 0:
        lista2.append(b)
    counter += 1
print(lista2)

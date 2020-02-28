# print("Hello World!")

def dluga_nazwa_funkcji():
    """ parametry: ... """ #tzw. docstring
    print("Hello World!")

# dlugaNazwaFunkcji
# Guido van Rossum
# pep8 pep0008

#łańcuch znaków
# CTRL + / - ustaw komentarz/usun komentarz
# Shift + alt + strzalka gora/dol
#łańcuch znaków

imie = 'Ala'
imie = 'Ala'
imie = """Ala ma 
kota a
kot jest glodny"""
print(type(imie))
# <class 'str'>
imie = str("Ala") # poprzez konstruktor
print(type(5))
print(type(5.6))
print(type(True))
print(type(None))
# isinstance() sprawdzam czy zmienna jest danego typu
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'NoneType'>

print("Ala " + "ma kota.")
# print("Ala " + "ma " + 5 +"kota.") blad
print("Ala " + "ma " + str(5) + "kotow.")
print(5)
ilosc_kotow = 5
print("Ala " + "ma {} kotow.".format(ilosc_kotow))
print("Ala " + f"ma {ilosc_kotow} kotow.")
print("Ala " + "ma {} {} {} kotow.".format(3, 5, 7))
liczba = 6.853213213
print(f"Liczba {liczba:.2f}") # 2 miejsca dizesietne
# http://pyformat.info 

print(imie [0])
# imie[0] = "O" nie jest mutowalny
imie = imie.lower()
print(imie)

# liczby
liczba = 1
liczbaf = 4.5
suma = liczba + liczbaf
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 * 2)
print(1 // 2) # DZIELENIE BEZ RESZTY
print(1 ** 2) # potegowanie
print(1 % 2) # modulo

print(0.1 + 0.2 == 0.3)

# listy

lista = []
lista2 = [1, 2, 3]
lista2 = [1, "Ala", 3.4, True, None]
final_list = lista + lista2 + lista3
lista2[2] # wartosc 3, indeks 2
lista4 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
lista4[1][1] # 5

# slownik
slownik = {}
slownik2 = {"klucz": "wartosc"}
slownik3 = {0: "Adam"}
slownik2["klucz"] = "costam"
slownik3[0]
slownik2.keys()
slownik2.values()
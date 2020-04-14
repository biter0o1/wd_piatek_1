def liczby(ile):
    wynik=[i for i in range(0,ile,4)]
    return wynik

print(liczby(2000))

plik = open("Cwiczenia4/plik1.py","w+")
plik.writelines(str(liczby(1000)))
plik.close()
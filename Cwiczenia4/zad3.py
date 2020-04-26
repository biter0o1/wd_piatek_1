with open("Cwiczenia4/plikdo3.py","w") as p3: 
    tekst = input('WPISZ TEKST DO PLIKU: ')
    p3.writelines(tekst)
    
with open("Cwiczenia4/plikdo3.py","r") as p3:
    for linia in p3:
        print(linia)



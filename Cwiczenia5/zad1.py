class Material:
    def __init__(self, rodzaj, dlugosc , szerokosc):
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        print(self.rodzaj,self.dlugosc,self.szerokosc)

class Ubrania(Material):
    def wyswietl_dane(self, rozmiar, kolor, dla_kogo):
        print("rozmiar:",rozmiar,
        "kolor:",kolor,
        "dla kogo:",dla_kogo,
        "rodzaj:",self.rodzaj, "dlugosc;",self.dlugosc, "szerokosc:",self.szerokosc)

class Sweter(Ubrania):
    def wyswietl_dane(self, rodzaj_swetra):
        print(
        "rodzaj:",self.rodzaj, "dlugosc;",self.dlugosc,
        "szerokosc:",self.szerokosc,"Rodzaj swetra:",rodzaj_swetra)




x = Ubrania("xyz","50cm","40cm")

x.wyswietl_dane(6,"bialy","xyz")

y = Sweter("zzz","45cm","50cm")

y.wyswietl_dane("nwm")



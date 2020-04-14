class NaZakupy:
    def __init__(self,nazwa_produktu,ilosc,jednostka_miary,cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        print("Nazwa produktu:",self.nazwa_produktu,"\nilosc:",self.ilosc,self.jednostka_miary,"\ncena jednego:",self.cena_jed,"Zł")

    def ile_produktu(self):
        print(self.ilosc,self.jednostka_miary)

    def ile_kosztuje(self):
        print("Razem kosztuje:",self.ilosc*self.cena_jed,"Zł")
        
        
        
Mleko = NaZakupy("mleko",12,"szt",2)

Mleko.wyswietl_produkt()
Mleko.ile_produktu()
Mleko.ile_kosztuje()
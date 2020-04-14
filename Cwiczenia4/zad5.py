class ciag:
    def __init__(self,a1,n,r): 
        self.a1=a1
        self.n=n
        self.r=r

    def wyswietl_dane(self):
        print(" a1=",self.a1," n=",self.n," r=",self.r,sep='')

    def pobierz_element(self): #?
        a1 = input('Podaj a1:')
        n = input('Podaj n:')
        r = input('Podaj r:') 

    def pobierz_parametry(self):
        a1 = input('Podaj a1:')
        r = input('Podaj r:')
        n = input("Podaj ilosc")

    def policz_sume(self):
        an = self.a1 + (self.n - 1) * self.r
        suma = (self.a1 + an)/2*self.n
        return suma

   # def policz_elementy(self):


x = ciag(4,5,6)

x.wyswietl_dane()
print(x.policz_sume())

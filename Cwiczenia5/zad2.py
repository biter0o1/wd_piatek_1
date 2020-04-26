class Kwadrat():

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, xyz):
        return self.x + xyz.x



kw = Kwadrat(76)
kw2 = Kwadrat(23)
wynik = kw.__add__(kw2)
print(wynik)

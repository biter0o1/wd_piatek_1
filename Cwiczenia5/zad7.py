class ite:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index % 2 == 0:
            self.index = self.index +2
        else:
            self.index = self.index +1
            
        return self.data[self.index]


lista = [i for i in range(0,100,3)]
x1= ite(lista)

print(iter(x1))
print(next(x1))
print(next(iter(x1)))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))



x2 = ite("AlaMaKotaAKotMaAle")
print(iter(x2))
print(next(x2))
print(next(x2))
print(next(x2))
print(next(x2))
print(next(x2))
print(next(x2))


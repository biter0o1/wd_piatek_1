class Ksztalty:
    def __init__(self,x):
        self.x = x
        
    def __gt__(self, xyz):
        return self.x > xyz.x

    def __ge__(self, xyz):
        return self.x >= xyz.x

    def __lt__(self, xyz):
        return self.x < xyz.x

    def __le__(self, xyz):
        return self.x <= xyz.x

class Kwadrat(Ksztalty):
    def __gt__(self, zxc):
        return self.x > zxc.x

x1 = Ksztalty(23)
x2 = Ksztalty(44)

print(x1.__gt__(x2))
print(x1.__ge__(x2))
print(x1.__lt__(x2))
print(x1.__le__(x2))

x3 = Kwadrat(50)
x4 = Kwadrat(32)

print(x3.__gt__(x4))
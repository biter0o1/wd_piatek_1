class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        
        self.index = self.index - 1
        return self.data[self.index]


x1 = Wspak("Ala ma kota")

print(x1.__iter__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())
print(x1.__next__())

x2 = Wspak([i for i in range(0,99,5)])

print(x2.__iter__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())
print(x2.__next__())

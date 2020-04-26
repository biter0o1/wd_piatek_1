class iter:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        list=('y','a','ą','e','ę','o','ó,''u','i')

        if self.data[self.index] in list:
            return self.data[self.index]

x = iter("Ala ma kota")

print(iter(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

print(isinstance(x,iter))

def gen(data):
    for index in range(0,len(data),1):
        yield data[index]


x1= gen("qwertyuiop")

print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
print(next(x1))
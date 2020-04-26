def fibo():
    list = [1, 1]
    for index in range(2, 30, 1):
        list.append(list[index-1] + list[index-2])
        yield list[index-2]


x = fibo()

for i in range(25):
    print(next(x))
def mies(list):
    for index in range(0,12):
        yield print(list[index])


list = ['Styczen',"Luty", "Marzec", "Kwiecień","Maj","Czerwiec","lipiec",
    "sierpień","Wrzesień","Październik","listopad","grudzień"]

x=mies(list)

for i in range(0,12):
    next(x)

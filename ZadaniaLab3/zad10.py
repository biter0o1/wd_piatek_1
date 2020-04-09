def listazakupow(** rzeczy):
    wynik=0
    for cos in rzeczy:
        wynik+=rzeczy[cos]
    return wynik
        


print(listazakupow(mleko=5,ser=8,ciastka=6,platki=0))
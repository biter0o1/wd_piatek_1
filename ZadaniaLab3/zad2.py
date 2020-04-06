macierz = [1,2,3,4,2,3,4,5,3,4,5,6,4,5,6,7]

print(macierz[:4])
print(macierz[4:8])
print(macierz[8:12])
print(macierz[12:16])

# lista = [i for i in macierz if macierz[i%5==0]]
lista=[]
print("")
lista.append(macierz[0])
lista.append(macierz[5])
lista.append(macierz[10])
lista.append(macierz[15])



print(lista)    
# Ten kod nie ma sensu
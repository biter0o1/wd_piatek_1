import pandas as pd
import numpy as np
import xlrd
import openpyxl

def pierwszy():
    print(imiona[imiona.Liczba>1000])

def drugi():
    print(imiona[imiona.Imie=="PAWEŁ"])

def trzeci():
    #print(sum(imiona.Liczba))
    print(imiona.agg({'Liczba':['sum']}))

def czwarty():
    print(sum(imiona.Liczba[imiona.Rok<=2005] & imiona.Liczba[imiona.Rok>=2000]))

def piaty():
    M = imiona.Liczba[imiona.Plec == 'M']
    K = imiona.Liczba[imiona.Plec == 'K']
    print("suma chłopców: ",sum(M), "suma dziewcząt: ", sum(K))

def szosty():
    x = imiona.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0)
    print(x)

def siódmy():
    x = imiona.sort_values('Liczba', ascending=False).groupby(['Plec']).nth(0)
    print(x)



x = pd.ExcelFile('Ćwiczenia8/imiona.xlsx')
imiona = pd.read_excel(x,'Arkusz1')

#pierwszy()
#drugi()
#trzeci()
#czwarty()
#piaty()
#szosty()
#siódmy()

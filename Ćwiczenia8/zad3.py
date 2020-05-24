import pandas as pd
import numpy as np

def pierwszy():
    x = df['Sprzedawca'].unique()
    print(x)

def drugi():
    x = df.sort_values('Utarg', ascending=False).iloc[range(5)]
    print(x['Utarg'])

def trzeci():
    x = df.groupby('Sprzedawca').count()
    print(x['idZamowienia'])

def czwarty():
    x = df.groupby('Kraj')
    print(x.count())

def piaty():
    x = df[(df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') & (df['Kraj']=='Polska')]
    x.groupby(['Kraj']).count
    print(x['idZamowienia'])

def szosty():
    x = df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')].mean()
    print(x['Utarg'])

def siodmy():
    x2004 = df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')]
    x2005 = df[(df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')]
    x2004.to_csv('Ćwiczenia8/zamowienia_2004.csv')
    x2005.to_csv('Ćwiczenia8/zamowienia_2005.csv')

df = pd.read_csv('Ćwiczenia8/zamowieniana.csv',delimiter=';')
#pierwszy()
#drugi()
#trzeci()
#czwarty()
#piaty()
#szosty()
#siodmy()
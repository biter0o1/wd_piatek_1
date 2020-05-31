import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Ćwiczenia8/imiona.xlsx',header=0,delimiter=';')

x = df[df['Rok']>2012].groupby('Plec').agg({'Liczba':['sum']})


x.plot.pie(subplots=True,autopct='%.2f%%',figsize=(10,7))
plt.show()
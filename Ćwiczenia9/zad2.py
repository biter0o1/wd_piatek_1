import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Ćwiczenia8/imiona.xlsx',header=0,delimiter=';')

x = df.groupby('Plec').agg({'Liczba':['sum']})


x.plot(kind='bar')

plt.legend(loc='lower center')
plt.xticks(rotation=0)
plt.show()
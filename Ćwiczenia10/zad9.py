import pandas as pd 
import matplotlib.pyplot as plt

x = pd.read_csv('Ćwiczenia8/zamowieniana.csv', delimiter=';')
ile=x.groupby(['Sprzedawca']).count()['idZamowienia']

plt.pie(ile, labels=ile.index.values, autopct = lambda pct: "{:.1f}%".format(pct), shadow = True, explode =(0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,))
plt.legend(title='Sprzedawcy', loc = 4, framealpha=0.5)
plt.show()
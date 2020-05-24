import pandas as pd 
import matplotlib.pyplot as plt

x = pd.read_csv('Ćwiczenia8/zamowieniana.csv', delimiter=';')
ile=x.groupby(['Sprzedawca']).count()['idZamowienia']

plt.subplot(2,1,1)
plt.pie(ile, labels=ile.index.values,autopct = lambda pct: "{:.1f}%".format(pct), shadow = True, explode =(0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,))
plt.annotate('Środek',xy=(0,0), xytext=(1.5,1.5),arrowprops=dict(facecolor='blue', shrink=1))

plt.subplot(2,1,2)
x = pd.ExcelFile('Ćwiczenia8/imiona.xlsx')
imiona = pd.read_excel(x,'Arkusz1')

K=(imiona.groupby(['Plec','Rok']).agg(sum).loc['K'])['Liczba']
M=(imiona.groupby(['Plec','Rok']).agg(sum).loc['M'])['Liczba']

plt.bar(K.index.values,K.values, label='Kobiety')
plt.bar(M.index.values,M.values, label='Mezczyzni', bottom = K.values)
plt.legend(loc='lower right')
plt.annotate('Najwiecej',xy=(2008.5,300000), xytext=(2000,300000),arrowprops=dict(facecolor='blue', shrink=1))


plt.show()

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Ćwiczenia8/zamowieniana.csv',header=0,delimiter=';')

x = df.groupby('Sprzedawca').agg({'idZamowienia':['count']})

x.plot.bar()
plt.show()
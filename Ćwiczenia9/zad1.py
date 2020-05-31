import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Ćwiczenia8/imiona.xlsx',header=0,delimiter=';')

x = df.groupby('Rok').sum()

x.plot(xticks=df['Rok'].unique())
plt.show()
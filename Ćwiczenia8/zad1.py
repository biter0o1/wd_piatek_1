import pandas as pd
import numpy as np
import xlrd
import openpyxl

x = pd.ExcelFile('Ćwiczenia8/imiona.xlsx')
imiona = pd.read_excel(x,'Arkusz1')
print(imiona)
import pandas as pd
from pandas.core.arrays import string_
import numpy as np
import openpyxl


def porcentaje_buscar (variableBuscar , variableDondeBuscar):
    longitudReferecia = 0
    porcentajeComparacion = 0
    for a in variableBuscar: # genero la longitud de la referencia a buscar
        if a ==" " or a ==".":
            continue
        longitudReferecia = longitudReferecia + 1
        
    for i in variableDondeBuscar: # eferencia a la que se quiere comparar
        if i==" " or i==".": # no comparo los espacios ni los .
            continue
        for b in variableBuscar: # referencia que se quiere buscar
            if b==" " or b==".": # no comparo los espacios ni los .
                continue
            if (b.upper()) == (i.upper()) : # verifico que esten en mayuscula
                porcentajeComparacion = porcentajeComparacion + 1
                break
    porcentajeComparacion = (porcentajeComparacion * 100) / longitudReferecia             
    return porcentajeComparacion

'''df_excel = pd.read_excel(io="inventario.xlsx", sheet_name="Reconteo")
df_excel['Cantidad Sistema'] = np.mean(df_excel, axis=1)
print(df_excel['Cantidad Sistema'])'''

'''imprimir = porcentaje_buscar("6203 2rs", "6203 2RS")
print(imprimir)'''
df = pd.read_excel("data/Inventario.xlsx")
df2 = pd.read_excel("QH.xlsx")
'''print(df)'''
'''print(df[['REFERENCIA REAL']])'''
print(df2)



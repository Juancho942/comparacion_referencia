from ast import For
import pandas as pd
from pandas.core.arrays import string_
import numpy as np
import openpyxl as py


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

'''imprimir = porcentaje_buscar("6203 2rs", "6203 2RS")
print(imprimir)'''
cci = pd.read_excel("data/Elementos de inventario.xlsx")
qh = pd.read_excel("data/QH.xlsx")
resultado = pd.DataFrame(columns=['Ref CCi', 'Ref QH','porcentaje'])
#SYB = pd.read_excel("data/SYB.xls")
#print(QH[["REFERENCIA","MARCA"]])
#print(CCI[["Código","Ref. fabricante","Marca"]])
referenciaCci = cci["Ref. fabricante"]
referenciaQh = qh["REFERENCIA"]
for a in referenciaCci:
    for b in referenciaQh:
        if (porcentaje_buscar(a,b) > 100.0) :
            print(a," ",b)
        '''if porcentaje > 80:
            resultado['Ref Cci'] = referenciaCci
            resultado['Ref Qh'] = referenciaQh
            resultado['porcentaje'] = porcentaje
        print(resultado)'''

        



from ast import For
import pandas as pd
from pandas.core.arrays import string_
import numpy as np
import openpyxl as py


def porcentaje_buscar (variableBuscar , variableDondeBuscar):
    longitudReferecia = 0
    porcentajeComparacion = 0
    if (len(variableBuscar)>len(variableDondeBuscar)):
        variableMayor = variableBuscar
        variableMenor = variableDondeBuscar
    else:
        variableMayor = variableDondeBuscar
        variableMenor = variableBuscar
    for a in variableMenor: # genero la longitud de la referencia a buscar
        if a == " " or a == ".":
            continue
    longitudReferecia = longitudReferecia + 1
        
    estado = 0    
    for i in variableMayor: # eferencia a la que se quiere comparar
        if i is " " or i is ".": # no comparo los espacios ni los .
            continue
        for b in variableMenor: # referencia que se quiere buscar
            if b is " " or b is ".": # no comparo los espacios ni los .
                continue
            if (b) is (i) and estado < 2: # verifico que esten en mayuscula
                porcentajeComparacion += 1
                estado = 1
                break
            elif estado == 1:
                estado = 2
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
        #if (porcentaje_buscar(str(a),str(b)) > 100.0) :
        '''porcentaje = porcentaje_buscar(str(a),str(b))
        if (porcentaje > 70):
            print(a," ",b," : ",porcentaje )'''
        print(a, "zise : ", len(a))
        print(b, "zise : " ,len(b))
        print((a[1]==b[1]))



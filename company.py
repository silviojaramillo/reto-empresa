'''
Una empresa de camisetas ha tenido muchos problemas últimamente
con sus últimas ventas para las ciudades de Cartagena, Barranquilla, 
Medellín y Bogotá. Luego de culminar la temporada no han contado 
adecuadamente las unidades vendidas y están muy preocupados porque
no saben cuál es el total vendido hasta la fecha. El gerente nacional
se ha puesto en contacto contigo para discutir como seria el programa
que necesitan y te ha enviado la siguiente tabla:
Talla      Precio
'S'        2500,
'M'        3400,
'L'        5200,
'XL'       6000,
'XXL'      9000
“Estos serían los precios de cada camiseta” te dijo en la reunión, 
además de esto te envía un diccionario indicando cada una de las 
unidades en la ciudad correspondiente:
{
'Cartagena': ['M', 'S', 'L', 'L', 'L', 'L', 'L', 'XL', 
'XXL', 'S', 'S', 'L', 'M', 'M', 'M', 'S', 'S', 'M', 'M'],
'Barranquilla': ['S', 'S', 'L', 'M', 'XL', 'S', 'L', 'M', 
'M', 'M', 'S', 'S', 'M', 'M', 'XL', 'S', 'M', 'S', 'XXL', 'XL', 'L'],
'Medellín': ['L', 'L', 'XL', 'XXL', 'S', 'S', 'S', 'S', 'L', 'L', 
'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 
L', 'L', 'M', 'M', 'S', 'S', 'S', 'S', 'XL', 'L'],
'Bogotá': ['M', 'S', 'S', 'M', 'M', 'X', 'S', 'M', 'S', 
'S', 'S', 'L', 'S', 'S', 'S', 'M', 'M','M', 'M', 'M', 'M', 'M', 
'M', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'M', 'M', 'M', 'M', 
'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL' ]}
Diseña un programa que lea el diccionario e indique el 
total de ventas, las tallas más vendidas y el total de tallas por ciudad.
'''
import os
import pandas as pd
import numpy as np
os.system('cls')
talla_precio = {
'S':2500,
'M':3400,
'L':5200,
'XL':6000,
'XXL':9000}
tallas = list(talla_precio.keys())
precios = list(talla_precio.values())
ventas = {
'Cartagena': ['M', 'S', 'L', 'L', 'L', 'L', 'L', 'XL', 'XXL', 
'S', 'S', 'L', 'M', 'M', 'M', 'S', 'S', 'M', 'M'],
'Barranquilla': ['S', 'S', 'L', 'M', 'XL', 'S', 'L', 'M', 
'M', 'M', 'S', 'S', 'M', 'M', 'XL', 'S', 'M', 'S', 'XXL', 'XL', 'L'],
'Medellín': ['L', 'L', 'XL', 'XXL', 'S', 'S', 'S', 'S', 'L', 'L', 
'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'L', 'L', 'L', 'L', 'L', 'L', 
'L', 'L', 'L', 'M', 'M', 'S', 'S', 'S', 'S', 'XL', 'L'],
'Bogotá': ['M', 'S', 'S', 'M', 'M', 'X', 'S', 'M', 'S', 'S', 
'S', 'L', 'S', 'S', 'S', 'M', 'M','M', 'M', 'M', 'M', 'M', 'M', 
'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL', 'M', 'M', 'M', 'M', 
'M', 'M', 'M', 'M', 'M', 'M', 'L', 'L', 'XL', 'XL', 'XL', 'XL', 'XL' ]}
ciudades = list(ventas.keys())
cantidad_tallas_vendidas_ciudad = {}
total_ventas = 0
tallas_mas_vendidas = {}
listado_mayores_tallas_vendidas = []
for ven in ventas:
    ciudad = []
    ciudad.append(ventas.get(ven).count('S'))
    ciudad.append(ventas.get(ven).count('M'))
    ciudad.append(ventas.get(ven).count('L'))
    ciudad.append(ventas.get(ven).count('XL'))
    ciudad.append(ventas.get(ven).count('XXL'))
    cantidad_tallas_vendidas_ciudad[ven] = ciudad
    ciudad.clear
for mas in cantidad_tallas_vendidas_ciudad:
    talla_con_ventas_mayores = cantidad_tallas_vendidas_ciudad.get(mas)
    valor_mayor_venta = max(talla_con_ventas_mayores)
    if(talla_con_ventas_mayores.count(valor_mayor_venta) > 1):
        for i in range(len(talla_con_ventas_mayores)):
            if(talla_con_ventas_mayores[i] == valor_mayor_venta):
                tallas_mas_vendidas[mas+tallas[i]] = valor_mayor_venta
    else:
        tallas_mas_vendidas[mas+tallas[talla_con_ventas_mayores.index(valor_mayor_venta)]] = valor_mayor_venta
    for x in range(len(talla_con_ventas_mayores)):
        total_ventas += talla_con_ventas_mayores[x] * precios[x]
lista_tallas_mas_vendidas = list(tallas_mas_vendidas.keys())
print(f"El total de las ventas es: {total_ventas}")
print('Las tallas más vendidas son: ')
for k in range(len(lista_tallas_mas_vendidas)):
    cadena = lista_tallas_mas_vendidas[k]
    if(cadena[-1] == 'S', cadena[-1] == 'M'):
        listado_mayores_tallas_vendidas.append(cadena[-1])
    elif('XXL' in cadena):
        listado_mayores_tallas_vendidas,np.append('XXL')
    elif('XL' in cadena):
        listado_mayores_tallas_vendidas,np.append('XL')
listado_mayores_tallas_vendidas = set(listado_mayores_tallas_vendidas)
listado_mayores_tallas_vendidas = list(listado_mayores_tallas_vendidas)
for u in range(len(listado_mayores_tallas_vendidas)):
    print(f"{listado_mayores_tallas_vendidas[u]}")
print('La cantidad de tallas vendidas por ciudad son: ')
df = pd.DataFrame([key for key in cantidad_tallas_vendidas_ciudad.keys()], columns=['Ciudad'])
df['S'] = [value[0] for value in cantidad_tallas_vendidas_ciudad.values()]
df['M'] = [value[1] for value in cantidad_tallas_vendidas_ciudad.values()]
df['L'] = [value[2] for value in cantidad_tallas_vendidas_ciudad.values()]
df['XL'] = [value[3] for value in cantidad_tallas_vendidas_ciudad.values()]
df['XXL'] = [value[4] for value in cantidad_tallas_vendidas_ciudad.values()]
print(df)
import pandas as pd

frutas = ['Uvas', 'Fresa', 'Sandia', 'Naranja']

NuevaSerie = pd.Series(frutas)
print(NuevaSerie)

Datos = pd.Series([2,4,5,6,6,8,9])
print(Datos)

#acceder a un dato en especifico

print(f'dato especifico de la serie: {Datos[5]}')
print(f'El dato de la serie de la fruta: {NuevaSerie[2]}')

indece = ['A', 'B', 'C', 'D', 'E', 'F']
impares = pd.Series([11, 13, 15, 17, 19, 21], index=indece)
print(impares)
print(f'el dato en la posición marcada es: {impares['C']}')

print(f'Los datos de la serie son: {NuevaSerie.head(2)}')

#ultimos elementos de la serie
print(f'Los ultimos datos de la serie son: {NuevaSerie.tail(2)}')

#estadisticas de la serie
print(f'Estadisticas de la serie: {Datos.describe()}')

#Orden de la serie
print(f'Orden de la serie: {Datos.sort_values()}')
print(f'Minimo de la serie de Datos: {Datos.min()}')
print(f'Maximo de la serie de Datos: {Datos.max()}')
print(f'Cantidad de elementos en la serie de Datos: {NuevaSerie.count()}')
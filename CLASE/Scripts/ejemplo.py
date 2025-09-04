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
import pandas as pd 

SegundaSerie = []

Usuarios = int(input('Ingrese la cantidad de datos que desea registrar: '))

for i in range(Usuarios):
    dato = int(input(f'Ingrese el dato {i+1}: '))
    SegundaSerie.append(dato)

SegundaSerie = pd.Series(SegundaSerie)
print(f'Los datos ingresados son: {SegundaSerie}')

print(f'La estadistica de la serie es : {SegundaSerie.describe()}')
print(f'El orden de la serie es: {SegundaSerie.sort_values()}')
print(f'El minimo de la serie es: {SegundaSerie.min()}')
print(f'El maximo de la serie es: {SegundaSerie.max()}')

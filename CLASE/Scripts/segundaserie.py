import pandas as pd 

SegundaSerie = []

Usuarios = int(input('Ingrese la cantidad de datos que desea registrar: '))

for i in range(Usuarios):
    dato = int(input(f'Ingrese el dato {i+1}: '))
    SegundaSerie.append(dato)

print(f'Los datos ingresados son: {SegundaSerie}')

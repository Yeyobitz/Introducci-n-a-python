"""
Para un supermercado se necesita llevar el control de las ventas, para esto se debe:
 -Ingresar la cantidad de sucursales a considerar (validar mayor a 0).
 -Para cada una de las sucursales, ingresar el total de ventas (validar mayor a 0).
 Al final, mostrar:
 -el promedio de los totales de ventas,
 -la cantidad de totales menores a 1000000 y
 -la cantidad de totales mayores o igual a 1000000.
(Pista, al leer cada total, acumularlo y preguntar si es menor a 1000000, si es así incrementar un contador en 1, si no es así incrementar otro contador en 1.
Al final mostrar el promedio y ambos contadores)
 """


sucursales = int(input('Ingrese la cantidad de sucursales: '))
while sucursales <= 0:
    sucursales = int(input('Error, ingrese la cantidad de sucursales: '))
total = 0
menor = 0
mayor = 0
for i in range(sucursales):
    ventas = int(input('Ingrese el total de ventas: '))
    while ventas <= 0:
        ventas = int(input('Error, ingrese el total de ventas: '))
    total += ventas
    if ventas < 1000000:
        menor += 1
    else:
        mayor += 1
        
print('El promedio de los totales de ventas es: ', total/sucursales)
print('La cantidad de totales menores a 1000000 es: ', menor)
print('La cantidad de totales mayores o igual a 1000000 es: ', mayor)


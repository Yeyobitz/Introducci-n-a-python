"""
En una multitienda nacional se desea calcular el total en ventas de este mes de los artículos, en cada sucursal, 
para esto se debe construir un algoritmo que realice lo siguiente: 
Ingresar la cantidad de sucursales a considerar (validar entre 2 y 4).
Para cada una de las sucursales, pedir la cantidad de artículos a considerar (validar entre 2 y 5).
Para cada artículo, pedir la cantidad vendida y el precio (validarlos mayor a 0), y multiplicar estos para tener el total 
de la venta.
Ir sumando el total de venta de cada artículo de todas las sucursales.
Al final se debe mostrar el total de ventas final de todos los artículos.
(Pista: se debe anidar un for dentro de otro. El for de afuera para la cantidad de sucursales y el for de adentro para la 
cantidad de artículos.) 
"""

# Inicializar variables
totalVentas = 0
i = 0
j = 0

# Ingreso de datos
sucursales = int(input("Ingrese la cantidad de sucursales a considerar (entre 2 y 4): "))
while sucursales < 2 or sucursales > 4:
    sucursales = int(input("Error, ingrese una cantidad válida de sucursales (entre 2 y 4): "))

# Loop
for i in range(sucursales):
    articulos = int(input("Ingrese la cantidad de artículos a considerar (entre 2 y 5): "))
    while articulos < 2 or articulos > 5:
        articulos = int(input("Error, ingrese una cantidad válida de artículos (entre 2 y 5): "))

    for j in range(articulos):
        cantidad = int(input("Ingrese la cantidad vendida del artículo: "))
        while cantidad <= 0:
            cantidad = int(input("Error, ingrese una cantidad válida de artículos: "))

        precio = int(input("Ingrese el precio del artículo: "))
        while precio <= 0:
            precio = int(input("Error, ingrese un precio válido: "))

        totalVentas += cantidad * precio

print("El total de ventas es de $" + str(totalVentas))


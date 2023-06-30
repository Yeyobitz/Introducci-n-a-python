"""
En un vivero, al iniciar un día de venta, se realiza lo siguiente:
   Mientras se responda afirmativamente a continuar (validar sólo las letras s y n, en 
   minúsculas):
-	Leer la cantidad de plantas a analizar (validar como mayor a cero y controlar 
    excepción para que sea número).
-	Llamar a una función enviando como parámetro la cantidad de plantas.
-	Dentro de la función, por cada planta leer su nombre y el precio.
-	Luego de leer y sumar todos los precios, retornar esta suma.
-	Mostrar la suma retornada, disminuir esta suma en 5% y mostrar la suma final.


Necesito que se haga lo más simple y como un estudiante lo haría. Se explicará en
detalle como se debe hacer con comentarios en el código.
"""
def plantas(cantidad):
    suma = 0
    for i in range(cantidad):
        nombre = input('Ingrese el nombre de la planta: ')
        precio = int(input('Ingrese el precio de la planta: '))
        suma += precio
    return suma

continuar = input('Desea continuar? (s/n): ')
while continuar != 's' and continuar != 'n':
    continuar = input('Error, desea continuar? (s/n): ')
while continuar == 's':
    while True:
        try:
            cantidad = int(input('Ingrese la cantidad de plantas a analizar: '))
            while cantidad <= 0:
                cantidad = int(input('Error, ingrese la cantidad de plantas a analizar: '))
            suma = plantas(cantidad)
            print('La suma es de ' + str(suma))
            print('La suma final es de ' + str(suma * 0.95))
            break
        except ValueError:
            print('Error, ingrese un numero entero')
    continuar = input('Desea continuar? (s/n): ')
    while continuar != 's' and continuar != 'n':
        continuar = input('Error, desea continuar? (s/n): ')
print('Fin del programa')

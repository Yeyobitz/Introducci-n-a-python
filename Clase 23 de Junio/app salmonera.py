"""
Una Salmonera necesita una aplicación computacional, para gestionar sus ventas de su recurso salmón. 

Usando funciones, realizar lo que se indica a continuación: 
 
Todo lo siguiente se ejecuta hasta elegir la opción s: 

Escribir en pantalla estas 5 líneas: 

MENÚ 

Venta (v) 

Aumentar stock (a) 

Salir (s) 

Ingrese la letra de una opción= 

Si ingresa v: 

Ejecutar lo siguiente hasta responder negativamente a continuar. 

Ingrese la cantidad a vender (validar mayor a 0 y controlar ValueError). Pedir el precio y calcular el pago.  Acumular los pagos y retornar el resultado. 

Si ingresa a: 

Ejecutar lo siguiente hasta responder negativamente a continuar. 

Ingrese la cantidad para aumentar el stock (validar mayor a 0 y controlar ValueError). 

Sumar esta cantidad al stock del recurso y retornar el stock resultante. 

Si ingresa s: 

Se detiene la estructura cíclica principal y se muestra el total en pago hecho y el stock actual. 

Hacerlo como en puntaje juego.py
"""

def venta():
    while True:
        try:
            suma = 0
            continuar = 's'
            while continuar == 's':
                cantidad = int(input('Ingrese la cantidad a vender: '))
                while cantidad <= 0:
                    cantidad = int(input('Error, ingrese la cantidad a vender: '))
                precio = int(input('Ingrese el precio: '))
                while precio <= 0:
                    precio = int(input('Error, ingrese el precio: '))
                pago = cantidad * precio
                suma += pago
                continuar = input('Desea continuar? (s/n): ')
                while continuar != 's' and continuar != 'n':
                    continuar = input('Error, desea continuar? (s/n): ')
            return suma
        except ValueError:
            print('Error, ingrese un numero entero')

def aumentar_stock():
    while True:
        try:
            suma = 0
            continuar = 's'
            while continuar == 's':
                cantidad = int(input('Ingrese la cantidad para aumentar el stock: '))
                while cantidad <= 0:
                    cantidad = int(input('Error, ingrese la cantidad para aumentar el stock: '))
                suma += cantidad
                continuar = input('Desea continuar? (s/n): ')
                while continuar != 's' and continuar != 'n':
                    continuar = input('Error, desea continuar? (s/n): ')
            return suma
        except ValueError:
            print('Error, ingrese un numero entero')

def main():
    while True:
        print('MENU')
        print('Venta (v)')
        print('Aumentar stock (a)')
        print('Salir (s)')
        opcion = input('Ingrese la letra de una opcion: ')
        while opcion != 'v' and opcion != 'a' and opcion != 's':
            opcion = input('Error, ingrese la letra de una opcion: ')
        if opcion == 'v':
            pago = venta()
        elif opcion == 'a':
            stock = aumentar_stock()
        else:
            break
    print(f'El total en pago hecho es {pago} y el stock actual es {stock}')

main()

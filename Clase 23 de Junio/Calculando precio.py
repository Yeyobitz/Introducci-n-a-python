"""
Leer un precio (validarlo mayor a cero y controlar ValueError) 

Llamar a una función enviándole este precio. 

Dentro de la función pedir otro número (validarlo mayor a cero y controlar ValueError) y sumárselo
al que se envió. 

Calcular el 5% del resultado anterior y retornar este resultado. 

Afuera de la función, si lo retornado es mayor a 3000 escribir “Alto” sino escribir “Normal”. 

"""

def suma(precio):
    while True:
        try:
            numero = int(input('Ingrese un numero: '))
            while numero <= 0:
                numero = int(input('Error, ingrese un numero: '))
            return (precio + numero) * 0.05
        except ValueError:
            print('Error, ingrese un numero entero')
while True:
    try:
        precio = int(input('Ingrese un precio: '))
        while precio <= 0:
            precio = int(input('Error, ingrese un precio: '))
        resultado = suma(precio)
        if resultado > 3000:
            print('Alto')
        else:
            print('Normal')
    except ValueError:
        print('Error, ingrese un numero entero')


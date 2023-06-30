"""
Para un juego, se lleva el siguiente registro de puntajes:
-	Leer la cantidad de puntajes a registrar (validar esta cantidad entre 10 y 100, 
y controlar excepción para que sea número).
-	Llamar a una función que lea cada puntaje (validar este puntaje como mayor a 
cero y controlar excepción para que sea número). Disminuir cada puntaje en un 2%, 
para así obtener un puntaje con descuento. Ir sumando estos puntajes con descuento 
para luego calcular el promedio.
-	Si el promedio de todos los puntajes con descuento es mayor a 50, escribir el 
promedio (redondeado con dos decimales) y el mensaje “Alto puntaje” sino si el 
promedio está entre 20 y 50 escribir el promedio (redondeado con dos decimales) y 
el mensaje “Puntaje Medio” sino escribir el promedio (redondeado con dos decimales) 
y el mensaje “Bajo Puntaje”.
"""
def puntajes():
    while True:
        try:
            cantidad = int(input('Ingrese la cantidad de puntajes a registrar: '))
            while cantidad < 10 or cantidad > 100:
                cantidad = int(input('Error, ingrese la cantidad de puntajes a registrar: '))
            suma = 0
            for i in range(cantidad):
                puntaje = int(input('Ingrese el puntaje: '))
                while puntaje <= 0:
                    puntaje = int(input('Error, ingrese un puntaje mayor a 0: '))
                suma += puntaje * 0.98
            promedio = suma / cantidad
            return promedio
        except ValueError:
            print('Error, ingrese un numero entero')

promedio = puntajes()
if promedio > 50:
    print('Alto puntaje')
elif promedio >= 20 and promedio <= 50:
    print('Puntaje Medio')
else:
    print('Bajo Puntaje')
print('El promedio es de ' + str(round(promedio, 2)))


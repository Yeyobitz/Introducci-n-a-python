"""
Para manejar el puntaje de un juego, se necesita una aplicación computacional, usando funciones, que 
realice lo que se indica a continuación: 

Todo lo siguiente se ejecuta hasta elegir la opción f: 

Estas 5 líneas deben aparecer en pantalla: 

JUEGO 

Aciertos (a) 

Errores (e) 

Finalizar (f) 

Qué elige?= 

Con a: 

Ejecutar lo siguiente hasta responder negativamente a continuar. 

Se deben ingresar los puntos de acierto (validar mayor a 0 y controlar ValueError). 

Sumar estos puntos al puntaje actual, si el puntaje resultante es mayor a 100 agregar 5 puntos extras. 
Retornar la suma de puntos de acierto. 

Con e: 

Ejecutar lo siguiente hasta responder negativamente a continuar. 

Se deben ingresar los puntos de error (validar mayor a 0 y controlar ValueError). 

Ir sumando estos puntos de error. Retornar la suma de puntos de error.  

Con f: 

Detiene la estructura cíclica principal, se muestra el puntaje final del jugador y la cantidad de vidas 
perdidas. Indicar como ganador si tiene menos de 5 vidas perdidas.  
"""

def aciertos():
    while True:
        try:
            suma = 0
            continuar = 's'
            while continuar == 's':
                puntos = int(input('Ingrese los puntos de acierto: '))
                while puntos <= 0:
                    puntos = int(input('Error, ingrese los puntos de acierto: '))
                suma += puntos
                continuar = input('Desea continuar? (s/n): ')
                while continuar != 's' and continuar != 'n':
                    continuar = input('Error, desea continuar? (s/n): ')
            if suma > 100:
                suma += 5
            return suma
        except ValueError:
            print('Error, ingrese un numero entero')

def errores():
    suma = 0
    continuar = 's'
    while True:
        while continuar == 's':
            puntos = int(input('Ingrese los puntos de error: '))
            while puntos <= 0:
                puntos = int(input('Error, ingrese los puntos de error: '))
            suma += puntos
            continuar = input('Desea continuar? (s/n): ')
            while continuar != 's' and continuar != 'n':
                continuar = input('Error, desea continuar? (s/n): ')
        return suma

def juego():
    print('JUEGO')
    print('Aciertos (a)')
    print('Errores (e)')
    print('Finalizar (f)')
    opcion = input('Que elige? (a/e/f): ')
    while opcion != 'f':
        if opcion == 'a':
            acierto = aciertos()
            print('Puntaje de acierto: ', acierto)
        elif opcion == 'e':
            error = errores()
            print('Puntaje de error: ', error)
        else:
            print('Error, ingrese una opcion valida')
        opcion = input('Que elige? (a/e/f): ')
    print('Puntaje final: ', acierto)
    print('Cantidad de vidas perdidas: ', error)
    if error < 5:
        print('Ganador')
    else:
        print('Perdedor')

juego()
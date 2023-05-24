"""
Dentro de un while infinito, leer para cada encomienda el peso en kilos (validarlo entre 1 y 20) y los kilometros a transportarlo.
Si el peso es menor o igual a 10, preguntar si el traslado es de más de 20km, si es así escribir 'valor_1', sino escribir 'valor_2.
Si el peso no es menor o igual a 10, preguntar si el traslado es menor a 10km, si es así escribir 'valor_3', sino escribir 'valor_4'.
Si se intresa un peso 0, salir del while infinito y mostrar cuantos quedaron en cada tipo de valor. 

"""
peso = 0
km = 0
valor_1 = 0
valor_2 = 0
valor_3 = 0
valor_4 = 0

while True:
    peso = float(input('Ingrese peso (0 para salir): '))
    if peso !=0:    
        while peso < 1 or peso > 20:
            peso = float(input('Error, ingrese peso (0 para salir): '))

        km = float(input('Ingrese kilometros: '))
        if peso <= 10:
            if km > 20:
                valor_1 += 1
                print('Agregado a valor 1 (Peso <= 10 y km > 20): ', valor_1)
            else:
                valor_2 += 1
                print('Agregado a valor 2 (Peso <= 10 y km <= 20): ', valor_2)
        else:
            if km < 10:
                valor_3 += 1
                print('Agregado a valor 3 (Peso > 10 y km < 10): ', valor_3)
            else:
                valor_4 += 1
                print('Agregado a valor 4 (Peso > 10 y km >= 10): ', valor_4)
    else:
        break

print('Valores: '
            ,'\nValor 1: ', valor_1
            ,'\nValor 2: ', valor_2
            ,'\nValor 3: ', valor_3
            ,'\nValor 4: ', valor_4
            )


    

    
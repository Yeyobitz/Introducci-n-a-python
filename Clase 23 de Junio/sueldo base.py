"""
En el código principal, leer un sueldo base (validar mayor o igual a 400000 y controlarle ValueError). 
Leer un porcentaje de bono con decimales (validar entre 0 y 100, y controlarle ValueError).
Leer un porcentaje de descuento con decimales (validar entre 0 y 100, y controlarle ValueError). 
Llamar a una función con estos tres valores. 
La función calculará el sueldo final y lo mostrará.  

La función avisará si el sueldo final es alto si da mayor a 2000000, sino avisará que es bajo. 
"""
    
def sueldo_final(sueldo, bono, descuento):
    sueldo_final = sueldo + (sueldo * bono / 100) - (sueldo * descuento / 100)
    print('El sueldo base es: ', sueldo)
    print('El porcentaje de bono es: ', sueldo * bono /100,)
    print('El porcentaje de descuento es: ', sueldo * descuento / 100)
    print('El sueldo final es: ', sueldo_final)
    if sueldo_final > 2000000:
        print('Sueldo alto')
    else:
        print('Sueldo bajo')

while True:
    try:
        sueldo = int(input('Ingrese el sueldo base: '))
        while sueldo < 400000:
            sueldo = int(input('Error, ingrese el sueldo base: '))
        bono = float(input('Ingrese el porcentaje de bono: '))
        while bono < 0 or bono > 100:
            bono = float(input('Error, ingrese el porcentaje de bono: '))
        descuento = float(input('Ingrese el porcentaje de descuento: '))
        while descuento < 0 or descuento > 100:
            descuento = float(input('Error, ingrese el porcentaje de descuento: '))
        sueldo_final(sueldo, bono, descuento)
    except ValueError:
        print('Error, ingrese un numero entero')


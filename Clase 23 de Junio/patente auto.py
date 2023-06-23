"""
En el código principal, mientras pulsemos s a seguir (validar s y n), nos debe pedir una patente de auto, 
su precio diario de arriendo y la cantidad de días que han pasado desde su retiro (validar ambos mayor a 0 
y controlarles ValueError).  

Luego: 

Llamar a una función que reciba la patente y el precio diario de arriendo, para que la función muestre el 
precio con IVA. 

Luego, llamar a otra función enviándole la patente y la cantidad de días que han pasado desde su retiro. 
Esta función, que tiene internamente una cantidad correspondiente a los días de vencimiento, debe retornar
la diferencia entre la cantidad de días de vencimiento y la cantidad de días que han pasado desde su retiro. 
Si la diferencia es mayor o igual a cero escribir Aún no vence, en caso contrario escribir Vencido. 
"""

def precio_iva(patente, precio):
    print('El precio con IVA del auto ', patente, ' es: ', precio*1.21)

def dias_vencimiento(patente, dias):
    vencimiento = 30
    if dias < vencimiento:
        print('El auto ', patente, ' aun no vence')
    else:
        print('El auto ', patente, ' vencio')
        
seguir = 's'
while seguir == 's':
    while True:
        try:
            patente = input('Ingrese la patente del auto: ')
            precio = int(input('Ingrese el precio diario de arriendo: '))
            while precio <= 0:
                precio = int(input('Error, ingrese el precio diario de arriendo: '))
            dias = int(input('Ingrese la cantidad de dias desde su retiro: '))
            while dias <= 0:
                dias = int(input('Error, ingrese la cantidad de dias desde su retiro: '))
            precio_iva(patente, precio)
            dias_vencimiento(patente, dias)
            seguir = input('Desea seguir? s/n: ')
            while seguir != 's' and seguir != 'n':
                seguir = input('Error, desea seguir? s/n: ')
        except ValueError:
            print('Error, ingrese un numero entero')


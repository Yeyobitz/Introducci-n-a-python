"""
En el código principal, mientras pulsemos s a seguir (validar s y n), nos debe pedir un código de 
producto, su precio y la cantidad de días que han pasado desde su fabricación (validarlos como 
mayores a 0 el precio y cantidad de días, además controlarles ValueError) 

luego: 
Llamar a una función que reciba el código y el precio, y muestre el precio con IVA. 

Luego, llamar a otra función enviándole el código y la cantidad de días que han pasado desde su 
fabricación. Esta función, que tiene internamente una cantidad correspondiente a los días de 
vencimiento, debe retornar la diferencia entre la cantidad de días de vencimiento y la cantidad de 
días que han pasado desde su fabricación. Si la diferencia es mayor o igual a cero escribir Aún no 
vence, en caso contrario escribir Vencido. 
"""

def precio_iva(codigo, precio):
    print('El precio con IVA del producto ', codigo, ' es: ', precio*1.21)

def dias_vencimiento(codigo, dias):
    vencimiento = 30
    if dias < vencimiento:
        print('El producto ', codigo, ' aun no vence')
    else:
        print('El producto ', codigo, ' vencio')

seguir = 's'
while seguir == 's':
    while True:
        try:
            codigo = int(input('Ingrese el codigo del producto: '))
            precio = int(input('Ingrese el precio del producto: '))
            while precio <= 0:
                precio = int(input('Error, ingrese el precio del producto: '))
            dias = int(input('Ingrese la cantidad de dias desde su fabricacion: '))
            while dias <= 0:
                dias = int(input('Error, ingrese la cantidad de dias desde su fabricacion: '))
            precio_iva(codigo, precio)
            dias_vencimiento(codigo, dias)
            seguir = input('Desea seguir? s/n: ')
            while seguir != 's' and seguir != 'n':
                seguir = input('Error, desea seguir? s/n: ')
        except ValueError:
            print('Error, ingrese un numero entero')


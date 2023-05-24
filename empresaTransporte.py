#### iniciando variables
pesoPaquete = -1
cont = 0
pesoTotal = 0
#### entrada de datos
while pesoPaquete !=0:
    pesoPaquete=float(input('Ingrese peso paquete '+str(cont+1)+' = '))
    cont+=1
    pesoTotal+=pesoPaquete
else:
    print('No hay mas paquetes')

#### mostrar el precio total
print('Pesos en total:', pesoTotal, 'Kg')

#### mostrar el promedio
cont-=1 # no cuenta el 0 de salida
if cont == 0:
    print('No hay paquetes')
    promedio = 0
else:
    promedio = pesoTotal/cont
    print('Promedio de peso de paquetes:', promedio, 'Kg')

#### mostrar si el promedio es bajo, medio, alto o muy alto
if promedio < 10:
    print('Bajo peso')
elif promedio < 15:
    print('Peso medio')
elif promedio < 20:
    print('Peso alto')
else:
    print('Peso muy alto')



from time import time

"""
inicio = time()

num1 = int(input('Ingrese un numero entre 1 y 9: '))
while True:
    num2 = num1 * 3
    num1 = int(input('Ingrese el numero anterior multiplicado por 3: '))
    if num1 != num2:
        print('ñoñoño')
        break
    elif num1 > 100:
        fin = time()
        print('Tiempo de ejecucion: ', round(fin-inicio), 'segundos')
        break
    """
from random import randint
acierto = 0
#inicializar num con un valor aleatorio
num = randint(1,9)
inicio = time()
while True:
    num1=int(input('Ingrese el doble de '+str(num)+' más 6 ='))
    num2= num * 2 + 6
    num=num2+round(time()-inicio) #Esta suma crece según el tiempo
    if num2 != num1:
        print("ñoñoño")
        break
    else:
        acierto += 1
        print('Aciertos: ', acierto)
        if acierto == 4:
            fin = time()
            print('Tiempo de ejecucion: ', round(fin-inicio), 'segundos')
            break
from random import *
intento=0

while True:
    aleatorio=randint(1,10)
    numero=int(input("Ingrese un número entre 1 y 10: "))
    while numero<1 or numero>10:
        numero=int(input("Error. Ingrese un número entre 1 y 10: "))
    intento+=1 #intento=intento+1
    if numero==aleatorio:
        print("Felicitaciones, adivinaste en", intento, "intentos")
        break
    else:
        print("No-ohhh, intenta nuevamente")
        if numero<aleatorio:
            print("El número ingresado es menor al número a adivinar")
        else:
            print("El número ingresado es mayor al número a adivinar")




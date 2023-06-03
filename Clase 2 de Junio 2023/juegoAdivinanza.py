from random import * #importamos todo de random
intento=0 #inicializamos la variable intento en 0
aleatorio=randint(1,10) #generamos un numero aleatorio entre 1 y 10

while True: #iteramos hasta que se adivine el número
    numero=int(input("Ingrese un número entre 1 y 10: ")) #pedimos un número entre 1 y 10
    while numero<1 or numero>10: #mientras el número no esté entre 1 y 10
        numero=int(input("Error. Ingrese un número entre 1 y 10: ")) #pedimos nuevamente el número
    intento+=1  #sumamos 1 a intento
    if numero==aleatorio: #si el número es igual al aleatorio
        print("Felicitaciones, adivinaste en", intento, "intentos")  #imprimimos el mensaje
        break 
    else:
        print("No-ohhh, intenta nuevamente") #si no, imprimimos el mensaje
        if numero<aleatorio:
            print("El número ingresado es menor al número a adivinar") #si el número es menor al aleatorio
        else:
            print("El número ingresado es mayor al número a adivinar") #si el número es mayor al aleatorio




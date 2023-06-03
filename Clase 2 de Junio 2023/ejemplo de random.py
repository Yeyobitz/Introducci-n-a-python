from random import * #importamos todo de random

cant=int(input("Cantidad de personas: ")) #pedimos la cantidad de personas
for i in range(cant): #iteramos desde 0 hasta cant-1
    edad=randint(1,110) #generamos un numero aleatorio entre 1 y 110
    print("Edad " + str(i+1)+ "=", edad) #imprimimos la edad de la persona i+1
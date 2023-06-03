from random import *

cant=int(input("Cantidad de personas: "))
for i in range(cant):
    edad=randint(1,110)
    print("Edad " + str(i+1)+ "=", edad)
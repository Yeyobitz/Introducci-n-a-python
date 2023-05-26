"""
Para completar la planilla de pago en una empresa, se desea calcular el total de pago en horas a los obreros, 
para lo cual se sabe que la hora de trabajo vale $4500. 
Se debe ingresar la cantidad de obreros (validar como mayor a cero).
Por cada obrero, ingresar el nombre (validar distinto a vacío, distinto a comillas vacías) y la cantidad de horas trabajadas 
de cada uno (validar como mayor a cero). 

Finalmente, mostrar el total de pago en horas trabajadas al total de obreros. 

"""

totalHoras = 0
i = 0

obreros = int(input("Ingrese la cantidad de obreros: "))
while obreros <= 0:
    obreros = int(input("Error, ingrese una cantidad válida de obreros: "))

while i < obreros:
    
    nombre = input("Ingrese el nombre del obrero: ")
    while nombre == "" or nombre == " ":
        nombre = input("Error, ingrese un nombre válido: ")
        
    horas = int(input("Ingrese la cantidad de horas trabajadas del obrero: "))
    while horas <= 0:
        horas = int(input("Error, ingrese una cantidad válida de horas trabajadas: "))
        
    totalHoras += horas
    i += 1

totalPagar = totalHoras * 4500
print("El total a pagar es de $" + str(totalPagar))


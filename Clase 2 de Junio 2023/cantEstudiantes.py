from random import *
cantEstudiantes=randint(1,30)
totalNotas=0
for i in range(cantEstudiantes):
    nota=uniform(1,7)
    print("Nota del estudiante", i+1, "=", round(nota,2))
    totalNotas+=nota
promedio=totalNotas/cantEstudiantes
print("Promedio del curso:", round(promedio,2))

suma=0
cont=0
while True:
    monto=randint(1,1000)
    if monto!=0:
        suma+=monto
        cont+=1
    else:
        break
if cont>0:
    print("Promedio de los montos ingresados:", round(suma/cont,1))
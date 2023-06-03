from random import * #importamos todo de random
cantEstudiantes=randint(1,30) #generamos un numero aleatorio entre 1 y 30
totalNotas=0 #inicializamos la variable totalNotas en 0
for i in range(cantEstudiantes): #iteramos desde 0 hasta cantEstudiantes-1
    nota=uniform(1,7) #generamos un numero aleatorio entre 1 y 7
    print("Nota del estudiante", i+1, "=", round(nota,2)) #imprimimos la nota del estudiante i+1
    totalNotas+=nota #sumamos la nota del estudiante i+1 a totalNotas
promedio=totalNotas/cantEstudiantes #calculamos el promedio
print("Promedio del curso:", round(promedio,2)) #imprimimos el promedio


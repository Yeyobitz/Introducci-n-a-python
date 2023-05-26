"""
Se necesita leer primero la cantidad total de estudiantes de un colegio y luego la cantidad de estudiantes que pasaron de curso.
(La cantidad total de estudiantes validarla como mayor a 0, y la cantidad de estudiantes que pasaron validarla como mayor o
 igual a 0 y menor o igual a la cantidad total de estudiantes)
Calcular el porcentaje de estudiantes que pasaron, que se obtiene dividiendo los estudiantes que pasaron por los estudiantes
 totales, multiplicado por 100.
Finalmente, es necesario mostrar un mensaje según la siguiente condición: si el porcentaje es mayor a 80, mostrará RENDIMIENTO
 NORMAL, sino mostrará RENDIMIENTO BAJO.  
"""

# Empezar el loop para preguntar si quiere ingresar otro número
respuesta = "si"
while respuesta == "si":
    
# Ingreso de datos
    estudiantes = int(input("Ingrese la cantidad total de estudiantes: "))
    while estudiantes <= 0:
        estudiantes = int(input("Error, ingrese una cantidad válida de estudiantes: "))

    aprobados = int(input("Ingrese la cantidad de estudiantes aprobados: "))
    while aprobados < 0 and aprobados > estudiantes:
        aprobados = int(input("Error, ingrese una cantidad válida de estudiantes aprobados: "))

    # Cálculo de porcentaje
    porcentaje = (aprobados / estudiantes) * 100

    # Mostrar mensaje
    if porcentaje > 80:
        print("RENDIMIENTO NORMAL")
    else:
        print("RENDIMIENTO BAJO")

    # Preguntar si quiere ingresar otro número
    respuesta = input("¿Desea ingresar otro número? (si/no): ") 
    while respuesta != "si" and respuesta != "no":
        respuesta = input("Error, ingrese una respuesta válida (si/no): ")


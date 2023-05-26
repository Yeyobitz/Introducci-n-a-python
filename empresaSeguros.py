"""
Una empresa de seguros desea calcular cuánto dinero obtendrá un vendedor por concepto de las ventas que realiza en el mes.
Leer el sueldo base de un vendedor (validar como mayor a 0). 
Mientras responda s para seguir: 

Leer un tipo de seguro que vende (validar el tipo de seguro permitiendo sólo las letras a, b o c)
La comisión se calcula de la siguiente manera: 

Si el tipo de seguro que vende es a, la comisión será 4.3% del sueldo base.
Si el tipo de seguro que vende es b, la comisión será 5.2% del sueldo base.
Si el tipo de seguro que vende es c, la comisión será 8.7% del sueldo base. 

Finalmente, mostrar el total que recibirá en el mes tomando en cuenta su sueldo base más sus comisiones. 

"""
# Inicializar variables
comision = 0
seguir = "s"
totalSueldo = 0

# Ingreso de datos
sueldoBase = int(input("Ingrese el sueldo base del vendedor: "))
while sueldoBase <= 0:
    sueldoBase = int(input("Error, ingrese un sueldo base válido: "))

respuesta = input("¿Desea ingresar un seguro? (s/n): ").lower()
while respuesta != "s" and respuesta != "n":
    respuesta = input("Error, ingrese una respuesta válida (s/n): ").lower()

# Loop
while seguir == "s":
    tipoSeguro = input("Ingrese el tipo de seguro que vende (a/b/c): ").lower()
    while tipoSeguro != "a" and tipoSeguro != "b" and tipoSeguro != "c":
        tipoSeguro = input("Error, ingrese un tipo de seguro válido (a/b/c): ")

    if tipoSeguro == "a":
        comision += sueldoBase * 0.043
    elif tipoSeguro == "b":
        comision += sueldoBase * 0.052
    else:
        comision += sueldoBase * 0.087

    seguir = input("¿Desea ingresar otro seguro? (s/n): ").lower()
    while seguir != "s" and seguir != "n":
        seguir = input("Error, ingrese una respuesta válida (s/n): ").lower()

totalSueldo = sueldoBase + comision
print("El total a pagar es de $" + str(totalSueldo))


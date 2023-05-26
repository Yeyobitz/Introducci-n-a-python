"""
Una tienda ofrece los siguientes descuentos por el monto de compra de los clientes, mientras responda s para seguir: 
Leer un monto inicial de compra (validar como mayor a 0).
Calcular el monto final de la compra, de la sgte. manera: 

-Si el monto inicial es menor a $100.000, descuento de 0%
-Si el monto inicial es mayor o igual a $100.000 y menor a $500.000, descuento de 5%.
-Si el monto inicial es mayor o igual a $500.000, descuento de 20%. 

Finalmente, mostrar la suma de los montos finales, que ingresa a la tienda.  

"""

# Inicializar variables
montoFinal = 0
seguir = "s"
totalCompra = 0

# Ingreso de datos
while seguir == "s":
    montoInicial = int(input("Ingrese el monto inicial de compra: "))
    while montoInicial <= 0:
        montoInicial = int(input("Error, ingrese el monto inicial de compra: "))

    if montoInicial < 100000:
        montoFinal = montoInicial
    elif montoInicial >= 100000 and montoInicial < 500000:
        montoFinal = montoInicial * 0.95
    else:
        montoFinal = montoInicial * 0.8

    totalCompra += montoFinal

    seguir = input("¿Desea ingresar otra compra? (s/n): ").lower()
    while seguir != "s" and seguir != "n":
        seguir = input("Error, ingrese una respuesta válida (s/n): ").lower()

print("El total a pagar es de $" + str(totalCompra))





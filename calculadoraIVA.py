"""
Mientras responda s para seguir: 
Se lee el precio de un artículo (validar entre 10000 y 300000).
Al precio agregarle el IVA
Si el precio resultante es mayor a 200000
- restarle 10000,
- mostrar el precio final resultante y
- escribir el mensaje “Precio Alto”,
en caso contrario,
- restarle 5000,
- mostrar el precio final resultante y
- escribir “Precio Normal”
"""
# Inicializar variables
precioFinal = 0
seguir = "s"

# Ingreso de datos
while seguir == "s":
    precio = int(input("Ingrese el precio del artículo: "))
    while precio < 10000 or precio > 300000:
        precio = int(input("Error, ingrese un precio válido: "))

    precioFinal = precio * 1.19

    if precioFinal > 200000:
        precioFinal -= 10000
        print("Precio Alto")
    else:
        precioFinal -= 5000
        print("Precio Normal")

    print("El precio final es de $" + str(precioFinal))

    seguir = input("¿Desea ingresar otro precio? (s/n): ").lower()
    while seguir != "s" and seguir != "n":
        seguir = input("Error, ingrese una respuesta válida (s/n): ").lower()

print("The End of Program: You can (NOT) calculate the IVA")
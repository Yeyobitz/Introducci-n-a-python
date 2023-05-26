"""
Leer el stock de los productos notebook, impresoras y smartphone (validar como mayor a 0). 
Mientras se responda s a seguir: 

Leer, como string, el código de producto (validar distinta vacío, distinto a comillas vacías) 

Leer un pedido de este producto (validar como mayor a 0) 

Si el pedido es menor o igual al stock de ese producto, rebajar el stock de ese producto, sino avisar que no hay stock suficiente de ese producto. 

Al finalizar, entregar el stock de cada producto. 
"""
seguir = "s"

stockNotebook = int(input("Ingrese el stock de notebooks: "))
while stockNotebook <= 0:
    stockNotebook = int(input("Error, ingrese un stock válido de notebooks: "))

stockImpresoras = int(input("Ingrese el stock de impresoras: "))
while stockImpresoras <= 0:
    stockImpresoras = int(input("Error, ingrese un stock válido de impresoras: "))
    
stockSmartphone = int(input("Ingrese el stock de smartphones: "))
while stockSmartphone <= 0:
    stockSmartphone = int(input("Error, ingrese un stock válido de smartphones: "))

while seguir == "s":
    codigo = input("Ingrese el código del producto: ")
    while codigo == "" or codigo == " ":
        codigo = input("Error, ingrese un código válido: ")
    
    pedido = int(input("Ingrese el pedido de este producto: "))
    while pedido <= 0:
        pedido = int(input("Error, ingrese un pedido válido: "))

    if codigo == "notebook":
        if pedido <= stockNotebook:
            stockNotebook -= pedido
        else:
            print("No hay stock suficiente de notebooks")
    elif codigo == "impresora":
        if pedido <= stockImpresoras:
            stockImpresoras -= pedido
        else:
            print("No hay stock suficiente de impresoras")
    elif codigo == "smartphone":
        if pedido <= stockSmartphone:
            stockSmartphone -= pedido
        else:
            print("No hay stock suficiente de smartphones")
            
    else:
        print("Código de producto inválido")

    seguir = input("¿Desea ingresar otro pedido? (s/n): ").lower()
    while seguir != "s" and seguir != "n":
        seguir = input("Error, ingrese una respuesta válida (s/n): ").lower()

print("El stock de notebooks es de " + str(stockNotebook))
print("El stock de impresoras es de " + str(stockImpresoras))
print("El stock de smartphones es de " + str(stockSmartphone))



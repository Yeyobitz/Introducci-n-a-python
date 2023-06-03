# find y rfind
# Busca un substring en el string, y entrega su posición inicial

# find: Busca desde la izquierda
# rfind: Busca desde la derecha
# Ambos métodos reciben como parámetro el substring a buscar
# Ambos métodos retornan la posición inicial del substring
# Si el substring no se encuentra, retorna -1
# Ejemplo:
texto=input('Ingrese un texto: ').lower() #convertimos el texto a minusculas
busca=input('Qué busca? ') #pedimos el substring a buscar
encuentra=texto.find(busca) #buscamos el substring
if encuentra>=0: #si se encontró
    print('Se encontró en la posición',encuentra) #imprimimos la posición
else:
    print('No tá') #si no se encontró, imprimimos que no tá

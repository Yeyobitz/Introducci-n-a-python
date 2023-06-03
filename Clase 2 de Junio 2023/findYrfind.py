# find y rfind
# Busca un substring en el string, y entrega su posición inicial

# find: Busca desde la izquierda
# rfind: Busca desde la derecha
# Ambos métodos reciben como parámetro el substring a buscar
# Ambos métodos retornan la posición inicial del substring
# Si el substring no se encuentra, retorna -1
# Ejemplo:
texto=input('Ingrese un texto: ').lower()
busca=input('Qué busca? ')
encuentra=texto.find(busca)
if encuentra>=0:
    print('Se encontró en la posición',encuentra)
else:
    print('No tá')

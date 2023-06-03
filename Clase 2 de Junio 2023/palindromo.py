texto=input('Ingrese un texto: ').lower() # Se solicita el texto
if texto==texto[::-1]: # Se compara el texto con su inverso
    print('El texto ingresado es un palíndromo')
else:
    print('El texto ingresado no es un palíndromo')
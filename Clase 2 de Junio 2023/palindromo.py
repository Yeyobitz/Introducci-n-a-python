texto=input('Ingrese un texto: ').lower() # Se solicita el texto
if texto==texto[::-1]: # Se compara el texto con su inverso
    print('El texto ingresado es un palíndromo') # Si son iguales, es palíndromo
else:
    print('El texto ingresado no es un palíndromo') # Si no son iguales, no es palíndromo
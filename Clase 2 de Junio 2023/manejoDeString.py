codigo=input('ingrese código (largo 8)=')
while len(codigo)!=8:
    print('Error. El código debe tener 8 caracteres')
    codigo=input('ingrese código (largo 8)=')
print('Código ingresado:', codigo)
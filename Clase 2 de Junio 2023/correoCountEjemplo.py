correo=input('Ingrese su correo: ')
if correo.count('@')==1 and correo.count('.')>=1:
    print('El correo es válido')
else:
    print('El correo no es válido')

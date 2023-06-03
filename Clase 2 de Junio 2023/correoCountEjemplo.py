correo=input('Ingrese su correo: ') #pedimos el correo
if correo.count('@')==1 and correo.count('.')>=1: #si hay un @ y al menos un .
    print('El correo es válido') #el correo es válido
else:
    print('El correo no es válido') #el correo no es válido

codigo=input('ingrese código (largo 8)=') #pedimos el código
while len(codigo)!=8: #mientras el largo del código no sea 8
    print('Error. El código debe tener 8 caracteres') #imprimimos el mensaje
    codigo=input('ingrese código (largo 8)=') #pedimos nuevamente el código
print('Código ingresado:', codigo) #imprimimos el código
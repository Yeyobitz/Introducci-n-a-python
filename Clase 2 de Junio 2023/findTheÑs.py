texto=input('Ingrese un texto: ').lower()
while True:
    if texto.find('ñ')>=0:
        texto=texto.replace('ñ','nh')
        print(texto)
    else:
        break
texto=input('Ingrese un texto: ').lower() #convertimos el texto a minusculas
while True: #iteramos hasta que no haya mas ñ
    if texto.find('ñ')>=0: #si hay ñ
        texto=texto.replace('ñ','nh') #reemplazamos la ñ por nh
        print(texto) #imprimimos el texto
    else:
        break #si no hay mas ñ, salimos del ciclo
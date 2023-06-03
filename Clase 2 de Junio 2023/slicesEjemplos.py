texto='SUPERCALIFRAGILISTICOESPIALIDOSO'
#recibe=texto[0:8] #rebana desde el primer caracter hasta el 7°
#recibe=texto[2:14:2] #rebana desde el índice 2 hasta el caracterer 13 e irá de 2 en 2
#recibe=texto[:11] #imprime desde el 0 hasta el 10
#recibe=texto[7:] #tomará del indice 7 hasta el final 
recibe=texto[::-1] #imprime el texto al revés
print(recibe) #imprimimos el texto
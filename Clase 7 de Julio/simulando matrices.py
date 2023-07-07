# USAR LISTAS ANIDADAS PARA SIMULAR MATRICES
"""
En python podemos usar listas anidadas para simular matrices
Una matriz es una estructura de datos que tiene filas y columnas
"""
juego=[]
etapa=[]
filas=3 #Las filas van para abajo y las columnas para al lado
columnas=5 #filas y columnas de la matriz, esta será 3x5
for i in range(filas):
    etapa.clear() #Limpiamos la lista para que no se repitan los valores
    for j in range(columnas):
        print('Ingrese puntaje[',i,',',j,end=']: ')
        puntaje=int(input())
        etapa.append(puntaje)
    juego.append(etapa[:]) #agrega una fila a la matriz, el [:] es para que agregue del inicio al fin
print(juego)

#recorre y muestra matriz
for i in range(filas):
    for j in range(columnas):
        print('\t',juego[i][j],end=' ')
    print('\n')

print(juego[2][1]) #Muestra el elemento de la fila 3, columna 2
juego[2][1]=100 #Modifica el elemento de la fila 3, columna 2
print(juego[2][1]) #Muestra el elemento de la fila 3, columna 2
juego[2][1]=juego[2][1]*1.05 #Aumenta el elemento de la fila 3, columna 2 en 5%
print(juego[2][1]) #Muestra el elemento de la fila 3, columna 2

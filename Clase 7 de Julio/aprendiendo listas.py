"""
Las listas se aproximan a lo que, en otros lenguajes de programación, les llaman
ARREGLOS (array en inglés)
Los arreglos pueden ser, principalmente, de dos tipos:
    - Estáticos: Tienen un tamaño fijo, que se define al momento de crearlos
    - Dinámicos: No tienen un tamaño fijo, se pueden agregar o quitar elementos
    en cualquier momento

"""

#Ejemplos de declaraciones de listas
lista1 = [] #Lista vacía
lista2 = list() #Lista vacía
lista3 = [3] #Lista con un elemento
Lista4 = [23,['Python', True], 'Hola'] #Lista con varios elementos y una lista anidada

"""
Recorrido de una lista (similar a lo visto con tuplas)
Usando un ciclo iterativo for in, es posible recorrer una lista
PERO VEREMOS DOS FUNCIONES DE TEXTO NUEVAS:
"""
cont1=0;cont2=0
codigos=['C4','A23','B2','F53','B111']
for valor in codigos:
    if valor.startswith('B'): #startswith() devuelve True si el texto empieza con el texto indicado
        cont1+=1
    if valor.endswith('2'): #endswith() devuelve True si el texto termina con el texto indicado
        cont2+=1

print(f"La cantidad de códigos que empiezan con B es {cont1}")
print(f"La cantidad de códigos que terminan con 2 es {cont2}")

"""
INVERTIR UNA LISTA
Es posible cambiar la listea, dej+andpla al revés, usando la función reverse()
"""
print(codigos)
codigos.reverse()
print(codigos)

"""
ORDENAR UNA LISTA
Hay dos maneras:
1) Mostrar ordenada la lista con la función sorted()
2) Ordenar la lista con el método sort()
"""
precios=[2400,9800,12000,3500,2100,3400]
print(sorted(precios)) #sorted() devuelve una lista ordenada, pero no modifica la lista original
print(precios) #La lista original no se modifica
precios.sort() #sort() ordena la lista original
print(precios) #La lista original se modifica


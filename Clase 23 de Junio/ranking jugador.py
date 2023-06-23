"""
En el código principal, mientras pulsemos s a seguir (validar s y n), nos debe pedir el nombre, puntaje y 
la cantidad de vidas de un jugador (validarlos como mayores a 0 el puntaje y la cantidad de vidas, también 
controlarles ValueError) 

Luego: 

Llamar a una función que reciba el puntaje y la cantidad de vidas y retorne el ranking final, el cual se 
calcula con el puntaje y dividiéndolo por la cantidad de vidas. 

Luego, llamar a otra función enviándole el ranking y el nombre, y que adentro pregunte si el ranking es 
mayor a 300, si es así escribe <el nombre>“tiene buen ranking” sino escribe <el nombre>“tiene ranking 
principiante” 
"""

def ranking_final(puntaje, vidas):
    return puntaje / vidas

def ranking_jugador(ranking, nombre):
    if ranking > 300:
        print(nombre, ' tiene buen ranking')
    else:
        print(nombre, ' tiene ranking principiante')

seguir = 's'
while seguir == 's':
    try:
        nombre = input('Ingrese el nombre del jugador: ')
        puntaje = int(input('Ingrese el puntaje del jugador: '))
        while puntaje <= 0:
            puntaje = int(input('Error, ingrese el puntaje del jugador: '))
        vidas = int(input('Ingrese la cantidad de vidas del jugador: '))
        while vidas <= 0:
            vidas = int(input('Error, ingrese la cantidad de vidas del jugador: '))
        ranking = ranking_final(puntaje, vidas)
        ranking_jugador(ranking, nombre)
        seguir = input('Desea seguir? s/n: ')
        while seguir != 's' and seguir != 'n':
            seguir = input('Error, desea seguir? s/n: ')
    except ValueError:
        print('Error, ingrese un numero entero')
        
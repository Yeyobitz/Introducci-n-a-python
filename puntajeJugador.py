seguir = 's'
total = 0
i=0
while seguir == 's':
    puntaje = int(input('Ingrese puntaje '+str(i+1)+'='))
    while puntaje < 0 or puntaje > 100:
        puntaje = int(input('Error, ingrese puntaje '+str(i+1)+'='))
    i+=1
    total+=puntaje
    seguir = input('Desea seguir? (s/n)').lower()
    while seguir != 's' and seguir != 'n':
        seguir = input('Error, desea seguir? (s/n)').lower()
    

print('Total de puntajes:', total)

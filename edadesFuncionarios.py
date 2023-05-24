seguir = 's'
total = 0
i=0
while seguir == 's':
    edad = float(input('Ingrese edad '+str(i+1)+'= '))
    while edad < 18  or edad > 65:
        edad = float(input('Error, ingrese edad '+str(i+1)+'= '))
    i+=1
    total+=edad
    seguir = input('Desea seguir? (s/n)').lower()
    while seguir != 's' and seguir != 'n':
        seguir = input('Error, desea seguir? (s/n)').lower()
    
promedio = total/i
print('Promedio de edades:', round(promedio, 1))
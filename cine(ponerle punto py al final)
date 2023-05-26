valorEntrada = 0

menoresHombres = 0
menoresMujeres = 0
valorMenoresHombres = 0
valorMenoresMujeres = 0

mayoresHombres = 0
mayoresMujeres = 0
valorMayoresHombres = 0
valorMayoresMujeres = 0

adultosMayoresHombres = 0
adultosMayoresMujeres = 0
valorAdultosMayoresHombres = 0
valorAdultosMayoresMujeres = 0

hombres = 0
mujeres = 0
sexo = ''
seguir = 's'
totalHombres = 0
totalMujeres = 0

while seguir == 's':

    #En el acceso a un cine, leer de los asistentes la edad (validad entre 1 y 110) y su sexo (validar con M o F)
    edad= int(input('Ingrese edad:'))
    if edad < 1 or edad > 110:
        edad = int(input('Error, ingrese edad:'))
    #SEEEEEEEEEEEXOOO
    sexo = input('Ingrese su sexo (m/f):').lower()
    if sexo != 'm' and sexo != 'f':
        sexo = input('Error, ingrese su sexo (m/f):').lower()
    if sexo == 'm':
        hombres += 1
        if edad < 18:
            valorEntrada = 2000
            menoresHombres += 1
            valorMenoresHombres += valorEntrada
            print('Menor de edad, valor entrada:' + str(valorEntrada))

        elif edad > 18 and edad < 60:
            valorEntrada = 5000
            mayoresHombres += 1
            valorMayoresHombres += valorEntrada
            print('Mayor de edad, valor entrada:' + str(valorEntrada))
        elif edad >= 60:
            valorEntrada = 4000
            adultosMayoresHombres += 1
            valorAdultosMayoresHombres += valorEntrada
            print('Adulto mayor, valor entrada:' + str(valorEntrada))

    else:
        mujeres += 1
        if edad < 18:
            valorEntrada = 2000
            menoresMujeres += 1
            valorMenoresMujeres += valorEntrada
            print('Menor de edad, valor entrada:' + str(valorEntrada))
        elif edad > 18 and edad < 60:
            valorEntrada = 5000
            mayoresMujeres += 1
            valorMayoresMujeres += valorEntrada
            print('Mayor de edad, valor entrada:' + str(valorEntrada))
        elif edad >= 60:
            valorEntrada = 4000
            adultosMayoresMujeres += 1
            valorAdultosMayoresMujeres += valorEntrada
            print('Adulto mayor, valor entrada:' + str(valorEntrada))

    seguir = input('Desea seguir? (s/n)').lower()
    while seguir != 's' and seguir != 'n':
        seguir = input('Error, desea seguir? (s/n)').lower()


#Al finalizar de leer todos los asistentes, entregar las siguientes estadisticas:

#Por sexo, cantidad de menores de edad, mayores de edad y adultos mayores
print('Cantidad de hombres:' + str(hombres))
print('Cantidad de mujeres:' + str(mujeres))

#Por sexo, total en pago hecho por menores de edad, mayores de edad y adultos mayores
print('Total pago hombres:' + str(totalHombres),"\n"
      "Total pago hombres menores:",valorMenoresHombres,"\n"
      "Total pago hombres mayores:",valorMayoresHombres,"\n"
      "Total pago hombres adultos mayores:",valorAdultosMayoresHombres,"\n")
print('Total pago mujeres:' + str(totalMujeres),"\n"
      "Total pago mujeres menores:",valorMenoresMujeres,"\n"
      "Total pago mujeres mayores:",valorMayoresMujeres,"\n"
      "Total pago mujeres adultos mayores:",valorAdultosMayoresMujeres,"\n")

#Total en pago por todo
print('Total pago:' + str(totalHombres + totalMujeres))

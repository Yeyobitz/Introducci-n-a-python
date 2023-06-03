from random import * # * importa todo lo de random

cant=int(input("Cantidad de contenedores embarcados="))
print('\tContainer\tPeso total(kg):')
for i in range(cant):
    peso=uniform(2300,32000) #uniform(a,b) devuelve un número flotante entre a y b
    print('\t\t'+str(i+1)+'\t', round(peso,2)) #round(x,n) redondea x a n decimales
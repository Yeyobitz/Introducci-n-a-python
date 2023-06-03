# replace
# reemplaza un substring del string

texto='Utilisando pithon' #definimos el string
print(texto) #imprimimos el string
texto=texto.replace('pithon','python') #reemplazamos pithon por python
print(texto)
texto=texto.replace('s','z') #reemplazamos s por z
print(texto)
texto=texto.replace('o','i',1) #reemplazamos la primera o por i
print(texto)
texto=texto.replace('i','o',2) #reemplazamos las primeras dos i por o
print(texto)
texto=texto.replace('o','i',-1) #reemplazamos la ultima o por i
print(texto)
texto=texto.replace('o','i',-2) #reemplazamos las ultimas dos o por i
print(texto)
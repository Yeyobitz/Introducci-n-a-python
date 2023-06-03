#strip, rstrip y lstrio
# elimina espacios del string

# strip: elimina espacios al inicio y al final
# rstrip: elimina espacios al final
# lstrip: elimina espacios al inicio

# Ejemplo:
texto1='   Hola q tal   '
inicio='->'
fin='<-'
print(inicio+texto1+fin)
texto1strip=texto1.strip()
print(inicio+texto1strip+fin)
texto1lstrip=texto1.lstrip()
print(inicio+texto1lstrip+fin)
texto1rstrip=texto1.rstrip()
print(inicio+texto1rstrip+fin)
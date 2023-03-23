import re

# chequear si el string termina con mundo
hola = "hola mundo"
patron = re.compile("[ndo]+$")
patron2 = re.compile("^[hol]+")
print(patron.search(hola))
print(patron2.match(hola))

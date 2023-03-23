import re

patron = re.compile("[aei]+uto")
lista = ["auto", "uto", "aeiuto", "eiuto", "iuto"]
for x in lista:
    print(patron.match(x))

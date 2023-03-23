# r sirve para bloquear las secuencias de escape, en este caso imprime "\d"
print(r"\d")
import re

patron = re.compile(r"(?i:pera) y manzana")
string1 = "pera y manzana"
string2 = "PERA y manzana"
string3 = "Pera y manzana"
string4 = "PERA Y manzana"
print(patron.search(string1))
print(patron.match(string2))
print(patron.match(string3))
print(patron.match(string4))

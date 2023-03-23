import re

l = ["papa", "pera", "manzana", "limon", "durazno", "naranja"]
p = re.compile("manzana" "|limon" "|naranja")
for x in l:
    print(p.search(x))

import re

l = ["a.bu.la..", "f.e.", "ac"]

patron = re.compile("[\.]+")
for x in l:
    print(patron.findall(x))

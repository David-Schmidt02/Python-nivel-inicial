import re

p = re.compile("[aeiou]{3,}")
l = ["aiu", "aaaaa", "xoai"]
for x in l:
    print(p.search(x))

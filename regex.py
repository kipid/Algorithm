# https://www.youtube.com/watch?v=wnuBwl2ekmo
# Regular Expressions in Python

import re

pattern = re.compile("^[A-Z]+$")

print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))

match = pattern.search("HELLOWORLD")
print(match)
print(match.group(0))
# print(match.group(1))
print()

matches = pattern.finditer("HELLOWORLD")

for m in matches:
	print(m)

findall = pattern.findall("HELLOWORLD")
print(findall)

pattern1 = re.compile("[^\\w]+")
findall = pattern1.findall("This: is a pencil.")
print(findall)
str = "This: is a pencil."
strReplaced = re.sub(r"[^\w]+", "", str).lower()
print(strReplaced)
print(strReplaced[::-1])
# https://www.youtube.com/watch?v=wnuBwl2ekmo
# Regular Expressions in Python

import re

pattern = re.compile("^[A-Z]+$")

print(pattern.search("Hello World"))
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))

match = pattern.search("HELLOWORLD")
print(match) # <re.Match object; span=(0, 10), match='HELLOWORLD'>
print(match.group(0)) # HELLOWORLD
# print(match.group(1))
print()

matches = pattern.finditer("HELLOWORLD")
print(matches) # <callable_iterator object at 0x000001CBF4327E20>
print()

for m in matches:
	print(m) # <re.Match object; span=(0, 10), match='HELLOWORLD'>
print()

findall = pattern.findall("HELLOWORLD")
print(findall) # ['HELLOWORLD']

pattern1 = re.compile("[^\\w]+")
findall = pattern1.findall("This: is a pencil.")
print(findall) # [': ', ' ', ' ', '.']
str = "This: is a pencil."
strReplaced = re.sub(r"[^\w]+", "", str).lower()
print(strReplaced) # thisisapencil
print(strReplaced[::-1]) # licnepasisiht

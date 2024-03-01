# Regular Expressions in Python

import re

pattern = re.compile("^[A-Z]+$")

print(pattern.search("Hello World")) # None
print(pattern.search("HELLO WORLD")) # None
print(pattern.search("HELLOWORLD")) # <re.Match object; span=(0, 10), match='HELLOWORLD'>
print("HELLO WORLD".find("WO")) # 6
print("HELLO WORLD".find("WOD")) # -1
print("HELLO WORLD".index("WO")) # 6
# print("HELLO WORLD".index("WOD")) # ValueError: substring not found

match = pattern.search("HELLOWORLD")
print(match) # <re.Match object; span=(0, 10), match='HELLOWORLD'>
print(match.group(0)) # HELLOWORLD
# print(match.group(1)) # IndexError: no such group
print()

pattern = re.compile("[A-Z]{3}")
matches = pattern.finditer("HELLOWORLD")
print(matches) # <callable_iterator object at 0x000001CBF4327E20>
print()

for m in matches:
	print(m)
"""
<re.Match object; span=(0, 3), match='HEL'>
<re.Match object; span=(3, 6), match='LOW'>
<re.Match object; span=(6, 9), match='ORL'>
"""
print()

findall = pattern.findall("HELLOWORLD")
print(findall) # ['HEL', 'LOW', 'ORL']

pattern1 = re.compile("[^\\w]+")
findall = pattern1.findall("This: is a pencil.")
print(findall) # [': ', ' ', ' ', '.']
str = "This: is a pencil_."
strReplaced = re.sub(r"[^\w]+", "", str).lower() # \w = [a-zA-Z0-9_]
print(strReplaced) # thisisapencil_
print(strReplaced[::-1]) # _licnepasisiht

print()
p = "a***"
p = re.sub(r"\*+", "*", p)
print(p) # a*
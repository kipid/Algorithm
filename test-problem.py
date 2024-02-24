import re

p = "a***"
p = re.sub(r"\*+", "*", p)
print(p)
import imports as code

# __name__: imports

#Determine how the script wa run using "__name__"
print(f"test __name__: {__name__}")
print(f"test __file__: {__file__}")

a = 10
b = 4

a, b = b, a
print(f"{a = }, {b = }")

if 10 == 10 == 10:
	print("True")
else:
	print("False")

n=5
# pin = [False for _ in range(n+2)]
pin = [False] * (n+2)
pin[-1] = pin[n] = True
print(f"{pin = }")
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"{len(alphabet) = }") # 26

import re

print(f'{re.split(r"[7-9]", "092938423749873298743909871934819204791238998") = }')

s = "092938423749873298743909871934819204791238998"
for ind, num in enumerate(s[1:],2):
	print(f"{ind = }, {num = }")

str_x = "Hello, World!"
for index, char in enumerate(str_x, 5):
    print(f"Index {index}: {char}")

print(f"{list(str_x).pop() = }")
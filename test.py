import imports as code

# __name__: imports

#Determine how the script wa run using "__name__"
print(f"test __name__: {__name__}")
print(f"test __file__: {__file__}")

a = 10
b = 4

a, b = b, a
print(f"{a = }, {b = }")

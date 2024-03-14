# with open("Lorem ipsum.txt") as lorem_file:
# 	items = lorem_file.read().split()
# 	print(items)

str = "Hello Hello replace test Hello"
print(f"{str.split(" ") = }")
print(str.replace("Hello", "Halo")) # replace All.

l = ['Bryan', 'Cat', 28]
s = set(l)
print(s)
print()

s.add("Hello")
print(s)
print()

s.discard("Bryan")
print(s)
print()

print(s.discard(1)) # Do not throw error!, even though it does not exist.
print(s)
print()

print(s.remove(28)) # Throw Error! if it does not exist.
print(s)
print()

s.update([1,2,3,4,4,5,6,7])
print(s)
print()

print(s.pop())
print(s)
print()

print(s.discard(7)) # return None, even though it exists.
print(s)
print()

print(l)
print(l.pop())
print(l)
print()

print("Bryan" in l)
print(l.remove("Bryan")) # return None, even though it exists.
print(l)
print()

# with open("Lorem ipsum.txt") as lorem_file:
# 	items = lorem_file.read().split()
# 	print(items)

str = "Hello Hello replace test Hello"
print(str.replace("Hello", "Halo")) # replace All.

l = ['Bryan', 'Cat', 28]
s = set(l)
print(s)

s.add("Hello")
print(s)

s.discard("Bryan")
print(s)

s.discard(1)
print(s)

s.remove(28) # Throw Error! if not exists.
print(s)

s.update([1,2,3,4,4,5,6,7])

print(s.pop())
print(s)

print(l)
print(l.pop())
print(l)

print("Bryan" in l)
print(l.remove("Bryan"))
print(l)

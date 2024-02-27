#Map
#Looping without a loop
#Maps function calls to a collection of items
#map(func, iterables)

#Basic usage - Count len
people = ["Matt", "Bryan", "Tammy", "Markus"]

#Old way
counts = []
for x in people:
	counts.append(len(x))
print(f"Old way: {counts}")

#Modern way
print(f"Mapped: {list(map(len, people))}")



#More complex - Combine elements
#Notice different lens, we are also passing multiple args

firstnames = ("Apple", "Chocolate", "Fudge", "Pizza")
lastnames = ("Pie", "Cake", "Brownies")

def merg(a,b):
	return a + " " + b

x = map(merg, firstnames, lastnames)
print(x) # <map object at 0x0000021820A87820>
print(list(x)) # ['Apple Pie', 'Chocolate Cake', 'Fudge Brownies']
print()



#Multiple functions - Combine functions
#Call multiple functions in one map call

def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def multiply(a,b):
	return a * b

def divide(a,b):
	return a / b

def doAll(func, nums):
	return func(nums[0], nums[1])

f = (add, subtract, multiply, divide)
v = [[5,3],[4,2]]
n = list(v[0:1]) * len(f) + list(v[1:2]) * len(f)
print(f"f:{f}, n:{n}")
print()

fAll = f * len(v)
print(f"fAll:{fAll}")
print()

m = map(doAll, f, n)
print(list(m))
print()

m = map(doAll, fAll, n)
print(list(m))
print()

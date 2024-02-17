#Packing and unpacking data

#Problem with  *arg and **kwarg is we can not use lists and dictionaries
#Instead we have to pack and unpack data

#Packing data
def pack(*nums):
	print(f'Packed: {nums}')
	for x in nums:
		print(f'nums: {x}')

pack(1,2,3)
print()
pack([1,2,3])
print()
pack([1,2,3], [4,5,6])
print()
pack(*[1,2,3])
print()



#Unpacking data
def unpack(a, b, c):
	print(f'Unpack: {a}, {b}, {c}')

unpack(1,2,3)
print()
unpack(*[1,2,3])
print()
unpack(*(1,2,3))
print()



#Dictionary issue
d = dict(name="kipid", age=40, pet="ChuChu")

pack(d)
print()
pack(*d) # Only keys are passed.
print()
print()
# unpack(d) # Error
unpack(*d) # Only keys are passed.



#Packing dictionary
def packdict(**nums):
	print(f'nums: {nums}')
	for k in nums:
		print(f'Key {k}: {nums[k]}')

packdict(name="kipid", age=40, pet="ChuChu")
# packdict(d) # Error: TypeError: packdict() takes 0 positional arguments but 1 was given
print()
packdict(**d)
print()
for k in d:
	print(f'Key {k}: {d[k]}')
print()
print("d.keys()")
for k in d.keys():
	print(f'Key {k}: {d[k]}')
print()



#Unpacking dictionary
def unpackdict(name, age, pet):
	print('Unpacking a dictionary!')
	print(f'name: {name}, age: {age}, pet: {pet}')

unpackdict(name="kipid", age=40, pet="ChuChu")
print()
unpackdict(age=40, name="kipid", pet="ChuChu")
# unpackdict(age=40, name="kipid", "ChuChu") # Error!
print()
unpackdict("shaun", pet="Dog", age=20)
# unpackdict("shaun", pet="Dog", age=20, name="kipid") # Error!
print()
# unpackdict("shaun", pet="Dog", name="kipid") # Error!: TypeError: unpackdict() got multiple values for argument 'name'
print()
unpackdict(**d)
print()



#Function in an argument
def test(name, age, pet):
	print(f'name: {name}, age: {age}, pet: {pet}')

def getData():
	# return { name: "Bryan", age:39, ...} # Error: Key must be String.
	return { "name": "Bryan", "age": 39, "pet": "Cat" }

test(**getData())
print()



#Function as an argument
def funky(data):
	d = data()
	print(d)

funky(getData)

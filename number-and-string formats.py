# https://www.youtube.com/watch?v=EoNOWVYKyo0

n: int = 1_000_000_000.123_456_789
print(n) # 1000000000.1234568
print(f"{n:_}") # 1_000_000_000.1234568
print(f"{n:,}") # 1,000,000,000.1234568
print(f"{n = :_}") # n = 1_000_000_000.1234568
print(f"{n = :,}") # n = 1,000,000,000.1234568
print()

n: int = 1e9
print(n) # 1000000000.0
print()

var: str = "var"
print(f"{var:>20}:") #                  var:
print(f"{var:<20}:") # var                 :
print(f"{var:20}:")  # var                 :
print(f"{var:^20}:") #         var         :
print(f"{var:_>20}:") # _________________var:
print(f"{var:#<20}:") # var#################:
print(f"{var:|^20}:") # ||||||||var|||||||||:
print()

from datetime import datetime

now: datetime = datetime.now()
print(f"{now:%d.%m.%y (%H:%M:%S)}") # 05.03.24 (13:01:15)
print(f"{now:%Y-%m-%d %H:%M:%S}") # 2024-03-05 13:01:15
print(f"{now:%c}") # Tue Mar  5 13:01:15 2024
print(f"{now:%I%p}") # 01PM
print()

n: float = 1234.56789012
print(n) # 1234.56789012
print(round(n, 2)) # 1234.57
print(f"Result: {n:.2f}") # Result: 1234.57
print(f"Result: {n:.0f}") # Result: 1235
print(f"Result: {n:,.4f}") # Result: 1,234.5679
print()

a: int = 5
b: int = 10
my_var: str = "Hi, Bob!"
print(f"a + b = {a + b}") # a + b = 15
print(f"{a + b = }") # a + b = 15
print(f"{bool(a) = }") # bool(a) = True
print(f"{my_var = }") # my_var = 'Hi, Bob!'
print(f"my_var = {my_var}") # my_var = Hi, Bob!
print()



# https://www.youtube.com/watch?v=E620yiMMtns
for x in "hello":
	print(f"{x} = {ord(x)}")
"""
h = 104
e = 101
l = 108
l = 108
o = 111
"""
print()

first = "Bryan" # Double qoute
last = 'Cairns' # Single qoute
print(first + " " + last) # Bryan Cairns
print(f"Hello my name is {first} {last}.") # Hello my name is Bryan Cairns.
print()

hers = "Heather's"
print(hers)
print()

s1 = chr(72) # H
s2 = chr(105) # i
print(s1 + s2) # Hi
print(chr(8710)) # Way beyond ascii! ∆

#Escape characters - start with a slash \
print(f"Hello{chr(13) + chr(10)}World!")
print(f"Hello\r\nWorld")
"""
Hello

World!
"""
print(f"Hello\nWorld")
"""
Hello
World
"""
print(f"Hello\tWorld") # Hello	World

qoute = "Then he said \"hello\" to me."
print(qoute) # Then he said "hello" to me.

#Must format strings to avoid errors
name = "Bryan"
age = 46
# print(name + " " + age) # TypeError: can only concatenate str (not "int") to str
print(f"My name is {name}. I am {age} years old.") # My name is Bryan. I am 46 years old.
print("My name is %s. I am %i years old." % (name, age)) # My name is Bryan. I am 46 years old.
# print("My name is %i. I am %s years old." % (name, age)) # TypeError: %i format: a real number is required, not str



# https://www.youtube.com/watch?v=IN98lMOORWg
#Basic String Operations
str = "Hello World, this is a string!"
print(len(str)) # Get the length: 30
print(str * 3) # Repeat: Hello World, this is a string!Hello World, this is a string!Hello World, this is a string!
str = "Hello World, this is a string! Hello again."
print(str.replace("Hello", "Hola")) # Replace all: Hola World, this is a string! Hola again.
print(str.split(",")) # Split: ['Hello World', ' this is a string! Hello again.']
print(str.startswith("He")) # Starts with: True
print(str.endswith("n.")) # Ends with: True
print(str.upper()) # HELLO WORLD, THIS IS A STRING! HELLO AGAIN.
print(str.lower()) # hello world, this is a string! hello again.
print(str.capitalize()) # Hello world, this is a string! hello again.
print()

str = "hello. hello. hello."
print(str.capitalize()) # Hello. hello. hello.
print()

#Slicing - or getting a sub string
print(str[0:5]) # hello
print(str[6:]) #  hello. hello.
print(str[-7:]) #  hello.
print(str[6:11]) #  hell
print()

str = "Hello World, this is a string! Hello again."
print(str.find("t")) # 13
print(str.find("T")) # -1
print(str.index("t")) # 13
# print(str.index("T")) # ValueError: substring not found
print()

i = str.find(",")
print(str[:i]) # Hello World
print(str[:str.find("!")]) # Hello World, this is a string
print()



# https://www.youtube.com/watch?v=5Llv-SzbnXM
# https://docs.python.org/3/library/sys.html
import sys
print(sys.int_info) # sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)
print(sys.float_info) # sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
print(sys.hash_info) # sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash13', hash_bits=64, seed_bits=128, cutoff=0)

cVal = 3 + 6j
print(f"{cVal = }") # cVal = (3+6j)
cVal = complex(5,3)
print(f"{cVal = }") # cVal = (5+3j)
print(f"real = {cVal.real}, imag = {cVal.imag}") # real = 5.0, imag = 3.0
print()

#Basic operations
x = 3
y = x + 3 # add
print(f"add = {y}") # 6

y = x - 1 # subtract
print(f"subtract = {y}") # 2

y = x * 4.157 # multiply
print(f"multiply = {y}") # 12.471

y = x / 0.5 # divide
print(f"divide = {y}") # 6.0

y = x ** 2 # pow
print(f"pow = {y}") # 9

y = x % 2.5 # remain
print(f"remain = {y}") # 0.5

y = x // 2.5 # quotient
print(f"quotient = {y}") # 1.0

y = x // 2 # quotient
print(f"quotient = {y}") # 1

y = x % 2 # remain
print(f"remain = {y}") # 1


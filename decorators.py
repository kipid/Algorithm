#Decorators

#Everything in Python is an object
#That means functions can be used as objects
#So we can do some really cool things
#A decorator takes in a function, adds some functionality and returns it.

#Basic decorator
#In this example we will change the execution order

def test_decorator(func):
	print("Before")
	func()
	print("After")

@test_decorator
def do_stuff():
	print("Doing stuff.")
"""
Before
Doing stuff.
After
"""

# test_decorator(do_stuff) # TypeError: 'NoneType' object is not callable



#Real decorator
#In this example, we will change the functionality
#@makeBold is equal to
#f = @makeBold(printName)
#f()
def makeBold(func):
	def inner():
		print("<b>")
		func()
		print("</b>")
	return inner # Return the inner function

@makeBold
def printName():
	print("Bryan Cairns")

printName() # = inner()
"""
<b>
Bryan Cairns
</b>
"""



#Decorator with params
#Notice this has a defined number of params

def numcheck(func):
	def checkInt(o):
		if isinstance(o, int):
			if o == 0:
				print("Can not divide by zero")
				return False
			return True
		print(f"{o} is not a number")
		return False

	def inner(x, y):
		if not checkInt(x) or not checkInt(y):
			return
		return func(x,y)
	return inner

@numcheck
def divide(a, b):
	print(a / b)

divide(100, 3)
# 33.333333333333336

divide(100, 0) # ZeroDivisionError: division by zero
# Can not divide by zero

divide(100, "cat") # TypeError: unsupported operand type(s) for /: 'int' and 'str'
# cat is not a number



#Decorator with unknown number of params
#We want a decorator that can pass params and handle anything
#We also want to chain them together
#*args, **kwargs to the rescue

def outline(func):
	def inner(*args, **kwargs):
		print("~"*20)
		func(*args, **kwargs)
		print("~"*20)
	return inner

def list_items(func):
	def inner(*args, **kwargs):
		func(*args, **kwargs)
		print(f"args = {args}")
		print(f"kwargs = {kwargs}")
		for x in args:
			print(f"arg={x}")
		for k,v in kwargs.items():
			print(f"key={k}, value={v}")
	return inner

@outline
@list_items
def display(msg):
	print(msg)

display("Hello world!")
"""
~~~~~~~~~~~~~~~~~~~~
Hello world!
args = ('Hello world!',)
kwargs = {}
arg=Hello world!
~~~~~~~~~~~~~~~~~~~~
"""
print()

display(msg="Hello kipid!")
"""
~~~~~~~~~~~~~~~~~~~~
Hello kipid!
args = ()
kwargs = {'msg': 'Hello kipid!'}
key=msg, value=Hello kipid!
~~~~~~~~~~~~~~~~~~~~
"""
print()



@outline
@list_items
def birthday(name="", age=0):
	print(f"Happy birthday {name} you are {age} years old.")

birthday(name="Bryan", age=36)
"""
~~~~~~~~~~~~~~~~~~~~
Happy birthday Bryan you are 36 years old.
args = ()
kwargs = {'name': 'Bryan', 'age': 36}
key=name, value=Bryan
key=age, value=36
~~~~~~~~~~~~~~~~~~~~
"""
print()

birthday("Kipid", age=40)
"""
~~~~~~~~~~~~~~~~~~~~
Happy birthday Kipid you are 40 years old.
args = ('Kipid',)
kwargs = {'age': 40}
arg=Kipid
key=age, value=40
~~~~~~~~~~~~~~~~~~~~
"""
print()

#Imports

#Lets make our code usable to other scripts
#This allows us to structure our code and simplify things
#We are really just scratching the surface of the import system

#Create the file
#Go ahead and look at mycode.py

#import as
import mycode as person

#Scope issues
global name # Can't shove it into the global scope but we should not
# print(name) # Not in the same scope

print(person.name) # Each file can and should use its own scope
person.greet()
person.toFile("import test.txt")
# person.toFile()

person.name = "Tammy"
person.greet()

person.fromFile("import test.txt")
person.greet()



#Main function

#How do you run your code automatically?

#Determine how the script wa run using "__name__"
print(f"__name__: {__name__}") # __main__
print(f"__file__: {__file__}") # C:\Algorithm\imports.py

#Create some code
def test():
	print("This is a test function.")

def main():
	print("This is the main function.")
	test()

#Run automatically
if __name__ == "__main__":
	main()

#Now run it from a different script - See test.py



#Import maddness

#__init__
#What is it? Why do we need it?

#Make a sub folder

#Imports
print()
import sub.test as code
code.doTest()

from sub import *
from sub import test as code

doTest() # This is ok. But not recommended.
test.doTest()
code.doTest()
print()

#Call the code
def main():
	print("This is the main function.")
	doTest() # This is ok. But not recommended.
	code.doTest()

if __name__ == "__main__":
	main()
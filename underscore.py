#The underscore
#Often ignored, multiple uses
#_Single
#__Double
#__Before
#After__
#__Both__

#Skipping
for _ in range(5):
	print("Hello")

#Test class
from person import *

#Before (Single)
#Internal use only, called a weak private
p = Person()
p.setName("Bryan")
print(f"Weak private: {p._name}")
p._name = "N0000000"
print(f"Weak private: {p._name}")

#Before (Double) #
#Internal use only, avoid conflict in subclass
#and tells python to rewrite the name (Mangling)
p = Person()
p.work()
# p.__think() # AttributeError: 'Person' object has no attribute '__think'

c = Child()
# c.testDouble() # AttributeError: 'Child' object has no attribute '_Child__think'

#After (Any)
#Helps to avoid naming conflicts with key words
class_ = Person()
print(class_)

#Before and After
#Considered special to Python, like the init and main function
p = Person()
p.__call__() # Works


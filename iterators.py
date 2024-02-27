#Iterators

t = (1,2,3,4)
for x in t:
	print(x)



#Iter Basics
#Lists, tuples, dictionaries, and sets are all iterable objects.
#They are iterable containers which you can get an iterator from.
people = ["Bryan", "Tammy", "Rango"]
i = iter(people)
print(i) # <list_iterator object at 0x000001F205C46590>
print(next(i)) # Bryan
print(next(i)) # Tammy
print(next(i)) # Rango
# print(next(i)) # StopIteration



#Iterable class
import random
class Lotto:
	def __init__(self):
		self._max = 5

	def __iter__(self):
		#The yield statement suspends function's execution
		#and sends a value back to the caller, but retains enough
		#state to enable function to resume where it is left off
		for _ in range(self._max):
			yield random.randrange(0,100)

	def setMax(self, value):
		self._max = value

print("-"*20)
lotto = Lotto()
lotto.setMax(10)

for x in lotto:
	print(x)

print("-"*20)

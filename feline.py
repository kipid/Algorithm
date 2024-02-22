#Class inheritance

#Feline class : Feline means "고양이과의 동물".
class Feline:
	def __init__(self, name):
		self.name = name
		print("Creating a feline.")

	def setName(self, name):
		print(f"{self} setting name: {name}")
		self.name = name

	def meow(self):
		print(f"{self.name} meow!")

	def sleep(self):
		print(f"{self.name} zzz...")

	def hungry(self):
		for x in range(5):
			self.meow()

	def eat(self):
		print(f"{self.name} nom nom nom")

#Tiger class
class Tiger(Feline):
	#Overriding a constructor is BAD idea.
	def __init__(self):
		#Super allows is to access the parent
		#if we forget this we will have a bad time later
		super().__init__("No name")
		print("Creating a tiger.")

	def stalk(self):
		#have to make sure name is set in the parent
		#this is considered -LBYL (Look Before You Leap)
		#here we are dynamically adding the attribute

		#If we did not init the super we will ave to be careful
		#If not hasattr(self,'name'): super().setName('No name')
		print(f"{self.name}: stalking")

	def rename(self,name):
		super().setName(name)

#Lion class
class Lion(Feline):
	def roar(self):
		print(f"{self.name} roar!")

c = Feline("kitty")
print(c)
c.meow()
c.setName("Chuchu")

l = Lion("Leo")
print(l)
l.meow()
l.roar()
print()

t = Tiger() #is a Feline, but with a different constructor
print(t)
t.stalk()
t.rename("Tony")
t.meow()
t.stalk()


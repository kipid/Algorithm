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



#Lion class
class Lion(Feline):
	def roar(self):
		print(f"{self.name} roar!")

c = Feline("kitty")
print(c)
c.meow()

l = Lion("Leo")
print(l)
l.meow()
l.roar()

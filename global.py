#Global

x = 1
def test():
	x = 6
	print(f'Local x: {x}')

test()
print(f'Global x: {x}')



#Global variable
count = 0

def counter(max):
	global count
	count += max
	print(f'count: {count}')

counter(10)
counter(1)

for x in range(5):
	counter(100) # With or Without is ok.
	print(f'count: {count}')


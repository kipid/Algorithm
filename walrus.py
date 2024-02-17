#Walrus operator and global

#Common issues ( )
# y := len('hello') # SyntaxError: invalid syntax
(y := len('hello'))
print(y)

if n := len("Cat") <= 3: print(n)
if (n := len("Cat")) <= 3: print(n)
# if (n = len("Cat")) <= 3: print(n) # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?



#Simple example
lines = []

def canAdd(max = 5):
	global lines
	if allowed := (count := len(lines)) < max:
		print(f'You can add {max - count} more.')
	return allowed

while canAdd():
	lines.append(l := input("Enter a line: "))

print(f'You entered: {lines}')

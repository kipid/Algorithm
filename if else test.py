if []: # False
	print("True")
else:
	print("False")

if [[]]: # True
	print("True")
else:
	print("False")

if not []: # True
	print("True")
else:
	print("False")

if "": # False
	print("True")
else:
	print("False")

if {}: # False
	print("True")
else:
	print("False")

if (): # False
	print("True")
else:
	print("False")

tuple_ = ()

if tuple_: # False
	print("True")
else:
	print("False")

if set(): # False
	print("True")
else:
	print("False")

if list(): # False
	print("True")
else:
	print("False")

if 0: # False
	print("True")
else:
	print("False")

if 1: # True
	print("True")
else:
	print("False")

if "0": # True
	print("True")
else:
	print("False")

if "1": # True
	print("True")
else:
	print("False")

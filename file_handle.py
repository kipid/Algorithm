import os, sys

print(f"File: {__file__}") # Built in file name
# File: C:\Algorithm\file_handle.py

print(f"Args: {sys.argv}")
# Args: ['C:\\Algorithm\\file_handle.py']

sfile = os.path.abspath(sys.argv[0])
print(f"Reading: {sfile}")
# Reading: C:\Algorithm\file_handle.py

#Exists
# sfile = "nope.txt"
if not os.path.exists(sfile):
	print("File not found!")
	# FileNotFoundError
	exit(1)


#Open the file
f = open(sfile, "r")

#Read a line
line = f.readline()
print(line)

#Read number of letters
chars = f.read(10)
print(f"Chars: *{chars}*")

#Position
print(f"Position: {f.tell()} of {os.stat(sfile).st_size}")

#Seek - move to a position in the file
#Zero based
f.seek(0)

#Read all lines
print("-"*30)
for l in f.readlines():
	print(l.rstrip())

#Close the file
#Allows other applications to work with it
f.close()



#Write a text file
#Simplify mode usage
def toFile(filename, mode, data):
	f = open(filename, mode)
	for i in range(5):
		f.write(str(i) + ":" + data + "\n")
	# f.flush() # Automatically called when file is closed.
	f.close()

#Write will overwrite the entire file
def writeFile(filename):
	toFile(filename, "w", "Hello World!")

#Append will add to the end of the file
def appendFile(filename):
	toFile(filename, "a", "Hello World!")

#Read the file
def readFile(filename):
	if not os.path.exists(filename):
		print("File not found")
		return
	f = open(filename, "r")
	for line in f.readlines():
		print(line.rstrip())
	# print(f.read())
	f.close()

#See it in action
myfile = "hello.txt"
writeFile(myfile)
appendFile(myfile)
readFile(myfile)



#Working with binary files
import random
import operator

#Create random bytes
def randomBytes(size):
	bytes = []
	for x in range(size):
		bytes.append(random.randrange(0,256))
	return bytes

def displayBytes(bytes):
	print("."*20)
	for index, item in enumerate(bytes,start=1):
		print(f"{index} = {item} ({hex(item)})")
		if item == 255:
			print("="*20)
			print(f"{index} = {item} ({hex(item)})")
			print("="*20)
	print("."*20)

b = randomBytes(16)
displayBytes(b)

print()
print(f"{0xff}")
print()



#Write bytes
def writeBytes(filename, bytes):
	with open(filename, "wb") as file:
		for i in bytes:
			file.write(i.to_bytes(1, byteorder="big"))

#Read bytes
def readBytes(filename):
	bytes = []
	with open(filename, "rb") as file:
		while True:
			b = file.read(1)
			if not b:
				break;
			bytes.append(int.from_bytes(b, byteorder="big"))
	return bytes

#See it in action
outbytes = randomBytes(16)
displayBytes(outbytes)

filename = "test.txt"
writeBytes(filename, outbytes)

inbytes = readBytes(filename)
displayBytes(inbytes)
print()

print(f"Match: {operator.eq(outbytes, inbytes)}")



#JSON files
#App to app communications

"""
{
	name: "kipid"
	, age: 46
	, pet: "ChuChu"
}
"""
import json
filename = "json.txt"

#To string
outD = dict(name="kipid", age=40, pet="ChuChu")
s = json.dumps(outD) # Dumps puts it to a string
print(f"String={s}")

#To file
with open(filename, "w") as f:
	json.dump(outD, f) # Dump puts it to a file

#From string
inD = json.loads(s) # Load the dictionary from the string
print(f"Dict={inD}")

#From file
with open(filename, "r") as f:
	fD = json.load(f)

print(f"Type: {type(fD)} = {fD}")

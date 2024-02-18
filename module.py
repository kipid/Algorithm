import os

d = os.getcwd() # Current Working Directory
print(d)

#Change directory
os.chdir("..")
print(os.getcwd())

os.chdir(d)
print(os.getcwd())



#List directory
print(os.listdir())

for f in os.listdir():
	print(f"Full Path: {os.path.abspath(f)}")
	if os.path.isdir(f): print(f"Dir: {f}")
	if os.path.isfile(f): print(f"File: {f}")
	if os.path.islink(f): print(f"Link: {f}")
	print()



#Scan directory
for e in os.scandir():
	print(e)
	print(f"e.name: {e.name}")
	print(f"e.path: {e.path}")
	if e.is_dir(): print(f"Dir: {e.name}")
	if e.is_file(): print(f"File: {e.name}")
	if e.is_symlink(): print(f"Link: {e.name}")
	print()



#Glob - recursive scan
import glob

for filename in glob.glob(pathname = d + "**/**", recursive = True):
	print(f"glob: {filename}")

print()

for currentpath, folders, files in os.walk('.'):
	for file in files:
		print(f"walk: {file},\nos.path.join: {os.path.join(currentpath, file)}")

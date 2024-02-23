dict_ = {"a":0, "b":1, "c":2, "d":3}
del dict_["a"]
print(dict_)
print(True if "b" in dict_ else False)
print(True if "a" in dict_ else False)

s = "abcdefghijklmnopqrstuvwxyz"
for r, let in enumerate(s):
	print(f"r: {r}, let: {let}")

print()
seen = dict()
print(seen)
for r, let in enumerate(s):
	seen[let] = r
print(seen)
print(seen.get("c", -1))
print(seen.get("!", -2)) # default value -2

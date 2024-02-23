dict_ = {"a":0, "b":1, "c":2, "d":3}
del dict_["a"]
print(dict_)
print(True if "b" in dict_ else False)
print(True if "a" in dict_ else False)

s = "abcdefghijklmnopqrstuvwxyz"
for r, let in enumerate(s):
	print(f"r: {r}, let: {let}")

s = set()
print(f"{s.add('1')}") # None
s.add("1")
s.add("1")
s.add("1")
s.add("1")
# s.add("3","2") # TypeError: set.add() takes exactly one argument (2 given)
print(s)
s.add("2")
s.add("3")
s.remove("1")
s.discard("1")
print(s)
print(len(s))
print(s.pop())
s = set(("1", "2", "4", "7"))
print(s)
s = set(["1", "2", "4", "7"])
print(s)
s = set("123456789")
print(s)
print(f"{list(s)[0]}")
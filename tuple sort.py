li = {(3,0,0), (3,2,0), (0,1,1), (0,0,1), (1,1,0), (2,9,5)}
print(li)
# li.sort()
# print(li)
li1 = set(li)
for item in li1:
	li.add(item + (1,) * 3)
print(li)

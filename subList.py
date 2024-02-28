list = [0,1,2,3,4,5,6,7,8,9]
print(list[1:]) # [1,2,3,4,5,6,7,8,9]
print(list[:3]) # [0,1,2]
print(list[:-3]) # [0,1,2,3,4,5,6]
print(list[-3:]) # [7,8,9]
print(list[3:5]) # [3,4]
print(list[3:5:-1]) # []
print(list[5:3:-1]) # [5,4]
print(list[3::-1]) # [3,2,1,0]
print(list[3:-1:-1]) # []
print(range(3,-1,-1)) # range(3,-1,-1)
for i in range(3,-1,-1):
	print(f"i: {i}") # 3,2,1,0
print()
print(list[3:0:-1]) # [3,2,1]
print(list[:3:-1]) # [9,8,7,6,5,4]
print(list[:-3:-1]) # [9,8]
print(list[-3::-1]) # [7,6,5,4,3,2,1,0]
print(list[::-1]) # [9,8,7,6,5,4,3,2,1,0]

l = [8,5,2,7,2,1,6,8,8,9,3,4,5]
l.sort()
print(l)
l = l * 2
print(l)

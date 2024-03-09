li = [0,1,2,3,4,5,6,7,8,9]
print(li) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[:]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(li[1:]) # [1,2,3,4,5,6,7,8,9]
print(li[:3]) # [0,1,2]
print(li[:-3]) # [0,1,2,3,4,5,6]
print(li[-3:]) # [7,8,9]
print(li[3:5]) # [3,4]
print(li[3:5:-1]) # []
print(li[5:3:-1]) # [5,4]
print(li[3::-1]) # [3,2,1,0]
print(li[3:-1:-1]) # []
print(range(3,-1,-1)) # range(3,-1,-1)
for i in range(3,-1,-1):
	print(f"i: {i}") # 3,2,1,0
print()
print(li[3:0:-1]) # [3,2,1]
print(li[:3:-1]) # [9,8,7,6,5,4]
print(li[:-3:-1]) # [9,8]
print(li[-3::-1]) # [7,6,5,4,3,2,1,0]
print(li[::-1]) # [9,8,7,6,5,4,3,2,1,0]
print()
print(f"li: {li}")
print()

l = [8,5,2,7,2,1,6,8,8,9,3,4,5]
sortedL = sorted(l, reverse=True)
print(f"sortedL: {sortedL}")
l.sort()
print(l)
l.remove(8)
print(l)
l = l * 2
print(l)
l = [1,3,2]
r = [1,3,2]
print(l == r)
for i in range(len(l)-1, -1, -1):
	if l[i]==2:
		break
print(i)

nums = [2,3,1]
print(f"nums: {nums}")
p = 0
nums = nums[:p+1] + sorted(nums[p+1:])
print(f"nums: {nums}")
print(f"sorted(nums): {sorted(nums)}")
print(f"nums.sort(): {nums.sort()}")
print(f"nums: {nums}")

str_ = "zckdiqoazkd"
print(sorted(str_))
print("".join(sorted(str_)))

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastNum = nums[0]
        k = 1
        for num in nums[1:]:
            if lastNum != num:
                nums[k] = num
                k += 1
                lastNum = num
        return k
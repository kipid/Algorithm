class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums) - 1
        i = 0
        while i < len(nums):
            if (nums[i] == val):
                nums[i] = nums[k]
                nums[k] = "_"
                k -= 1
                i -= 1
            if (k == i):
                return k + 1
            i += 1
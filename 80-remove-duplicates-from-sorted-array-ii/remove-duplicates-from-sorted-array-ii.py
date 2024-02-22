class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 2
        for num in nums[2:]:
            if nums[k-2] != nums[k-1]:
                nums[k] = num
                k += 1
            elif nums[k-1] != num:
                nums[k] = num
                k += 1
        return k


        
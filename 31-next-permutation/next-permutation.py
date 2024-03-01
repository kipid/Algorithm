class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
    def reverse(self, nums: List[int], start: int) -> None:
        i = start
        j = len(nums) - 1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        p = i - 1
        if p == -1:
            self.reverse(nums, 0)
            return
        i = len(nums) - 1
        while i > 0:
            if nums[p] < nums[i]:
                break
            i -= 1
        self.swap(nums, p, i)
        self.reverse(nums, p+1)
        return

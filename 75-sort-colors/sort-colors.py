class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsCount = { 0:0, 1:0, 2:0 }
        for num in nums:
            numsCount[num] += 1
        nums.clear()
        for i in range(3):
            nums += [i] * numsCount[i]

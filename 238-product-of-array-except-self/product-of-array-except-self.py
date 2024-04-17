class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        left = 1
        for i in range(len(nums)-1):
            res[i] = left
            left *= nums[i]
        res[-1] = left
        right = 1
        for i in range(len(nums)-1, 0, -1):
            res[i] *= right
            right *= nums[i]
        res[0] = right

        return res 
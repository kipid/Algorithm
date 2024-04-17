class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        totalProduct = 1
        num0Count = 0
        for num in nums:
            if num == 0:
                num0Count += 1
            else:
                totalProduct *= num
        if num0Count == 1:
            for k in range(len(nums)):
                if nums[k] == 0:
                    ans[k] = totalProduct
        elif num0Count == 0:
            for k in range(len(nums)):
                ans[k] = totalProduct // nums[k]
        return ans
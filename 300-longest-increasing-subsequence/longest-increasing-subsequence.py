class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        
        # n = len(nums)
        # dp = [1] * n

        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)

        monostack = []
        for num in nums: 
            if not monostack or monostack[-1] < num:
                monostack.append(num)
            else:
                idx = bisect.bisect_left(monostack, num)
                monostack[idx] = num
        return len(monostack)
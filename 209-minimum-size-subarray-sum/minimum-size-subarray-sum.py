class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = math.inf

        l= 0
        curSum = 0
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minlen = min(minlen, r-l+1)
                curSum -= nums[l]
                l+=1
        return minlen if minlen != math.inf else 0
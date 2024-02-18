class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = current_max = 0
        for num in nums:
            current_max += num 
            if current_max < 0:
                current_max = 0
            elif current_max > maximum:
                maximum = current_max
        
        return maximum if maximum > 0 else max(nums)
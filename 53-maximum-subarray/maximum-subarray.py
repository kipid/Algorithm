class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            if curr_sum < 0:
                curr_sum = num
            else:
                curr_sum += num
            max_sum = max(max_sum, curr_sum) # 모든 List[int] 가 minus 일 때도 제대로 동작.
        return max_sum

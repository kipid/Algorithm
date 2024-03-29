class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        best = 0
        for start in nums:
            if start - 1 not in nums:
                end = start + 1
                while end in nums:
                    end += 1
                best = max(best, end - start)
        return best
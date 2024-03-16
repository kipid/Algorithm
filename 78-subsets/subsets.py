class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets_at = [()]
        for i in range(len(nums)):
            subsets_at = [s + (nums[i],) for s in subsets_at] + subsets_at
        return subsets_at
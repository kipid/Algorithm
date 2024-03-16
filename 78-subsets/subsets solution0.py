from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for k in range(len(nums)+1):
            res += combinations(nums, k)
        return res
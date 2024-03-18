class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        nums.sort()

        def backtracking(current: List[int], k: int=0):
            subsets.append(current)

            for i in range(k, len(nums)):
                if i > k and nums[i] == nums[i-1]:
                    continue
                backtracking(current + [nums[i]], i+1)

        backtracking([])
        return subsets
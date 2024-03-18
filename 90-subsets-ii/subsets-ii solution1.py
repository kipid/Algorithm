class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        subsets = []
        nums.sort()

        def backtracking(current: list[int], k: int=0):
            subsets.append(current)
            print(current)
            for i in range(k, len(nums)):
                if i > k and nums[i] == nums[i-1]:
                    continue
                backtracking(current + [nums[i]], i+1)

        backtracking([])
        return subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def addNums(path0: List[int], maxIndex: int):
            res.append(path0)
            for i in range(maxIndex+1, n):
                addNums(path0 + [nums[i]], i)
        
        addNums([], -1)
        return res
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numSet = set()
        for num in nums:
            if num in numSet:
                numSet.remove(num)
            else:
                numSet.add(num)
        for res in numSet:
            return res
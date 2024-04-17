class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numDict = dict();
        for num in nums:
            numDict[num] = numDict.get(num, 0) + 1
        maxCount = len(nums) // 2;
        for num in numDict:
            if numDict[num] > maxCount:
                return num
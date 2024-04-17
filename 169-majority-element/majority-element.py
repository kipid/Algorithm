class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        elem = 0
        for num in nums:
            if count == 0:
                elem = num
            if elem == num:
                count += 1
            else:
                count -= 1
        return elem
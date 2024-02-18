class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lenNums = len(nums)
        if lenNums == 1:
            return nums[0]
        start = 0
        endEnd = lenNums - 1
        atLeastOnePositive = False
        while start < lenNums:
            if nums[start] > 0:
                atLeastOnePositive = True
                break
            start += 1
        if atLeastOnePositive:
            while endEnd >= start:
                if nums[endEnd] > 0:
                    break
                endEnd -= 1
            maxSum = 0
            while start <= endEnd:
                sum = 0
                if nums[start] <= 0:
                    start += 1
                    continue
                end = start
                while end <= endEnd:
                    sum += nums[end]
                    if sum <= 0:
                        start = end
                        break
                    elif sum > maxSum:
                        maxSum = sum
                    end += 1
                if start > 0:
                    while start <= endEnd and nums[start] >= 0 and nums[start - 1] >= 0:
                        start += 1
                start += 1
            return maxSum
        else:
            maxSum = nums[0]
            start = 1
            while start < lenNums:
                if nums[start] > maxSum:
                    maxSum = nums[start]
                start += 1
            return maxSum

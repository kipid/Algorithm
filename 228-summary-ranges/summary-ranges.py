class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = [str(nums[0])]
        i = 0
        while i < len(nums)-1:
            if nums[i+1] - nums[i] != 1:
                if int(res[-1]) != nums[i]:
                    res[-1] += "->" + str(nums[i])
                res.append(str(nums[i+1]))
            i += 1
        if nums[i] - nums[i-1] == 1:
            res[-1] += "->" + str(nums[i])
        return res
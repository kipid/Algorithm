class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        nums = [ (3 * num - target) for num in nums ]
        if nums[0] >= 0:
            return (nums[0] + nums[1] + nums[2]) // 3 + target
        r = len(nums) - 1
        if nums[r] <= 0:
            return (nums[r] + nums[r-1] + nums[r-2]) // 3 + target
        sumMin = nums[0] + nums[1] + nums[r]
        if sumMin == 0:
            return target
        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            while l < r:
                sum_ = num + nums[l] + nums[r]
                if abs(sum_) < abs(sumMin):
                    sumMin = sum_
                    if sumMin == 0:
                        return target
                if sum_ < 0:
                    l += 1
                    sum_ = num + nums[l] + nums[r]
                    while l < r and sum_ <= 0:
                        if abs(sum_) < abs(sumMin):
                            sumMin = sum_
                            if sumMin == 0:
                                return target
                        l += 1
                        sum_ = num + nums[l] + nums[r]
                else:
                    r -= 1
                    sum_ = num + nums[l] + nums[r]
                    while l < r and sum_ >= 0:
                        if abs(sum_) < abs(sumMin):
                            sumMin = sum_
                            if sumMin == 0:
                                return target
                        r -= 1
                        sum_ = num + nums[l] + nums[r]
        return sumMin // 3 + target
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        if len(nums) < 3:
            return res
        set_ = set()
        nums.sort()
        minSum = sum(nums[:4])
        if minSum > target:
            return res
        maxSum = sum(nums[-4:])
        if maxSum < target:
            return res
        for i, num0 in enumerate(nums[:-3]):
            j = i + 1
            while j < len(nums) - 2:
                num1 = nums[j]
                l, r = j+1, len(nums)-1
                while l < r:
                    sum_ = num0 + num1 + nums[l] + nums[r]
                    if sum_ == target:
                        list_ = [num0, num1, nums[l], nums[r]]
                        hash_ = f"{num0};{num1};{nums[l]};{nums[r]}"
                        if hash_ not in set_:
                            set_.add(hash_)
                            res.append(list_)
                    if sum_ < target:
                        l += 1
                    else:
                        r -= 1
                j += 1
        return res

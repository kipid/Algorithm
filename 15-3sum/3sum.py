class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i , a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            
            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                k = a + nums[p1] + nums[p2]
                if k > 0:
                    p2 -= 1
                elif k < 0:
                    p1 += 1
                else:
                    res.append([a,nums[p1],nums[p2]])
                    p1 += 1
                    while nums[p1] == nums[p1-1] and p1 < p2:
                        p1 += 1

        return res
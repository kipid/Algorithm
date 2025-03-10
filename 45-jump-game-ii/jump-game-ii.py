class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        ans = 0
        while r < len(nums) - 1:
            maxJump = 0
            for i in range(l, r+1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            ans += 1
        return ans

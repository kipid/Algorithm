class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def maxJump(left: int, right: int) -> int:
            maxJumpTo = right
            for i in range(left,right+1):
                maxJumpTo = max(maxJumpTo, i+nums[i])
            return maxJumpTo
        left0, right0, n = 0, 0, len(nums)
        while (maxJumpTo := maxJump(left0, right0)) < n-1:
            if maxJumpTo == right0:
                return False
            left0, right0 = right0, maxJumpTo
        return True
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            mid = l + (r - l + 1) // 2
            if mid ** 2 <= x:
                l = mid
            else:
                r = mid - 1
        return l
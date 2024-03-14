class Solution:
    def mySqrt(self, x: int) -> int:
        def findSqrt(left: int, right: int) -> int:
            print(f"{left = }, {right = }")
            if left >= right - 1:
                return right - 1
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                return findSqrt(left, mid)
            else:
                return findSqrt(mid, right)
        if x == 0:
            return 0
        cand = findSqrt(1, x)
        if (cand+1) * (cand+1) <= x:
            return cand+1
        else:
            return cand
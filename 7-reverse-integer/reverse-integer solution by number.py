class Solution:
    def reverse(self, x: int) -> int:
        isMinus = (x < 0)
        if isMinus:
            x = -x
        res = x % 10
        while (x := x // 10) > 0:
            res = 10 * res + x % 10
        if isMinus:
            res = -res
        if -2**31 <= res <= 2**31 - 1:
            return res
        else:
            return 0
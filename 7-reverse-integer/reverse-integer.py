class Solution:
    def reverse(self, x: int) -> int:
        isMinus = (x < 0)
        if isMinus:
            x = -x
        res = int(str(x)[::-1])
        if isMinus:
            res = -res
        if -2**31 <= res <= 2**31 - 1:
            return res
        else:
            return 0
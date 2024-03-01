class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        if dividend == - 2**31 and divisor == -1:
            return 2**31 - 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        i = 0
        while dividend - (divisor << i) >= 0:
            i += 1
        if i > 0:
            q = 1 << (i-1)
            dividend -= divisor << (i-1)
        else:
            return 0
        for k in range(i-2,-1,-1):
            if dividend - (divisor << k) >= 0:
                q += 1 << k
                dividend -= divisor << k
        return sign * q
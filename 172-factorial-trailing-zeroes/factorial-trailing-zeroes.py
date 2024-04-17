class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeroes = 0
        k = 1
        while n >= (fives := 5**k):
            for i in range(fives, n+1, fives):
                zeroes += 1
            k += 1
        return zeroes
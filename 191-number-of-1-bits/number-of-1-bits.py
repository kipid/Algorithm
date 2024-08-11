class Solution:
    def hammingWeight(self, n: int) -> int:
        w = 0
        while (n > 0):
            w += n % 2
            n = n // 2
        return w
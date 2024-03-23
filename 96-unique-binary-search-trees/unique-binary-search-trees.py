class Solution:
    @lru_cache
    def numTrees(self, n: int) -> int:
        if n<=1:
            return 1
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n-1-i)
        return res
memo = {0:1, 1:1}
class Solution:
    def numTrees(self, n: int) -> int:
        if n<=1:
            return 1
        res = 0
        if n in memo:
            return memo[n]
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n-1-i)
        memo[n] = res
        return res
class Solution:
    def climbStairs(self, n: int) -> int:
        # climbStairs(n) = climbStairs(n-1) + climbStairs(n-2)
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        res = [0, 1, 2]
        for i in range(3, n+1):
            res.append(res[i-1] + res[i-2])
        return res[n]
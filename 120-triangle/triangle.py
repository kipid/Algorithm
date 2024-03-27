class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[triangle[0][0]]]
        for d in range(1, len(triangle)):
            dp.append([
                min(dp[d-1][i] if i<len(dp[d-1]) else math.inf, dp[d-1][i-1] if i>0 else math.inf) + v for i,v in enumerate(triangle[d])
            ])
        return min(dp[-1])
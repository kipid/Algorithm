class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [1,1]
        for ith, num in enumerate(s[1:],2):
            ways = 0
            if num != "0":
                ways += dp[ith-1]
            if 10 <= int(s[ith-2] + num) <= 26:
                ways += dp[ith-2]
            dp.append(ways)
        return dp[-1]
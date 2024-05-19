class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # maintaing a dp matrix 
        dp = [[[0 for _ in range(k+1)] for _ in range(2)] for _ in range(n+1)]
        # Traversing the prices inversely and buy can be 0 or 1 if 0 means we can buy and 1 means we cannot
        for i in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if buy == 0:
                        # If we are buying then the capacity remains same as we have not sell it yet 
                        # If we buy we add - to the price as we have invested the money
                        dp[i][buy][cap] = max(0+dp[i+1][0][cap],-prices[i]+dp[i+1][1][cap])
                    elif buy == 1: # Selling 
                        dp[i][buy][cap] = max(0+dp[i+1][1][cap], prices[i]+dp[i+1][0][cap-1])
        return dp[0][0][k]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lastIndex = len(prices)-1
        profit = 0
        i = 0
        while i<lastIndex:
            profit += max(0, prices[i+1]-prices[i])
            i += 1
        return profit
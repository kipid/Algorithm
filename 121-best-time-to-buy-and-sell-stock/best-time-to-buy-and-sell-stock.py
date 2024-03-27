class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max(-min(prices[:i]) + max(prices[i:]))
        minPriceUntil = [prices[0]]
        for i in range(1, len(prices)-1):
            minPriceUntil.append(min(minPriceUntil[-1], prices[i]))
        maxPriceAfter = [prices[-1]]
        profit = 0
        for i in range(len(prices)-2, -1, -1):
            profit = max(profit, -minPriceUntil[i]+maxPriceAfter[-1])
            maxPriceAfter.append(max(maxPriceAfter[-1], prices[i]))
        return profit
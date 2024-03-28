class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lastIndex = len(prices)-1
        if lastIndex==0:
            return 0
        i = 0
        minMaxPrices = []
        while i<lastIndex:
            while i<lastIndex and prices[i] >= prices[i+1]:
                i += 1
            minMaxPrices.append(prices[i])
            while i<lastIndex and prices[i] <= prices[i+1]:
                i += 1
            minMaxPrices.append(prices[i])
        if minMaxPrices[-2]==prices[-1]:
            minMaxPrices.pop()
            minMaxPrices.pop()
        
        def helper(nums: List[int]) -> int:
            min_price = nums[0]
            profit = 0
            for i in range(0, len(nums), 2):
                if nums[i] < min_price:
                    min_price = nums[i]
                if nums[i+1] - min_price > profit:
                    profit = nums[i+1] - min_price
            return profit
        
        print(f"{minMaxPrices = }")
        if len(minMaxPrices)==0:
            return 0
        elif len(minMaxPrices)==2:
            return minMaxPrices[1]-minMaxPrices[0]
        max_profit = 0
        for i in range(2, len(minMaxPrices), 2):
            max_profit = max(max_profit, helper(minMaxPrices[:i])+helper(minMaxPrices[i:]))
        return max_profit
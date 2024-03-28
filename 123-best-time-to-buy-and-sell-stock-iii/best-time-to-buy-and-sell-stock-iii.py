class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to track the profits
        first_buy, second_buy = float('inf'), float('inf')
        first_profit, second_profit = 0, 0

        for price in prices:
            # Update the first buy to the minimum price
            first_buy = min(first_buy, price)
            # Update the first profit to the maximum profit achievable with one transaction
            first_profit = max(first_profit, price - first_buy)
            # Update the second buy to the minimum price after accounting for the first profit
            second_buy = min(second_buy, price - first_profit)
            # Update the second profit to the maximum profit achievable with two transactions
            second_profit = max(second_profit, price - second_buy)

        # The second profit will be the maximum profit achievable with at most two transactions
        return second_profit
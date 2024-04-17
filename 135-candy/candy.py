class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ratings.append(ratings[-1])
        ratings.append(ratings[0])
        candies = [1] * (n + 2)
        for i in range(n):
            if ratings[i-1] < ratings[i]:
                candies[i] = candies[i-1] + 1
        for i in range(n-1, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])
        return sum(candies[:n])
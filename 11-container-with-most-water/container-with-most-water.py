class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxWater = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                newL = l + 1
                while height[newL] <= height[l] and newL < r:
                    newL += 1
                l = newL
            else:
                newR = r - 1
                while height[newR] <= height[r] and l < newR:
                    newR -= 1
                r = newR
            water = min(height[l], height[r]) * (r - l)
            if water > maxWater:
                maxWater = water
        return maxWater
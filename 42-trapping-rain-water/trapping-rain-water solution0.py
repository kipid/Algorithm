class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height)-1
        while left < right and height[left] <= height[left+1]:
            left += 1
        while right > left and height[right] <= height[right-1]:
            right -= 1

        def fillWater(left: int, right: int) -> int: # waterFilled
            if left >= right-1:
                return 0
            l = left
            while l < right and height[l] >= height[l+1]:
                l += 1
            r = l
            while r < right and height[r] <= height[r+1]:
                r += 1
            minHeight = min(height[left], height[r])
            waterFilled = 0
            for i in range(left+1, r):
                if height[i] < minHeight:
                    waterFilled += minHeight - height[i]
                    height[i] = minHeight
            # print(height[left:right+1])
            # print(f"{waterFilled = }, {r = }, {right = }")
            return waterFilled + fillWater(r, right)

        water = fillWater(left, right)
        fullWater = water
        while water > 0:
            water = fillWater(left, right)
            fullWater += water
        return fullWater

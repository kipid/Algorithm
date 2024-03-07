class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        leftwall = 0
        rightwall = 0

        trapped_rain = 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= leftwall:
                    leftwall = height[l]
                else:
                    trapped_rain += (leftwall-height[l])
                l += 1
            else:
                if height[r] >= rightwall:
                    rightwall = height[r]
                else:
                    trapped_rain += (rightwall-height[r])
                r -= 1

        return trapped_rain

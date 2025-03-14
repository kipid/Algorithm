class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area
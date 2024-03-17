class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxArea = 0

        def isRect(row: int, row1: int, col:int, col1:int) -> bool:
            for r in range(row+1, row1):
                for c in range(col+1, col1):
                    if matrix[r][c] == "0":
                        return False
            return True

        def maxAreaRect(row: int, col: int) -> int:
            maxArea = 1
            row1 = row + 1
            while row1 < m and matrix[row1][col] == "1":
                row1 += 1
            maxArea = max(maxArea, row1-row)
            col1 = col + 1
            while col1 < n and matrix[row][col1] == "1":
                col1 += 1
            maxArea = max(maxArea, col1-col)
            if row+1 < m and col+1 < n and row1 > row+1 and col1 > col+1 and matrix[row+1][col+1] == "1":
                isFirstAndMaxArea = False
                r = row1
                c = col1
                if isRect(row, r, col, c):
                    return max(maxArea, (r-row)*(c-col))
                for r in range(row1, row, -1):
                    for c in range(col1, col, -1):
                        if maxArea < (r-row)*(c-col) and isRect(row, r, col, c):
                            maxArea = max(maxArea, (r-row)*(c-col))
            return maxArea

        if matrix[0][0] == "1":
            maxArea = max(maxArea, maxAreaRect(0, 0))
        if maxArea == m * n:
            return maxArea
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    maxArea = max(maxArea, maxAreaRect(row, col))
        return maxArea
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # minSumOfPath[m][n] = min(minSumOfPath[m-1][n]+grid[m][n], minSumOfPath[m][n-1]+grid[m][n])
        m = len(grid)
        n = len(grid[0])
        minSumOfPath = [[0] * n for _ in range(m)]
        minSumOfPath[0][0] = grid[0][0]
        for j in range(1, n):
            minSumOfPath[0][j] = grid[0][j] + minSumOfPath[0][j-1]
        for i in range(1, m):
            minSumOfPath[i][0] = grid[i][0] + minSumOfPath[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                minSumOfPath[i][j] = grid[i][j] + min(minSumOfPath[i-1][j], minSumOfPath[i][j-1])
        return minSumOfPath[m-1][n-1]
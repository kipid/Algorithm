class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = int(matrix[i][0])

        for j in range(n):
            dp[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return max(max(dp[i]) for i in range(m)) ** 2
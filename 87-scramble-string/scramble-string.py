class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        n = len(s1)
        # dp[i][j][k] represents whether s2[j:j+k] is a scrambled string of s1[i:i+k]
        dp = [[[False] * (n + 1) for _ in range(n)] for _ in range(n)]

        # Initialize base cases (single characters)
        for i in range(n):
            for j in range(n):
                dp[i][j][1] = (s1[i] == s2[j])

        # Build up the solution for longer substrings
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                for j in range(n - k + 1):
                    for m in range(1, k):
                        # Check if s2[j:j+m] and s2[j+m:j+k] are scrambled versions
                        if (dp[i][j][m] and dp[i + m][j + m][k - m]) or \
                        (dp[i][j + k - m][m] and dp[i + m][j][k - m]):
                            dp[i][j][k] = True
                            break

        return dp[0][0][n]
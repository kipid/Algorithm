function longestCommonSubsequence(text1: string, text2: string): number {
    const m = text1.length;
    const n = text2.length;
    
    // Create a 2D DP array with size (m+1) x (n+1)
    const dp: number[][] = Array(m + 1).fill(0)
        .map(() => Array(n + 1).fill(0));
    
    // Fill the DP table
    for (let i = 1; i <= m; i++) {
        for (let j = 1; j <= n; j++) {
            if (text1[i - 1] === text2[j - 1]) {
                // If characters match, add 1 to the LCS of prefixes
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                // If no match, take maximum of skipping either character
                dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }
    
    return dp[m][n];
};